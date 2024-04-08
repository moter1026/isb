import json
from typing import Any


def read_json_file(json_file_name) -> list[Any]:
    data = {}
    with open(json_file_name, "r", encoding="utf-8") as JSON_file:
        data = json.load(JSON_file)

        frequency_ru = data["frequency_ru"]
        encrypt_text = data["encrypt_text"]
        frequency_for_encrypt_text = data["frequency_for_encrypt_text"]
        ready_frequency = data["ready_frequency"]
        ready_text = data["ready_text"]

        return [frequency_ru, encrypt_text, frequency_for_encrypt_text, ready_frequency, ready_text]
