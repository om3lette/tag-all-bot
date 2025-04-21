from src.db import create_db_metadata
from src.client import client
import src.commands # Used to register the commands. Do not remove

if __name__ == "__main__":
    create_db_metadata()

    client.start()
    client.run_until_disconnected()
