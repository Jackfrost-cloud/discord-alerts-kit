from discord_alerts_kit import AlertBot

bot = AlertBot(config_path="config.yaml")

# Exemple de source d'alertes — tu remplace ça par ton vrai scraper
@bot.add_source
def free_games():
    return [
        {
            "title": "🎮 Jeu gratuit détecté !",
            "description": "Epic Games offre **GTA V** gratuitement",
            "url": "https://epicgames.com",
            "footer": "discord-alerts-kit • free games"
        }
    ]

bot.run_bot()