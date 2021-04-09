from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

engine = create_engine('sqlite:///data.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
