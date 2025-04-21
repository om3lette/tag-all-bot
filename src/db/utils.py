from sqlalchemy import select
from src.db.engine import engine, SessionLocal
from src.db.models import MuteEntry
from src.db.base import Base

def create_db_metadata():
    Base.metadata.create_all(engine)

def toggle_mention_in_chat(user_id: int, chat_id: int) -> bool:
    """
    Creates or deletes if present a user entry with a given user_id and chat_id\n
    :returns bool whether or not an entry was created
    """
    with SessionLocal() as session:
        stmt = select(MuteEntry).where(
            MuteEntry.user_id == user_id,
            MuteEntry.chat_id == chat_id
        )
        entry = session.scalar(stmt)

        was_created: bool = False
        if entry:
            session.delete(entry)
        else:
            session.add(MuteEntry(user_id=user_id, chat_id=chat_id))
            was_created = True

        session.commit()
        return was_created

def get_muted_users_by_chat_id(chat_id: int) -> list[int]:
    with SessionLocal() as session:
        stmt = select(MuteEntry.user_id).where(MuteEntry.chat_id == chat_id)
        return session.scalars(stmt).all()
