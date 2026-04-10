# discord-alerts-kit

A simple Python library to build Discord alert bots in minutes.

No boilerplate, no headaches — plug your data source and go.

[![PyPI version](https://badge.fury.io/py/discord-alerts-kit.svg)](https://pypi.org/project/discord-alerts-kit/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

```bash
pip install discord-alerts-kit
```

## Quick Start

```python
from discord_alerts_kit import AlertBot, get_free_epic_games

bot = AlertBot(config_path="config.yaml")

# Use a built-in source
bot.add_source(get_free_epic_games)

# Or create your own
@bot.add_source
def my_alerts():
    return [
        {
            "title": "🔔 My Alert",
            "description": "Something happened!",
            "url": "https://example.com",
            "footer": "my-bot"
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
check_interval: 10
```

## Features

- 🔌 Plug any data source in one function
- 🎮 Built-in sources: Epic Games, Steam free games
- 📨 Auto DM subscribers
- 🔕 Anti-duplicate system — never send the same alert twice
- ⏰ Configurable check interval
- 🎨 Custom embeds with colors, thumbnails, fields
- ⚙️ YAML config
- `/subscribe` `/unsubscribe` `/status` slash commands

## Built-in Sources

```python
from discord_alerts_kit import get_free_epic_games, get_free_steam_games

bot.add_source(get_free_epic_games)
bot.add_source(get_free_steam_games)
```

## Slash Commands

| Command | Description |
|---|---|
| `/subscribe` | Subscribe to DM alerts |
| `/unsubscribe` | Unsubscribe from alerts |
| `/status` | Show bot status |

## License

MIT