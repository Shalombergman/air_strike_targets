
from my_package import *
from my_package.file_handling import read_from_csv, file_path
from my_package.requests_from_api import *

file_path_city  = '/Users/shalom_bergman/kodcode2/Data_engineering_course/Python/Air_Strike_Simulation_Project/air_strike_targets.csv'

citys_target =list(map(lambda target: target["City"],[i for i in read_from_csv(file_path_city)]))
print(citys_target)

def return_list_json_geographic_data(citys_target):
    geographic_data = []

    for city in citys_target:

        geographic_data.append(extraction_from_geographic_universe_of_a_city(city, key_api))
    return geographic_data

geographic_data = return_list_json_geographic_data(citys_target)
print(geographic_data)
