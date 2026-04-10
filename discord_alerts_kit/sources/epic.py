import aiohttp

EPIC_API = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"

async def get_free_epic_games():
    async with aiohttp.ClientSession() as session:
        async with session.get(EPIC_API) as r:
            data = await r.json()
    
    games = data["data"]["Catalog"]["searchStore"]["elements"]
    free = []
    
    for game in games:
        promotions = game.get("promotions")
        if not promotions:
            continue
        offers = promotions.get("promotionalOffers", [])
        if not offers:
            continue
        for offer in offers:
            for o in offer.get("promotionalOffers", []):
                if o["discountSetting"]["discountPercentage"] == 0:
                    free.append({
                        "title": f"🎮 {game['title']} — Gratuit sur Epic !",
                        "description": game.get("description", "")[:200],
                        "url": f"https://store.epicgames.com/p/{game.get('productSlug', '')}",
                        "footer": "discord-alerts-kit • Epic Games"
                    })
    return free