import json
import csv
file_path = ''
def read_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    return json_data



def read_from_csv(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
        return data


def export_results_to_csv(results, filename='missions_results.csv'):

    fieldnames = [
        'Target City', 'Pilot Name', 'Pilot Skill', 'Aircraft Type',
        'Aircraft Speed(km/h)', 'Fuel Capacity (km)',
        'Mission Score', 'Mission Fit Score', 'Weather Condition'
    ]
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for result in results:
            writer.writerow(result)