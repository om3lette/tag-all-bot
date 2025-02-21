from telethon import TelegramClient, events
from src.constants import APP_ID, APP_HASH, ToggleExitCode, DEFAULT_MESSAGE, BOT_TOKEN
from src.db import get_no_disturb_users, toggle_no_disturb
import logging

logging.basicConfig(level=logging.INFO)

bot = TelegramClient("tagAll", APP_ID, APP_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern="/toggle_tag"))
async def toggle_tag(event: events.NewMessage.Event):
    response: ToggleExitCode = toggle_no_disturb(event.message.from_id.user_id, event.chat_id)
    if response == ToggleExitCode.TURNED_OFF:
        await event.reply("Оповещения выключены")
        return
    if response == ToggleExitCode.TURNED_ON:
        await event.reply("Оповещения включены!")
        return
    await event.reply("Что-то пошло не так. Попробуйте позже")


@bot.on(events.NewMessage(pattern="@all"))
async def main(event: events.NewMessage.Event):
    # Do not respond in DM
    if event.chat_id > 0:
        return

    muted_users = {user.user_id for user in get_no_disturb_users(event.chat_id)}
    users = [
        user for user in await bot.get_participants(event.chat)
        if not user.bot and user.id not in muted_users
    ]

    output: str = ""
    missing_cnt: int = 0

    for user in users:
        # No need to tag bots
        if user.username == "" and user.username is None:
            # User didn't specify username
            missing_cnt += 1
            continue
        output += f"[.](https://t.me/{user.username})"
    if missing_cnt > 0:
        output += f"\n{missing_cnt} пользователей не было оповещено. Имена пользователей не указаны"
    if output == "":
        output = DEFAULT_MESSAGE
    await event.reply(output, link_preview=False)

if __name__ == "__main__":
    bot.run_until_disconnected()