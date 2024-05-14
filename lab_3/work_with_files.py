import json
import logging

logging.basicConfig(filename="message.log", filemode="a", level=logging.INFO)


def read_json_file(json_file_name) -> dict:
    """
    Читает JSON файл и возвращает словарь с его данными
    """
    try:
        with open(json_file_name, "r", encoding="utf-8") as JSON_file:
            json_data = json.load(JSON_file)

        return json_data

    except FileNotFoundError:
        logging.error(f"Неудача при открытии файла '{json_file_name}',"
                      f" в функции read_json_file")
    except Exception as e:
        logging.error(f"Произошла ошибка {e} в функции read_json_file")


def read_file_in_bytes(path: str) -> bytes:
    """
    Читает файл по пути path

    Возвращает данные из файла в виде строки
    """
    try:
        with open(path, "rb") as f:
            text = f.read()
        logging.info("read_file")

        return text

    except FileNotFoundError:
        logging.error(f"Неудача при открытии файла '{path}',"
                      f" в функции read_file_in_bytes")
    except Exception as e:
        logging.error(f"Произошла ошибка {e} в функции read_file_in_bytes")


def read_file(path: str) -> str:
    """
    Читает файл по пути path

    Возвращает данные из файла в виде строки
    """
    try:
        with open(path, "r", encoding='utf-8') as f:
            text = f.read()
        logging.info("read_file")

        return text

    except FileNotFoundError:
        logging.error(f"Неудача при открытии файла '{path}',"
                      f" в функции read_file")
    except Exception as e:
        logging.error(f"Произошла ошибка {e} в функции read_file")


def write_file_in_bytes(path: str, data: bytes) -> None:
    """
    Записывает данные data в байтах в файл по пути path
    """
    try:
        with open(path, "wb") as f:
            f.write(data)

    except FileNotFoundError:
        logging.error(f"Неудача при открытии файла '{path}',"
                      f" в функции write_file_in_bytes")
    except Exception as e:
        logging.error(f"Произошла ошибка {e} в функции write_file_in_bytes")


def write_file(path: str, data: str) -> None:
    """
    Записывает данные data в файл по пути path
    """
    try:
        with open(path, "w", encoding='utf-8') as f:
            f.write(data)

    except FileNotFoundError:
        logging.error(f"Неудача при открытии файла '{path}',"
                      f" в функции write_file")
    except Exception as e:
        logging.error(f"Произошла ошибка {e} в функции write_file")
