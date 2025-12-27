import os

import discord
from discord import app_commands
from dotenv import load_dotenv

from search import build_fallback_url, search_docs


load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")


class DocsSearchBot(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync()


client = DocsSearchBot()


@client.tree.command(name="search", description="Search GL.iNet docs with tag keywords.")
@app_commands.describe(tags="Keywords/tags to search for (separate with spaces or commas)")
async def search(interaction: discord.Interaction, tags: str) -> None:
    await interaction.response.defer(thinking=True)

    tag_list = [tag for tag in tags.replace(",", " ").split(" ") if tag.strip()]

    try:
        results = search_docs(tag_list, limit=10)
    except Exception:
        fallback_url = build_fallback_url(tag_list)
        await interaction.followup.send(
            f"I couldn't reach the search provider right now. Try this link instead: {fallback_url}",
        )
        return

    if not results:
        fallback_url = build_fallback_url(tag_list)
        await interaction.followup.send(
            f"No results found. Try broader tags or use: {fallback_url}",
        )
        return

    lines = [f"**Top {len(results)} results for:** `{tags}`"]
    for index, result in enumerate(results, start=1):
        snippet = f" — {result.snippet}" if result.snippet else ""
        lines.append(f"{index}. [{result.title}]({result.url}){snippet}")

    await interaction.followup.send("\n".join(lines))


if __name__ == "__main__":
    if not TOKEN:
        raise SystemExit("DISCORD_BOT_TOKEN is not set.")

    client.run(TOKEN)
