from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_db_engine():
    db_engine = create_engine('sqlite:///database.db', echo=True)
    return db_engine

data_base_engine = get_db_engine()
def get_session():
    session = sessionmaker(bind=data_base_engine)()
    return session
