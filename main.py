# from my_package.requests_from_api import xtract_weather_forecast_for_city, key_api, \
#     extraction_from_geographic_universe_of_a_city
# from my_package.file_handling import read_from_json, read_from_csv, export_results_to_csv
# from Mission import Mission, weather_score
# from geographical_location import return_list_json_geographic_data, citys_target
# from weather_city import return_list_json_file, weather_data_n
#
# targets = read_from_csv('/Users/shalom_bergman/kodcode2/Data_engineering_course/Python/Air_Strike_Simulation_Project/air_strike_targets.csv')
# pilots = read_from_json('/Users/shalom_bergman/kodcode2/Data_engineering_course/Python/Air_Strike_Simulation_Project/JSON/pilots.json')
# aircrafts = read_from_json('/Users/shalom_bergman/kodcode2/Data_engineering_course/Python/Air_Strike_Simulation_Project/JSON/aircrafs.json')
#
#
#
# results = []
# weather_data = weather_data_n
# for target in targets:
#     if 'lat' not in target or 'lon' not in target:
#         geo_data = extraction_from_geographic_universe_of_a_city(target["City"],key_api)
#         target['lat'] = geo_data[0]['lat']
#         target['lon'] = geo_data[0]['lon']
#     for pilot in pilots:
#         for aircraft in aircrafts:
#             mission = Mission(target, pilot, aircraft, weather_data)
#             score = mission.calculate_score()
#             print(f"Mission Score for target {target['City']}: {score}")
#             results.append({
#                 'Target City': target["City"],
#                 'Pilot Name': pilot["name"],
#                 'Aircraft Type': aircraft["type"],
#                 'Mission Score': score,
#                 'Weather Condition': weather_score(list(map(lambda x: x["list"], [i for i in weather_data]))[4][1]["weather"][0]["main"])
#             })
#     #
# export_results_to_csv(results)

from my_package.requests_from_api import xtract_weather_forecast_for_city, key_api, extraction_from_geographic_universe_of_a_city
from my_package.file_handling import read_from_json, read_from_csv, export_results_to_csv
from Mission import Mission, weather_score
from geographical_location import return_list_json_geographic_data, citys_target
from weather_city import return_list_json_file

targets = read_from_csv('/Users/shalom_bergman/kodcode2/Data_engineering_course/Python/Air_Strike_Simulation_Project/air_strike_targets.csv')
pilots = read_from_json('/Users/shalom_bergman/kodcode2/Data_engineering_course/Python/Air_Strike_Simulation_Project/JSON/pilots.json')
aircrafts = read_from_json('/Users/shalom_bergman/kodcode2/Data_engineering_course/Python/Air_Strike_Simulation_Project/JSON/aircrafs.json')


results = []

for target in targets:
    if 'lat' not in target or 'lon' not in target:
        geo_data = extraction_from_geographic_universe_of_a_city(target["City"], key_api)
        target['lat'] = geo_data[0]['lat']
        target['lon'] = geo_data[0]['lon']
    weather_data = xtract_weather_forecast_for_city(target["City"], key_api)
    for pilot in pilots:
        for aircraft in aircrafts:
            mission = Mission(target, pilot, aircraft, weather_data)
            score = mission.calculate_score()
            print(f"Mission Score for target {target['City']}: {score}")

            results.append({
                'Target City': target["City"],
                'Pilot Name': pilot["name"],
                'Pilot Skill': pilot["skill_level"],
                'Aircraft Type': aircraft["type"],
                'Aircraft Speed(km/h)': aircraft["speed"],
                'Fuel Capacity (km)': aircraft["fuel_capacity"],
                'Mission Score': score,
                'Mission Fit Score': score,
                'Weather Condition': weather_data["list"][0]["weather"][0]["main"]
            })

def filter_results_by_city(results):

    filtered_results = {}

    for result in results:
        city = result['Target City']
        if city not in filtered_results:
            filtered_results[city] = result
        else:
            if result['Mission Score'] > filtered_results[city]['Mission Score']:
                filtered_results[city] = result

    return list(filtered_results.values())



filtered_results = filter_results_by_city(results)
export_results_to_csv(filtered_results)