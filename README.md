# glinet_discord_search_docs.gl-inet.com

Discord bot that searches https://docs.gl-inet.com/ with tag keywords and returns the top 10 results.

## Setup

1. Create a Discord application + bot and copy the bot token.
2. Invite the bot with `applications.commands` scope.
3. Create a `.env` file using `.env.example` and add your token.
4. Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python bot.py
```

## Usage

Use the `/search` slash command with tags:

```
/search tags: vpn client setup
```
