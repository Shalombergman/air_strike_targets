from datetime import datetime

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

    from datetime import datetime

    def calculate_score(self):
        distance_score = self.calculate_distance_score()
        pilot_skill_score = self.pilot['skill_level'] * 0.25
        aircraft_fuel_score = self.aircraft['fuel_capacity'] * 0.25

        target_time_str = "2024-09-14 00:00:00"
        target_time = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M:%S")

        closest_forecast = None
        min_time_diff = None

        for forecast in self.weather_data["list"]:
            forecast_time = datetime.strptime(forecast["dt_txt"], "%Y-%m-%d %H:%M:%S")
            time_diff = abs((forecast_time - target_time).total_seconds())

            if min_time_diff is None or time_diff < min_time_diff:
                min_time_diff = time_diff
                closest_forecast = forecast

        if closest_forecast is None:
            raise ValueError(f"Weather data for {target_time_str} not found")

        weather_condition = closest_forecast["weather"][0]["main"]
        weather_condition_score = weather_score(weather_condition)

        return distance_score + pilot_skill_score + aircraft_fuel_score + weather_condition_score

    def calculate_distance_score(self):
        return haversine_distance(BASE_LAT, BASE_LON,self.target['lat'], self.target['lon']) * 0.2