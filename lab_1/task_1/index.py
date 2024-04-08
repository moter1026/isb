import consts
import os
import sys
sys.path.insert(0, os.path.abspath('../'))
import work_with_json

from functions_for_task1 import (read_file_txt, encrypt_text,
                                 write_file)

if __name__ == "__main__":
    text_start, key, text_end = work_with_json.read_json_file(consts.JSON_FILE)

    text = read_file_txt(text_start)
    key = read_file_txt(key)

    encrypt_text = encrypt_text(text, key)

    print(encrypt_text)

    write_file(text_end, encrypt_text)
