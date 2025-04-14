from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class DatabaseInit:
    def __init__(self):
        self.engine = create_engine('sqlite:///nutrition.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)