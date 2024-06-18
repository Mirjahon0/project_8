from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

ENGINE = create_engine('postgresql://postgres:mirjahon0706@localhost:5432/chairs', echo=True)
Base = declarative_base()
session = sessionmaker()