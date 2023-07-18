import json
import csv
import os

def read_file(name_filter: str):
    marged_data = {}
    csv_file = []
    json_file = []
    for file in os.listdir("SKU"):
        if file.endswith(".json"):
            json_file.append(file)
        elif file.endswith(".csv"):
            csv_file.append(file)
    for files in csv_file:
        file_path = os.path.join("SKU", files)
        with open(file_path, newline='') as c_file:
            reader = csv.DictReader(c_file)
            for row in reader:
                key = row[name_filter]
                if key in marged_data:
                    marged_data[key].append(row)
                else:
                    marged_data[key] = [row]
    for j_file in json_file:
        j_file_path = os.path.join("SKU", j_file)
        with open(j_file_path) as js_file:
            json_data = json.load(js_file)
            for item in json_data["data"]:
                key = item[name_filter]
                if key in marged_data:
                    marged_data[key].append(item)
                else:
                    marged_data[key] = [item]
    return marged_data
