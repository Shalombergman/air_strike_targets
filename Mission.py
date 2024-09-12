import weather_city
from utils import haversine_distance
from weather_city import weather_data

BASE_LAT = 31.79592425
BASE_LON = 35.211980759695
def weather_score(weather):
    if weather == "Clear":
        return 1.0
    elif weather == "Clouds":
        return 0.7
    elif weather == "Rain":
        return 0.4
    elif weather == "Stormy":
        return 0.2
    else:
        return 0

class Mission:
    def __init__(self, target, pilot, aircraft ,weather_data):
        self.target = target
        self.pilot = pilot
        self.aircraft = aircraft
        self.weather_data = weather_data


    def calculate_score(self):
        distance_score = self.calculate_distance_score()
        pilot_skill_score = self.pilot['skill_level'] * 0.25
        aircraft_fuel_score = self.aircraft['fuel_capacity'] * 0.25
        weather_condition_score = weather_score(list(map(lambda x: x["list"], [i for i in self.weather_data]))[4][1]["weather"][0]["main"])
        return distance_score + pilot_skill_score + aircraft_fuel_score + weather_condition_score

    def calculate_distance_score(self):
        return haversine_distance(BASE_LAT, BASE_LON,self.target['lat'], self.target['lon'],) * 0.2