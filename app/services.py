from fastapi import HTTPException
from sqlalchemy.orm import Session

from pyowm import OWM
import os
from dotenv import load_dotenv

from schemas.accessHistorySchemas import AccessHistoryCreate
from crud import get_city_by_id, create_api_access_history
from schemas.weatherInfomationSchema import WeatherInformation
from enums import RequestStatus

# load config files
load_dotenv()

# using the python open weather api sdk
# I can also invoke http calls manually
# but using sdk is better
# can also move this into a separate files, but this file is so small so i will keep this simple
class OpenWeatherClient:
    def __init__(self):
        api_key = os.getenv('OWM_API_KEY')
        self.owm = OWM(api_key)
        self.mgr = self.owm.weather_manager()

    def get_weather_by_city_name_external(self, city_name: str):
        try:
            observation = self.mgr.weather_at_place(city_name)
        # re-throw the error up
        # NOTE: in python and .net, to keep the original stack track, we need to use raise wihtout specifying any exceptions
        # this is very important for future troubleshooting as it will retain error information
        except:
            raise
        return observation



# methods exposed to controllers
def get_open_weather_client():
    return OpenWeatherClient()

def get_weather_by_city_id(db: Session, city_id: int, openWeatherClient: OpenWeatherClient) -> WeatherInformation:
    city_entity = get_city_by_id(db, city_id)
    if city_entity is None:
        raise HTTPException(status_code=404, detail="invalid city id")
    try:
        current_weather = openWeatherClient.get_weather_by_city_name_external(city_entity.name)
        current_weather_mapped = WeatherInformation(city_name=current_weather.location.name,
                                                    detailed_status=current_weather.weather.detailed_status, 
                                                    wind=current_weather.weather.wind(), 
                                                    humidity=current_weather.weather.humidity,
                                                    temperature=current_weather.weather.temperature("celsius"),
                                                    clouds=current_weather.weather.clouds)
        
    except Exception as e:
        # log the access history as failure
        accessHistory = AccessHistoryCreate(city_id=city_id, status=RequestStatus.Failure)
        create_api_access_history(db, accessHistory)
        
        # re-throw error up
        raise HTTPException(status_code=500, detail=e)

    # log the access history as success
    accessHistory = AccessHistoryCreate(city_id=city_id, status=RequestStatus.Success)
    create_api_access_history(db, accessHistory)

    return current_weather_mapped
