from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import select, Sequence
from sqlalchemy import Engine, create_engine
from src.constants import ToggleExitCode, CONNECTION_STRING

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "disable_tags"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(primary_key=True)


engine: Engine = create_engine(CONNECTION_STRING)
session_local = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

def get_no_disturb_users(chat_id: int) -> Sequence[User]:
    with session_local() as session:
        return session.scalars(select(User).where(User.chat_id.is_(chat_id))).all()

def toggle_no_disturb(user_id: int, chat_id: int) -> ToggleExitCode:
    exit_code = ToggleExitCode.ERROR
    with session_local() as session:
        user = session.get(User, (user_id, chat_id))
        if not user:
            session.add(User(user_id=user_id, chat_id=chat_id))
            exit_code = ToggleExitCode.TURNED_OFF
        elif user:
            session.delete(user)
            exit_code = ToggleExitCode.TURNED_ON
        session.commit()
    return exit_code