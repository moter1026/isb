import json

def readJSONFile(json_file_name) -> dict:
    data = {}
    with open(json_file_name, "r", encoding="utf-8") as JSON_file:
        data = json.load(JSON_file)
    return data