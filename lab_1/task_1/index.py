from functions_for_task1 import (read_file_txt, encrypt_text,
                                 write_file, get_paths_from_json)

if __name__ == "__main__":
    text_start, key, text_end = get_paths_from_json()

    text = read_file_txt(text_start)
    key = read_file_txt(key)

    encrypt_text = encrypt_text(text, key)

    print(encrypt_text)

    write_file(text_end, encrypt_text)
