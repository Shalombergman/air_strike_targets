import requests

key_api = "3fd517e0d82e0acf437c2a0bd04b378c"
city = ""

def extraction_from_geographic_universe_of_a_city(city, key_api):
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key_api}"
    response = requests.get(url)
    return response.json()


def xtract_weather_forecast_for_city(city,key_api):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key_api}"
    response = requests.get(url)
    return response.json()
#https://api.openweathermap.org/data/2.5/forecast?q=yemen&appid=3fd517e0d82e0acf437c2a0bd04b378c