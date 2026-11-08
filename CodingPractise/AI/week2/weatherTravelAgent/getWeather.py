import os
import requests
from dotenv import load_dotenv
load_dotenv()

def getWeather(city):
    #https://api.weatherapi.com/v1/forecast.json?key=e4927524411f47f68af190057260811&q=Bengaluru&days=3&aqi=no&alerts=no
    weatherAPIKey=os.getenv("Weather_API_Key")
    if not weatherAPIKey:
        raise ValueError("No API Key Available to call weather API")
    weatherURL=os.getenv("Weather_URL")
    if not weatherURL:
        raise ValueError("No API Url Available")
    params={
        "key":weatherAPIKey,
        "q":city,
        "days":3,
        "aqi":"no",
        "alerts":"no"
    }
    response=requests.get(weatherURL,params=params,timeout=15)
    return response
