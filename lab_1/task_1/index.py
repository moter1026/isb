import consts
import work_with_json

from functions_for_task1 import read_file_txt, encrypt_text, write_file


if __name__ == "__main__":
    FILES = work_with_json.read_json_file(consts.JSON_FILE)
    
    text = read_file_txt(FILES["text_start"])
    key = read_file_txt(FILES["key"])

    encrypt_text = encrypt_text(text, key)

    print(encrypt_text)

    write_file(FILES["text_end"], encrypt_text)



