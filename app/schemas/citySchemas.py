from pydantic import BaseModel

class CityBase(BaseModel):
    name: str

class CityCreate(CityBase):
    pass

class City(CityBase):
    id: int

    class Config:
        form_attributes = True