import aiohttp

STEAM_API = "https://store.steampowered.com/api/featuredcategories"

async def get_free_steam_games():
    async with aiohttp.ClientSession() as session:
        async with session.get(STEAM_API) as r:
            data = await r.json()

    free = []
    specials = data.get("specials", {}).get("items", [])

    for game in specials:
        if game.get("discount_percent") == 100:
            free.append({
                "title": f"🎮 {game['name']} — Gratuit sur Steam !",
                "description": f"Prix original : {game.get('original_price', 0) / 100:.2f}€",
                "url": f"https://store.steampowered.com/app/{game['id']}",
                "footer": "discord-alerts-kit • Steam"
            })

    return free