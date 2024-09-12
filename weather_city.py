
from my_package import *
from my_package.file_handling import read_from_csv, file_path
from my_package.requests_from_api import *

file_path_city  = '/Users/shalom_bergman/kodcode2/Data_engineering_course/Python/Air_Strike_Simulation_Project/air_strike_targets.csv'

citys_target =list(map(lambda target: target["City"],[i for i in read_from_csv(file_path_city)]))
#print(citys_target)

def return_list_json_file(citys_target):
    weather_data = []

    for city in citys_target:

        weather_data.append(xtract_weather_forecast_for_city(city, key_api))
    return weather_data

weather_data = return_list_json_file(citys_target)
# print(weather_data)
weather_data_n = []
for i in weather_data:
    temp = list(map(lambda x: x["list"], [i for i in weather_data]))[4][1]
    citise=  temp["weather"][0]["main"],temp["clouds"]["all"],temp["wind"]["speed"]
    weather_data_n.append(citise)

print(weather_data_n)

