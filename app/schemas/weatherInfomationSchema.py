from pydantic import BaseModel

class WeatherInformation(BaseModel):
    city_name: str
    detailed_status: str

    # {'speed': 4.6, 'deg': 330}
    wind: dict

    # 87
    humidity: int
    
    # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}           
    temperature: dict

    # 75
    clouds: int