#!/usr/bin/env node
/**
 * Trello MCP server (stdio). Credentials come from TRELLO_API_KEY and TRELLO_TOKEN.
 */
import { McpServer } from "@modelcontextprotocol/server";
import { serveStdio } from "@modelcontextprotocol/server/stdio";
import * as z from "zod/v4";
import { trello } from "./api.js";

const CHARACTER_LIMIT = 25_000;

enum ResponseFormat {
  MARKDOWN = "markdown",
  JSON = "json"
}

const fmtField = z
  .enum(ResponseFormat)
  .default(ResponseFormat.MARKDOWN)
  .describe("'markdown' for readable text, 'json' for raw data");

const READ = { readOnlyHint: true, destructiveHint: false, idempotentHint: true, openWorldHint: true };
const WRITE = { readOnlyHint: false, destructiveHint: false, idempotentHint: false, openWorldHint: true };
const UPDATE = { readOnlyHint: false, destructiveHint: false, idempotentHint: true, openWorldHint: true };

type Result = { content: { type: "text"; text: string }[] };
const text = (value: string): Result => ({ content: [{ type: "text", text: value }] });

/** Render items in the requested format, dropping items from the tail until under CHARACTER_LIMIT. */
function renderList<T>(
  title: string,
  items: T[],
  format: ResponseFormat,
  line: (item: T) => string
): Result {
  const render = (shown: T[]): string => {
    if (format === ResponseFormat.JSON) {
      return JSON.stringify({ total: items.length, shown: shown.length, items: shown }, null, 2);
    }
    const lines = [`# ${title}`, `Showing ${shown.length} of ${items.length}.`, "", ...shown.map(line)];
    if (shown.length < items.length) lines.push("", "Output truncated; narrow the query or use a smaller limit.");
    return lines.join("\n");
  };
  let shown = items;
  let out = render(shown);
  while (shown.length > 1 && out.length > CHARACTER_LIMIT) {
    shown = shown.slice(0, Math.ceil(shown.length / 2));
    out = render(shown);
  }
  return text(items.length === 0 ? `${title}: nothing found.` : out);
}

interface Board { id: string; name: string; url: string; desc?: string; closed?: boolean; lists?: TList[]; labels?: Label[] }
interface TList { id: string; name: string; closed?: boolean; idBoard?: string }
interface Label { id: string; name: string; color: string | null }
interface Card {
  id: string; name: string; desc?: string; url: string; idList: string; closed?: boolean; due?: string | null;
  dueComplete?: boolean; labels?: Label[]; idShort?: number; shortUrl?: string;
  checklists?: Checklist[]; badges?: { comments?: number; attachments?: number };
}
interface CheckItem { id: string; name: string; state: "complete" | "incomplete" }
interface Checklist { id: string; name: string; idCard?: string; checkItems: CheckItem[] }
interface CommentAction { id: string; date: string; memberCreator?: { fullName?: string }; data: { text?: string } }

const cardLine = (c: Card): string => {
  const labels = (c.labels ?? []).map(l => l.name || l.color).filter(Boolean).join(", ");
  const due = c.due ? ` · due ${c.due.slice(0, 10)}${c.dueComplete ? " ✓" : ""}` : "";
  return `- **${c.name}** (id: ${c.id}${c.idShort ? `, #${c.idShort}` : ""})${labels ? ` [${labels}]` : ""}${due}${c.closed ? " · archived" : ""}`;
};

const ID = (what: string) => z.string().min(1).describe(`${what} (Trello id, 24-char hex; for boards the short id from the URL also works)`);

