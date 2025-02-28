from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / "config.env"
load_dotenv(dotenv_path=env_path)

db_url = os.getenv('DATABASE_URL')

# Добавляем проверку
if not db_url:
    raise ValueError("DATABASE_URL not found in .env file")

def get_db_engine():
    db_engine = create_engine(db_url, echo=True)
    return db_engine

data_base_engine = get_db_engine()
def get_session():
    session = sessionmaker(bind=data_base_engine)()
    return session
