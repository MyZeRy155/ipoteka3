from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_db_engine(db_url: str):
    db_engine = create_engine(db_url, echo=True)
    return db_engine

def get_session(db_url: str):
    engine = create_engine(db_url, echo=True, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal
