import json
from typing import Any


def read_json_file(json_file_name) -> list[Any]:
    data = {}
    with open(json_file_name, "r", encoding="utf-8") as JSON_file:
        data = json.load(JSON_file)

        text_start = data["text_start"]
        key = data["key"]
        text_end = data["text_end"]

        return [text_start, key, text_end]
