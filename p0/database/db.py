from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base


engine= create_engine('sqlite:///revhire.db', echo=True)
connection=engine.connect()

Session = sessionmaker(bind=engine,autocommit=False, autoflush=False)
# Create a base class for ORM models
Base = declarative_base()