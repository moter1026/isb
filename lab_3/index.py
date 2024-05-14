import logging
import argparse

from crypto import Cryptography
from work_with_files import read_json_file

if __name__ == "__main__":
    logging.basicConfig(filename="message.log", filemode="a", level=logging.INFO)

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', action='store_true',
                       help='Запускает режим генерации ключей')
    group.add_argument('-enc', '--encryption', action='store_true',
                       help='Запускает режим шифрования')
    group.add_argument('-dec', '--decryption', action='store_true',
                       help='Запускает режим дешифрования')

    parser.add_argument("-paths", "--paths", type=str,
                        help='Ожидает путь до файла json, где указаны необходимые пути до файлов')
    parser.add_argument("-size_k", "--size_key", type=int,
                        help='Количество бит (кратное 8, не меньше 32 и не больше 442)')

    args = parser.parse_args()
    file_name = args.paths

    names_of_files = read_json_file(file_name)

    if args.generation:
        # генерируем ключи
        crypt = Cryptography(names_of_files["symmetric_key"],
                             names_of_files["public_key"],
                             names_of_files["private_key"])
        crypt.generate_keys(args.size_key)

    elif args.encryption:
        crypt = Cryptography(names_of_files["symmetric_key"],
                             names_of_files["public_key"],
                             names_of_files["private_key"])
        crypt.encrypt(names_of_files["initial_file"], names_of_files["encrypted_file"])

    elif args.decryption:
        crypt = Cryptography(names_of_files["symmetric_key"],
                             names_of_files["public_key"],
                             names_of_files["private_key"])
        crypt.decrypt(names_of_files["encrypted_file"], names_of_files["decrypted_file"])
    else:
        # дешифруем
        print()
