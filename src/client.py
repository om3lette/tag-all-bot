from telethon import TelegramClient
from src.configs import api_config, bot_config
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    datefmt="%H:%M:%S %d-%m-%Y"
)
logger = logging.getLogger(__name__)

client = TelegramClient('tag_all', api_config.api_id, api_config.api_hash).start(bot_token=bot_config.bot_token)
