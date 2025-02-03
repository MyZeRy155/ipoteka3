from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv(dotenv_path="config.env")
db_url = os.getenv('DATABASE_URL')

def get_db_engine():
    db_engine = create_engine(db_url, echo=True)
    return db_engine

data_base_engine = get_db_engine()
def get_session():
    session = sessionmaker(bind=data_base_engine)()
    return session
