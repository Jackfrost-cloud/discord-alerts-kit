import yaml
import os

DEFAULT_CONFIG = {
    "token": "",
    "prefix": "!",
    "alert_channel": None,
    "dm_subscribers": False,
    "color": 0x00ff00
}

def load_config(path: str = "config.yaml") -> dict:
    if not os.path.exists(path):
        return DEFAULT_CONFIG.copy()
    
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    
    return {**DEFAULT_CONFIG, **data}