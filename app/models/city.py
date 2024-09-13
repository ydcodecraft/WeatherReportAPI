from sqlalchemy import Column, Integer, String
from database import Base

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)

    # index the name of the column becasue city names are going to be unique, this can increase retrieval speed
    name = Column(String, unique=True, index=True) 