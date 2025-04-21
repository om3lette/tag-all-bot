from sqlalchemy import Column, Integer
from src.db.base import Base

class MuteEntry(Base):
    __tablename__ = "muted_users"

    user_id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, primary_key=True)
