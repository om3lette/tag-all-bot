from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.constants import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
