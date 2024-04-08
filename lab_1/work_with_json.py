import json
import logging


def read_json_file(json_file_name) -> dict:
    """
    Читает JSON файл и возвращает словарь с его данными
    """
    try:
        data = {}
        with open(json_file_name, "r", encoding="utf-8") as JSON_file:
            data = json.load(JSON_file)

        return data
    except FileNotFoundError:
        logging.error(f"Неудача при открытии файла '{json_file_name}',"
                      f" в функции read_csv_frequency")
    except Exception as e:
        logging.error(f"Произошла ошибка {e} в функции read_json_file")
