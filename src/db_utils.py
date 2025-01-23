from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_db_engine():
    engine = create_engine('sqlite:///database.db', echo=True)
    return engine
engine = get_db_engine()

def get_session():
    session = sessionmaker(bind=engine)()
    return session
