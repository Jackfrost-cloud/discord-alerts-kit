from .alerts import AlertBot
from .embed import build_embed
from .config import load_config
from .sources import get_free_epic_games, get_free_steam_games

__version__ = "0.5.0"
__author__ = "jackfrost_13"

__all__ = ["AlertBot", "build_embed", "load_config", "get_free_epic_games", "get_free_steam_games"]