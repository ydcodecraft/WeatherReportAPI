from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from database import Base
from enums import RequestStatus

class AccessHistory(Base):
    __tablename__ = "access_histories"

    id = Column(Integer, primary_key=True)
    
    # can also take the timestamp from front end/ generate it from the backend app
    # generating in the database creates consistency across time zone
    # generating it in the backend creates better portability, they each have their pros and cons
    timestamp = Column(DateTime(timezone=True), default=func.now(), server_default=func.now())
    city_id = Column(Integer, ForeignKey("cities.id"))
    
    # used enum to lock values down, can also use string for more flexbility but I personall likes enum to enforce data integrity
    status = Column(Enum(RequestStatus), nullable=False)
    