import json
from typing import Any


def read_json_file(json_file_name) -> Any:
    """
    Читает json файл, обычно возвращая словарь с данными

    :param json_file_name: путь к файлу
    :return: Any
    """
    with open(json_file_name, "r", encoding="utf-8") as JSON_file:
        data = json.load(JSON_file)
        return data


def write_json_file(data: dict, json_file_name: str = "data_for_selection_card.json") -> None:
    """
    Записывает данные из словаря в json файл

    :param data: словарь с данными
    :param json_file_name: путь к файлу
    :return: None
    """
    with open(json_file_name, "w", encoding="utf-8") as write_file:
        json.dump(data, write_file)