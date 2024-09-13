# I only created a single file for crud methods becasue there are not many functions required
# in a larger project, I would create a folder for cruds
# each crud files would contain a set of cruds for a specific table

from sqlalchemy.orm import Session
from models import AccessHistory, City
from schemas import accessHistorySchemas, citySchemas
from enums import RequestStatus

def get_city_by_id(db: Session, city_id: int):
    return db.query(City).filter(City.id == city_id).first()


def create_api_access_history(db: Session, accessHistory: accessHistorySchemas.AccessHistoryCreate):
    db_entry = AccessHistory(city_id=accessHistory.city_id, status=accessHistory.status)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry
    

# default the limit to 5, but put it as an optional parameter in case there is future reuiqrement change
def get_recent_successful_api_access_history(db: Session, limit: int = 5):
    return db.query(AccessHistory).filter(AccessHistory.status == RequestStatus.Success).order_by(AccessHistory.timestamp.desc()).limit(limit).all()