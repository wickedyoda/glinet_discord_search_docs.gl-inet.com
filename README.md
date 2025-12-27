# GL.iNet Docs Search Discord Bot

A Discord slash-command bot that searches **https://docs.gl-inet.com** and returns the top 10 results based on the tags you provide.

---

## Features

- **Slash command**: `/search`
- **Domain restricted**: only searches `docs.gl-inet.com`
- **Top results**: returns up to 10 results with titles, links, and snippets
- **Fallback link**: if the search provider is unavailable, the bot returns a direct search URL
- **Docker-ready**: run the bot in a container

---

## Requirements

### Local

- **Python** 3.10+
- A **Discord application** and **bot token**

### Docker

- Docker Engine 20+

---

## Quick Start (Local)

1. **Clone and enter the repo**

   ```bash
   git clone <your-repo-url>
   cd glinet_discord_search_docs.gl-inet.com
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Copy the example file and add your token:

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and set:

   ```env
   DISCORD_BOT_TOKEN=your-token-here
   ```

5. **Run the bot**

   ```bash
   python bot.py
   ```

---

## Quick Start (Docker)

1. **Build the image**

   ```bash
   docker build -t glinet-docs-search:latest \
     -t glinet-docs-search:$(date +%Y%m%d%H%M%S) .
   ```

2. **Run the container**

   ```bash
   docker run --rm \
     --env DISCORD_BOT_TOKEN=your-token-here \
     glinet-docs-search:latest
   ```

> Tip: You can also use an `.env` file and `--env-file .env`.

---

## Discord Bot Setup

1. **Create a Discord application**
   - Go to https://discord.com/developers/applications
   - Click **New Application**

2. **Create a bot user**
   - In your application, go to **Bot**
   - Click **Add Bot**
   - Copy the **Token** and put it in your `.env`

3. **Invite the bot to your server**
   - Go to **OAuth2 → URL Generator**
   - Scopes:
     - `bot`
     - `applications.commands`
   - Bot permissions (minimum):
     - **Send Messages**
     - **Embed Links** (optional but recommended)
   - Use the generated URL to invite the bot

---

## Usage

Use the `/search` command inside Discord:

```
/search tags: vpn client setup
```

The bot will respond with up to 10 results from **docs.gl-inet.com**.

---

## How Search Works

- The bot builds a query like:

  ```
  site:docs.gl-inet.com <your tags>
  ```

- It fetches results from DuckDuckGo’s HTML endpoint and parses titles, URLs, and snippets.
- If the search provider is unavailable, it returns a fallback link you can open in a browser.

---

## Project Structure

```
.
├── bot.py              # Discord bot + slash command
├── search.py           # Search logic and result parsing
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
├── Dockerfile          # Container build
├── .dockerignore       # Container ignores
└── README.md           # Documentation
```

---

## Troubleshooting

- **Bot doesn’t respond to slash commands**
  - Make sure the bot was invited with the `applications.commands` scope.
  - Try restarting the bot to force command sync.

- **No search results**
  - Try different or broader tags.
  - The search provider may be rate-limiting or temporarily unavailable.

- **Token errors**
  - Confirm `DISCORD_BOT_TOKEN` is set in your `.env` file.

---

## Security Notes

- Never commit your real `.env` file.
- Regenerate your token if it’s exposed.

---

## License

MIT
