import json
import os
import hashlib

STORAGE_FILE = "sent_alerts.json"

def _load() -> set:
    if not os.path.exists(STORAGE_FILE):
        return set()
    with open(STORAGE_FILE, "r") as f:
        return set(json.load(f))

def _save(data: set):
    with open(STORAGE_FILE, "w") as f:
        json.dump(list(data), f)

def hash_alert(alert: dict) -> str:
    key = f"{alert.get('title', '')}{alert.get('url', '')}"
    return hashlib.md5(key.encode()).hexdigest()

def is_duplicate(alert: dict) -> bool:
    sent = _load()
    return hash_alert(alert) in sent

def mark_sent(alert: dict):
    sent = _load()
    sent.add(hash_alert(alert))
    _save(sent)