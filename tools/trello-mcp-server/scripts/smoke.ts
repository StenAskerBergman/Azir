/**
 * Self-check: starts the built server over stdio and exercises read-only tools.
 * Run: npm run build && npm run smoke
 * Without TRELLO_API_KEY/TRELLO_TOKEN only the offline checks run.
 */
import { strict as assert } from "node:assert";
import { Client } from "@modelcontextprotocol/client";
import { getDefaultEnvironment, StdioClientTransport } from "@modelcontextprotocol/client/stdio";

const live = !!(process.env.TRELLO_API_KEY && process.env.TRELLO_TOKEN);
const client = new Client({ name: "smoke-test", version: "1.0.0" });
await client.connect(
  new StdioClientTransport({
    command: "node",
    args: ["dist/index.js"],
    env: {
      ...getDefaultEnvironment(),
      TRELLO_API_KEY: process.env.TRELLO_API_KEY ?? "",
      TRELLO_TOKEN: process.env.TRELLO_TOKEN ?? ""
    }
  })
);

const { tools } = await client.listTools();
const names = tools.map(t => t.name);
console.error(`${names.length} tools: ${names.join(", ")}`);
for (const n of ["trello_list_boards", "trello_get_card", "trello_create_card", "trello_add_comment"]) {
  assert.ok(names.includes(n), `missing ${n}`);
}

const invalid = await client.callTool({ name: "trello_get_card", arguments: {} });
assert.equal(invalid.isError, true, "missing card_id must be rejected");

if (!live) {
  const noCreds = await client.callTool({ name: "trello_list_boards", arguments: {} });
  assert.equal(noCreds.isError, true);
  assert.match(JSON.stringify(noCreds.content), /TRELLO_API_KEY/);
  console.error("Offline checks passed (set TRELLO_API_KEY/TRELLO_TOKEN for live checks)");
} else {
  const boards = await client.callTool({ name: "trello_list_boards", arguments: {} });
  assert.ok(!boards.isError, JSON.stringify(boards.content));
  console.error(JSON.stringify(boards.content).slice(0, 400));
  console.error("Live checks passed");
}
await client.close();
