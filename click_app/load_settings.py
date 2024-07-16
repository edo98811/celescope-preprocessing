import json
from pathlib import Path
from typing import Any, dict


CONFIG_DIR = Path.home() / ".config" / "celescope"
CONFIG_FILE = CONFIG_DIR / "config.json"


def load_config(config_path: Path = CONFIG_FILE):
    try:
        with open(config_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Configuration file not found")