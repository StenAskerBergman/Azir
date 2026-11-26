const API_BASE_URL = "https://api.trello.com/1";
const REQUEST_TIMEOUT_MS = 30_000;

export class ApiError extends Error {
  constructor(
    readonly status: number,
    detail: string
  ) {
    super(httpErrorMessage(status, detail));
  }
}

function httpErrorMessage(status: number, detail: string): string {
  const suffix = detail ? ` (Trello said: ${detail.slice(0, 200)})` : "";
  switch (status) {
    case 400:
      return `Trello rejected the request as invalid${suffix}. Check ID formats and field values.`;
    case 401:
      return `Trello rejected the credentials${suffix}. Check that TRELLO_API_KEY and TRELLO_TOKEN are set and the token has not been revoked.`;
    case 403:
      return `Permission denied${suffix}. The token needs read,write scope and membership on this board.`;
    case 404:
      return `Not found${suffix}. Check the ID; trello_list_boards, trello_list_lists and trello_list_cards return valid IDs.`;
    case 429:
      return `Trello rate limit hit${suffix}. Wait ~10 seconds and retry.`;
    default:
      return `Trello returned HTTP ${status}${suffix}.`;
  }
}

function credentials(): { key: string; token: string } {
  const key = process.env.TRELLO_API_KEY;
  const token = process.env.TRELLO_TOKEN;
  if (!key || !token) {
    throw new Error(
      "TRELLO_API_KEY and TRELLO_TOKEN must be set in the MCP server's environment. " +
        "Get a key at https://trello.com/power-ups/admin and generate a token from that key's page."
    );
  }
  return { key, token };
}

type Params = Record<string, string | number | boolean | undefined>;

export async function trello<T>(
  method: "GET" | "POST" | "PUT" | "DELETE",
  path: string,
  params: Params,
  signal: AbortSignal
): Promise<T> {
  const { key, token } = credentials();
  const url = new URL(`${API_BASE_URL}${path}`);
  for (const [name, value] of Object.entries(params)) {
    if (value !== undefined) url.searchParams.set(name, String(value));
  }

  let response: Response;
  try {
    response = await fetch(url, {
      method,
      headers: {
        // Header auth keeps the secret out of URLs and error messages
        Authorization: `OAuth oauth_consumer_key="${key}", oauth_token="${token}"`,
        Accept: "application/json"
      },
      signal: AbortSignal.any([signal, AbortSignal.timeout(REQUEST_TIMEOUT_MS)])
    });
  } catch (error) {
    if (error instanceof DOMException && error.name === "TimeoutError") {
      throw new Error("Trello did not respond within 30 seconds. Try again.");
    }
    throw error;
  }
  if (!response.ok) throw new ApiError(response.status, await response.text().catch(() => ""));
  const text = await response.text();
  return (text ? JSON.parse(text) : {}) as T;
}
