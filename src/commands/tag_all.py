from telethon import events
from src.utils import create_mentioning_text, fetch_and_exclude_muted_users
from src.configs import bot_config
import src.reply_messages as messages
from src.main import client

@client.on(events.NewMessage(pattern=f"@(all|everyone|{bot_config.bot_username})"))
async def tag_all(event: events.NewMessage.Event):
    users_to_tag = fetch_and_exclude_muted_users(await client.get_participants(event.chat_id), event.chat_id)
    message_text: str = create_mentioning_text(users_to_tag)
    await event.reply(message_text if message_text != "" else messages.NO_USERS_TO_TAG)
