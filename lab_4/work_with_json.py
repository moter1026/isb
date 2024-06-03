import json
from typing import Any


def read_json_file(json_file_name) -> Any:
    with open(json_file_name, "r", encoding="utf-8") as JSON_file:
        data = json.load(JSON_file)
        return data