function createServer(): McpServer {
  const server = new McpServer({ name: "trello-mcp-server", version: "1.0.0" });

  // ---------- Boards & lists ----------

  server.registerTool(
    "trello_list_boards",
    {
      title: "List Boards",
      description:
        "List the authenticated user's Trello boards (id, name, url). Start here to find a board id. Example: \"what boards do I have?\"",
      inputSchema: z.strictObject({
        include_closed: z.boolean().default(false).describe("Also include archived boards"),
        response_format: fmtField
      }),
      annotations: READ
    },
    async ({ include_closed, response_format }, ctx) => {
      const boards = await trello<Board[]>(
        "GET",
        "/members/me/boards",
        { filter: include_closed ? "all" : "open", fields: "name,url,closed,desc" },
        ctx.mcpReq.signal
      );
      return renderList("Trello boards", boards, response_format, b => `- **${b.name}** (id: ${b.id}) ${b.url}${b.closed ? " · archived" : ""}`);
    }
  );

  server.registerTool(
    "trello_get_board",
    {
      title: "Get Board",
      description:
        "Get one board with its open lists and labels. Use trello_list_cards for the cards. Example: \"show the lists on the Runeterra board\".",
      inputSchema: z.strictObject({ board_id: ID("Board id or short id"), response_format: fmtField }),
      annotations: READ
    },
    async ({ board_id, response_format }, ctx) => {
      const b = await trello<Board>(
        "GET",
        `/boards/${encodeURIComponent(board_id)}`,
        { fields: "name,url,desc,closed", lists: "open", list_fields: "name", labels: "all", label_fields: "name,color" },
        ctx.mcpReq.signal
      );
      if (response_format === ResponseFormat.JSON) return text(JSON.stringify(b, null, 2));
      const lines = [`# ${b.name} (id: ${b.id})`, b.url, b.desc ? `\n${b.desc}` : "", "", "## Lists"];
      for (const l of b.lists ?? []) lines.push(`- ${l.name} (id: ${l.id})`);
      lines.push("", "## Labels");
      for (const l of b.labels ?? []) lines.push(`- ${l.name || "(unnamed)"} · ${l.color ?? "none"} (id: ${l.id})`);
      return text(lines.join("\n"));
    }
  );

  server.registerTool(
    "trello_create_list",
    {
      title: "Create List",
      description: "Create a new list (column) on a board. Appended at the end unless position='top'.",
      inputSchema: z.strictObject({
        board_id: ID("Board id"),
        name: z.string().min(1).max(16384).describe("List name, e.g. 'Playtest feedback'"),
        position: z.enum(["top", "bottom"]).default("bottom")
      }),
      annotations: WRITE
    },
    async ({ board_id, name, position }, ctx) => {
      const l = await trello<TList>("POST", "/lists", { idBoard: board_id, name, pos: position }, ctx.mcpReq.signal);
      return text(`Created list "${l.name}" (id: ${l.id}).`);
    }
  );

  server.registerTool(
    "trello_update_list",
    {
      title: "Update List",
      description: "Rename or archive/unarchive a list. Archiving is reversible; nothing is deleted.",
      inputSchema: z.strictObject({
        list_id: ID("List id"),
        name: z.string().min(1).optional().describe("New name"),
        archived: z.boolean().optional().describe("true to archive, false to restore")
      }),
      annotations: UPDATE
    },
    async ({ list_id, name, archived }, ctx) => {
      const l = await trello<TList>("PUT", `/lists/${list_id}`, { name, closed: archived }, ctx.mcpReq.signal);
      return text(`List "${l.name}" (id: ${l.id}) updated${l.closed ? " (archived)" : ""}.`);
    }
  );

  // ---------- Cards ----------

  server.registerTool(
    "trello_list_cards",
    {
      title: "List Cards",
      description:
        "List cards on a list or on a whole board (give exactly one of list_id / board_id). Returns names, ids, labels, due dates; descriptions are omitted — use trello_get_card for full detail. Example: \"what's in the TODO list?\"",
      inputSchema: z.strictObject({
        list_id: z.string().optional().describe("List id"),
        board_id: z.string().optional().describe("Board id (all open cards on the board)"),
        include_archived: z.boolean().default(false).describe("Include archived cards (board_id only)"),
        limit: z.number().int().min(1).max(1000).default(200).describe("Max cards to return"),
        response_format: fmtField
      }),
      annotations: READ
    },
    async ({ list_id, board_id, include_archived, limit, response_format }, ctx) => {
      if (!!list_id === !!board_id) throw new Error("Provide exactly one of list_id or board_id.");
      const path = list_id ? `/lists/${list_id}/cards` : `/boards/${encodeURIComponent(board_id!)}/cards/${include_archived ? "all" : "open"}`;
      const cards = await trello<Card[]>(
        "GET",
        path,
        { fields: "name,idList,idShort,labels,due,dueComplete,closed,url", limit },
        ctx.mcpReq.signal
      );
      return renderList("Trello cards", cards.slice(0, limit), response_format, c => cardLine(c) + (board_id ? ` · list ${c.idList}` : ""));
    }
  );

  server.registerTool(
    "trello_get_card",
    {
      title: "Get Card",
      description:
        "Get one card in full: description, labels, due date, checklists with item ids and states, and recent comments. Example: \"read card 81\".",
      inputSchema: z.strictObject({ card_id: ID("Card id or the board-local number"), response_format: fmtField }),
      annotations: READ
    },
    async ({ card_id, response_format }, ctx) => {
      const id = encodeURIComponent(card_id);
      const [card, comments] = await Promise.all([
        trello<Card>("GET", `/cards/${id}`, { checklists: "all", fields: "all" }, ctx.mcpReq.signal),
        trello<CommentAction[]>("GET", `/cards/${id}/actions`, { filter: "commentCard", limit: 20 }, ctx.mcpReq.signal)
      ]);
      if (response_format === ResponseFormat.JSON) return text(JSON.stringify({ card, comments }, null, 2));
      const lines = [`# ${card.name}`, `id: ${card.id} · list: ${card.idList} · ${card.url}${card.closed ? " · archived" : ""}`];
      if (card.due) lines.push(`Due: ${card.due}${card.dueComplete ? " (done)" : ""}`);
      const labels = (card.labels ?? []).map(l => `${l.name || l.color} (id: ${l.id})`).join(", ");
      if (labels) lines.push(`Labels: ${labels}`);
      lines.push("", card.desc || "(no description)");
      for (const cl of card.checklists ?? []) {
        lines.push("", `## Checklist: ${cl.name} (id: ${cl.id})`);
        for (const it of cl.checkItems) lines.push(`- [${it.state === "complete" ? "x" : " "}] ${it.name} (id: ${it.id})`);
      }
      if (comments.length) {
        lines.push("", "## Comments");
        for (const c of comments) lines.push(`- ${c.date.slice(0, 10)} ${c.memberCreator?.fullName ?? "?"}: ${c.data.text ?? ""}`);
      }
      return text(lines.join("\n").slice(0, CHARACTER_LIMIT));
    }
  );

  server.registerTool(
    "trello_create_card",
    {
      title: "Create Card",
      description:
        "Create a card at the bottom of a list (or top with position='top'). Use trello_list_boards/trello_get_board to find the list id. Example: \"add a TODO card 'Fix Nazumah loc keys'\".",
      inputSchema: z.strictObject({
        list_id: ID("List id"),
        name: z.string().min(1).max(16384).describe("Card title"),
        desc: z.string().max(16384).optional().describe("Markdown description"),
        due: z.string().optional().describe("Due date, ISO 8601 e.g. 2026-12-01 or 2026-12-01T18:00:00Z"),
        label_ids: z.array(z.string()).optional().describe("Label ids from trello_get_board"),
        position: z.enum(["top", "bottom"]).default("bottom")
      }),
      annotations: WRITE
    },
    async ({ list_id, name, desc, due, label_ids, position }, ctx) => {
      const c = await trello<Card>(
        "POST",
        "/cards",
        { idList: list_id, name, desc, due, idLabels: label_ids?.join(","), pos: position },
        ctx.mcpReq.signal
      );
      return text(`Created card "${c.name}" (id: ${c.id}) ${c.url}`);
    }
  );

  server.registerTool(
    "trello_update_card",
    {
      title: "Update Card",
      description:
        "Edit a card: rename, change description/due date, move it to another list (list_id), reorder, or archive/restore it. Only the fields you pass change. Nothing is deleted. Example: \"move this card to Done\" -> list_id of Done.",
      inputSchema: z.strictObject({
        card_id: ID("Card id"),
        name: z.string().min(1).optional(),
        desc: z.string().optional().describe("Replaces the whole description"),
        list_id: z.string().optional().describe("Move to this list"),
        board_id: z.string().optional().describe("Needed only when moving to a list on a different board"),
        due: z.string().optional().describe("ISO 8601 date; empty string clears the due date"),
        due_complete: z.boolean().optional(),
        archived: z.boolean().optional().describe("true to archive, false to restore"),
        position: z.enum(["top", "bottom"]).optional()
      }),
      annotations: UPDATE
    },
    async ({ card_id, name, desc, list_id, board_id, due, due_complete, archived, position }, ctx) => {
      const c = await trello<Card>(
        "PUT",
        `/cards/${encodeURIComponent(card_id)}`,
        { name, desc, idList: list_id, idBoard: board_id, due, dueComplete: due_complete, closed: archived, pos: position },
        ctx.mcpReq.signal
      );
      return text(`Updated card "${c.name}" (id: ${c.id}), list ${c.idList}${c.closed ? ", archived" : ""}.`);
    }
  );

  server.registerTool(
    "trello_add_comment",
    {
      title: "Add Comment",
      description: "Post a comment on a card as the authenticated user. Visible to board members, so confirm wording with the user first.",
      inputSchema: z.strictObject({ card_id: ID("Card id"), text: z.string().min(1).max(16384).describe("Comment text (markdown)") }),
      annotations: WRITE
    },
    async ({ card_id, text: body }, ctx) => {
      await trello("POST", `/cards/${encodeURIComponent(card_id)}/actions/comments`, { text: body }, ctx.mcpReq.signal);
      return text(`Comment added to card ${card_id}.`);
    }
  );

  server.registerTool(
    "trello_search",
    {
      title: "Search Trello",
      description:
        "Full-text search across the user's cards (and optionally boards). Example: \"find cards mentioning Moonstone\". Optionally restrict to board ids.",
      inputSchema: z.strictObject({
        query: z.string().min(1).describe("Search text; Trello operators like label:red or list:\"TODO\" work"),
        board_ids: z.array(z.string()).optional().describe("Restrict to these boards"),
        limit: z.number().int().min(1).max(100).default(20),
        response_format: fmtField
      }),
      annotations: READ
    },
    async ({ query, board_ids, limit, response_format }, ctx) => {
      const r = await trello<{ cards: Card[] }>(
        "GET",
        "/search",
        {
          query,
          modelTypes: "cards",
          cards_limit: limit,
          idBoards: board_ids?.join(",") ?? "mine",
          card_fields: "name,idList,idShort,labels,due,dueComplete,closed,url"
        },
        ctx.mcpReq.signal
      );
      return renderList(`Search: ${query}`, r.cards, response_format, c => `${cardLine(c)} · list ${c.idList}`);
    }
  );

  // ---------- Checklists ----------

  server.registerTool(
    "trello_create_checklist",
    {
      title: "Create Checklist",
      description: "Add an empty checklist to a card; optionally seed it with items. Returns the checklist id for trello_add_checklist_item.",
      inputSchema: z.strictObject({
        card_id: ID("Card id"),
        name: z.string().min(1).default("Checklist"),
        items: z.array(z.string().min(1)).optional().describe("Item names to add immediately")
      }),
      annotations: WRITE
    },
    async ({ card_id, name, items }, ctx) => {
      const cl = await trello<Checklist>("POST", "/checklists", { idCard: card_id, name }, ctx.mcpReq.signal);
      for (const item of items ?? []) {
        await trello("POST", `/checklists/${cl.id}/checkItems`, { name: item }, ctx.mcpReq.signal);
      }
      return text(`Created checklist "${cl.name}" (id: ${cl.id}) with ${items?.length ?? 0} items.`);
    }
  );

  server.registerTool(
    "trello_add_checklist_item",
    {
      title: "Add Checklist Item",
      description: "Append an item to an existing checklist (ids from trello_get_card).",
      inputSchema: z.strictObject({ checklist_id: ID("Checklist id"), name: z.string().min(1), checked: z.boolean().default(false) }),
      annotations: WRITE
    },
    async ({ checklist_id, name, checked }, ctx) => {
      const it = await trello<CheckItem>("POST", `/checklists/${checklist_id}/checkItems`, { name, checked }, ctx.mcpReq.signal);
      return text(`Added item "${it.name}" (id: ${it.id}).`);
    }
  );

  server.registerTool(
    "trello_set_checklist_item",
    {
      title: "Tick Checklist Item",
      description: "Mark a checklist item complete or incomplete. Needs the card id and the item id from trello_get_card.",
      inputSchema: z.strictObject({ card_id: ID("Card id"), item_id: ID("Checklist item id"), complete: z.boolean() }),
      annotations: UPDATE
    },
    async ({ card_id, item_id, complete }, ctx) => {
      await trello(
        "PUT",
        `/cards/${encodeURIComponent(card_id)}/checkItem/${item_id}`,
        { state: complete ? "complete" : "incomplete" },
        ctx.mcpReq.signal
      );
      return text(`Item ${item_id} marked ${complete ? "complete" : "incomplete"}.`);
    }
  );

  // ---------- Labels ----------

  server.registerTool(
    "trello_create_label",
    {
      title: "Create Label",
      description: "Create a label on a board. Colors: yellow, purple, blue, red, green, orange, black, sky, pink, lime (or omit for a colorless label).",
      inputSchema: z.strictObject({
        board_id: ID("Board id"),
        name: z.string().max(16384).default(""),
        color: z.enum(["yellow", "purple", "blue", "red", "green", "orange", "black", "sky", "pink", "lime"]).optional()
      }),
      annotations: WRITE
    },
    async ({ board_id, name, color }, ctx) => {
      const l = await trello<Label>("POST", "/labels", { idBoard: board_id, name, color }, ctx.mcpReq.signal);
      return text(`Created label "${l.name}" ${l.color ?? ""} (id: ${l.id}).`);
    }
  );

  server.registerTool(
    "trello_set_card_label",
    {
      title: "Add/Remove Card Label",
      description: "Attach or detach an existing label on a card (label ids from trello_get_board).",
      inputSchema: z.strictObject({ card_id: ID("Card id"), label_id: ID("Label id"), attach: z.boolean().default(true) }),
      annotations: UPDATE
    },
    async ({ card_id, label_id, attach }, ctx) => {
      const base = `/cards/${encodeURIComponent(card_id)}/idLabels`;
      if (attach) await trello("POST", base, { value: label_id }, ctx.mcpReq.signal);
      else await trello("DELETE", `${base}/${label_id}`, {}, ctx.mcpReq.signal);
      return text(`Label ${label_id} ${attach ? "attached to" : "removed from"} card ${card_id}.`);
    }
  );

  return server;
}

serveStdio(createServer);
console.error("trello-mcp-server running on stdio");
