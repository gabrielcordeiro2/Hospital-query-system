from os import environ
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

Base = declarative_base()

app_config = {
    "URI": environ.get("DATABASE_URI"),
    "API_PORT": environ.get("API_PORT", 5000),
    "API_HOST": environ.get("API_HOST", 'localhost')   
}

class DBConnection:
    """ Manage all connections in database """

    def __init__(self):
        self.__get_URI = app_config["URI"]

    def create_engine(self):
        engine = create_engine(self.__get_URI)
        return engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.create_engine())
        self.session = session_make()
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        print("exit")

def create_db():
    database = Base.metadata.create_all(DBConnection().create_engine())
    return database
    