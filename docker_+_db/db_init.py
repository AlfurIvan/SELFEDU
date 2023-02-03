from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connection_url = 'postgresql+psycopg2://postgres:password@db:5432/db'

engine = create_engine(connection_url)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def db_init():
    import models
    Base.metadata.create_all(bind=engine)
