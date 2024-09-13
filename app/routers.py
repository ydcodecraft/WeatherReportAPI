# I only created a single file for routers becasue there are not many endpoints
# in a larger project, I would create a folder for routers
# each router files would contain a specific business domain

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services import OpenWeatherClient, get_open_weather_client, get_weather_by_city_id
from schemas.weatherInfomationSchema import WeatherInformation
from schemas.accessHistorySchemas import AccessHistory
from crud import get_recent_successful_api_access_history

router = APIRouter(
    prefix="/weather",
    tags=["weather"]
)

@router.get("/{city_id}", response_model=WeatherInformation)
def get_weather(city_id: int, db: Session = Depends(get_db), openWeatherClient: OpenWeatherClient = Depends(get_open_weather_client)):
    try:
        weather_result = get_weather_by_city_id(db, city_id, openWeatherClient)
    except:
        # controller pass through exceptions from service
        # i can also put some exception handling in controller instead, both works and it's a matter of preferences
        raise
    return weather_result


# sementically, i can split this endpoint into its own loggin endpoint
# we only have 2 endpoints and it exists for weather, so i left it alone
@router.get("/history/", response_model=list[AccessHistory])
# added an additonal parameter skip for future pagination need, not in the requiremetns but it's easy to make these in fastapi
def get_recent_success_requests(db: Session = Depends(get_db), limit: int = 5, skip: int = 0):
    return get_recent_successful_api_access_history(db, limit)
