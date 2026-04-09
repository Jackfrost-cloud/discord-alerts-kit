import discord
from datetime import datetime

def build_embed(
    title: str,
    description: str = "",
    url: str = None,
    color: int = 0x00ff00,
    footer: str = None,
    thumbnail: str = None,
    fields: list = []
) -> discord.Embed:
    
    embed = discord.Embed(
        title=title,
        description=description,
        color=color,
        timestamp=datetime.utcnow()
    )

    if url:
        embed.url = url

    if footer:
        embed.set_footer(text=footer)

    if thumbnail:
        embed.set_thumbnail(url=thumbnail)

    for field in fields:
        embed.add_field(
            name=field.get("name", ""),
            value=field.get("value", ""),
            inline=field.get("inline", False)
        )

    return embed