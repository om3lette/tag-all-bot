from telethon import events
from src.db import toggle_mention_in_chat
import src.reply_messages as messages
from src.main import client

@client.on(events.NewMessage(pattern="/toggle_tag"))
async def toggle_mute(event: events.NewMessage.Event):
    is_created: bool = toggle_mention_in_chat(event.sender_id, event.chat_id)
    message_text: str = messages.USER_MUTED if is_created else messages.USER_UNMUTED
    await event.reply(message_text)