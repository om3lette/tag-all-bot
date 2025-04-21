from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parents[1]

DB_PATH: Path = BASE_DIR / "tag_all.db"
DATABASE_URL: str = f"sqlite:///{DB_PATH}"
