# discord-alerts-kit

A simple Python library to build Discord alert bots in minutes.

No boilerplate, no headaches — just plug your data source and go.

## Installation

```bash
pip install discord-alerts-kit
```

## Quick Start

```python
from discord_alerts_kit import AlertBot

bot = AlertBot(config_path="config.yaml")

@bot.add_source
def my_alerts():
    return [
        {
            "title": "🎮 Free Game!",
            "description": "GTA V is free on Epic Games",
            "url": "https://epicgames.com",
            "footer": "discord-alerts-kit"
        }
    ]

bot.run_bot()
```

## Configuration

```yaml
token: "YOUR_BOT_TOKEN"
prefix: "!"
alert_channel: 123456789
dm_subscribers: true
color: 0x00ff00
```

## Features

- 🔌 Plug any data source in one function
- 📨 Auto DM subscribers
- 🎨 Custom embeds with colors, thumbnails, fields
- ⚙️ YAML config
- 🔄 Auto check every 10 minutes

## License

MIT