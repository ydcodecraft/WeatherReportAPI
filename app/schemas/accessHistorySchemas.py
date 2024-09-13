from pydantic import BaseModel
from datetime import datetime
from enums import RequestStatus

class AccessHistoryBase(BaseModel):
    city_id: int
    status: RequestStatus

class AccessHistoryCreate(AccessHistoryBase):
    pass


class AccessHistory(AccessHistoryBase):
    id: int
    timestamp: datetime

    class Config:
        form_attributes = True
        # arbitrary_types_allowed = True
