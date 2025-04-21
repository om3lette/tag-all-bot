from telethon.tl.types import User
from src.db import get_muted_users_by_chat_id

def create_mentioning_text(users: list[User]):
    out_message = ""
    for user in users:
        if not should_user_be_mentioned(user):
            continue
        out_message += f"[.](@{user.username})"

    return out_message

def fetch_and_exclude_muted_users(users: list[User], chat_id: int):
    muted_users = get_muted_users_by_chat_id(chat_id)
    return [user for user in users if not is_user_muted(muted_users, user)]

def is_user_muted(muted_users: list[int], user: User) -> bool:
    return user.id in muted_users

def should_user_be_mentioned(user: User) -> bool:
    """Checks if a given user should be included in the message"""
    return not user.bot and user.username not in ["", None]