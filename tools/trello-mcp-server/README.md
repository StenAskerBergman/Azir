# trello-mcp-server

Local stdio MCP server for the Trello REST API. 15 tools: boards, lists, cards (list/get/create/update/move/archive), comments, search, checklists, labels. Nothing is ever hard-deleted; "archive" is reversible.

## Setup (one time)

1. Create a Power-Up at https://trello.com/power-ups/admin, copy its **API key**, then use "generate a Token" on that page (read + write).
2. Store them as user environment variables (never commit them):

```powershell
setx TRELLO_API_KEY "<your key>"
setx TRELLO_TOKEN "<your token>"
```

3. Restart Claude Code / the desktop app so it inherits them, then approve the `trello` server from the repo-root `.mcp.json`.

## Build / verify

```powershell
npm install
npm run build
npm run smoke   # offline checks always; live board listing when the env vars are set
```

Board: https://trello.com/b/kCzJIYNA/runeterra-shurima (Planner.md: reading is expected, editing/commenting needs the author's go-ahead per action).
