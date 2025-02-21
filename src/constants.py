from dotenv import load_dotenv
from enum import IntEnum
import os

load_dotenv()

RELEASE: bool = os.getenv("RELEASE", "") != ""
DB_DIR: str = "data"

if RELEASE:
    os.makedirs(DB_DIR, exist_ok=True)

CONNECTION_STRING = f"sqlite:///{DB_DIR}/tag_settings.db"

APP_ID: int = os.getenv("APP_ID", 0)
APP_HASH: str = os.getenv("APP_HASH", "")
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

assert APP_ID != 0 and APP_HASH != "" and BOT_TOKEN != "", "Credentials must be set"

DEFAULT_MESSAGE: str = "Нет пользователей для оповещение"

class ToggleExitCode(IntEnum):
    TURNED_OFF = 0
    TURNED_ON = 1
    ERROR = 2
