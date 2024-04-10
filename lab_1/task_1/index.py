import consts
import logging

from functions_for_task1 import (read_file_txt, encrypt_text,
                                 write_file, get_paths_from_json)


def main() -> None:
    """
    Выполняет основной алгоритм программы
    """
    text_start, key, text_end = get_paths_from_json(consts.JSON_FILE)

    text = read_file_txt(text_start)
    key = read_file_txt(key)

    encrypt_main_text = encrypt_text(text, key, consts.ALPHABET)

    print(encrypt_main_text)

    write_file(text_end, encrypt_main_text)


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        logging.error(f"Программа завершилась неудачей с ошибкой {e}")
