import logging
import argparse
from enum import Enum

from crypto import Cryptography
from work_with_files import read_json_file


def create_crypt_obj(names_dict: dict) -> Cryptography:
    return Cryptography(names_dict["symmetric_key"],
                        names_dict["public_key"],
                        names_dict["private_key"])


class Option(Enum):
    GENERATE_ALL_KEY = 0
    GENERATE_SYMMETRIC_KEY = 1
    GENERATE_ASYMMETRIC_KEYS = 2
    ENCRYPT = 3
    DECRYPT = 4


if __name__ == "__main__":
    logging.basicConfig(filename="message.log", filemode="a", level=logging.INFO)
    try:
        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-opt', '--options', type=int,
                           help='0 - Запускает режим генерации всех ключей'
                                '1 - Запускает режим генерации симметричного ключа. \n'
                                '\tДля успешного запуска необходим публичный ключ'
                                '2 - Запускает режим генерации асимметричных ключей'
                                '3 - Запускает режим шифрования'
                                '4 - Запускает режим дешифрования')

        # Аргументы, получающие пути сохранения файлов
        parser.add_argument("-pj", "--paths_json", type=str,
                            help='Ожидает путь до файла json, где указаны необходимые пути до файлов')
        parser.add_argument("-smp", "--symmetric_path", type=str,
                            help='Ожидает путь до файла симметричного ключа')
        parser.add_argument("-aspr", "--asymmetric_private_path", type=str,
                            help='Ожидает путь до файла асимметричного приватного ключа')
        parser.add_argument("-aspu", "--asymmetric_public_path", type=str,
                            help='Ожидает путь до файла асимметричного публичного ключа')
        parser.add_argument("-in", "--initial_path", type=str,
                            help='Ожидает путь до файла с исходным текстом')
        parser.add_argument("-encp", "--encrypted_path", type=str,
                            help='Ожидает путь до файла с зашифрованным текстом')
        parser.add_argument("-decp", "--decrypted_path", type=str,
                            help='Ожидает путь до файла с расшифрованным текстом')

        parser.add_argument("-sk", "--size_key", type=int,
                            help='Количество бит (кратное 8, не меньше 32 и не больше 442)')

        args = parser.parse_args()
        names_of_files = {}
        # Если был передан json файл, то берём данные из него, иначе берём из аргументов
        if args.paths_json:
            file_name = args.paths_json
            names_of_files = read_json_file(file_name)
        else:
            names_of_files["symmetric_key"] = args.symmetric_path if args.symmetric_path else None
            names_of_files["public_key"] = args.asymmetric_public_path if args.asymmetric_public_path else None
            names_of_files["private_key"] = args.asymmetric_private_path if args.asymmetric_private_path else None
            names_of_files["initial_file"] = args.initial_path if args.initial_path else None
            names_of_files["encrypted_file"] = args.encrypted_path if args.encrypted_path else None
            names_of_files["decrypted_file"] = args.decrypted_path if args.decrypted_path else None

        # В зависимости от аргументов при запуске, выполняем разные действия
        match args.options:
            case Option.GENERATE_ALL_KEY.value:
                if not (names_of_files["symmetric_key"] and
                        names_of_files["public_key"] and
                        names_of_files["private_key"]):
                    raise "Не переданы все необходимые пути"

                # генерируем ключи
                crypt = create_crypt_obj(names_of_files)
                crypt.generate_keys(args.size_key)

            case Option.GENERATE_SYMMETRIC_KEY.value:
                if not names_of_files["public_key"]:
                    raise "Не переданы все необходимые пути"

                # генерируем симметричный ключ
                crypt = create_crypt_obj(names_of_files)
                crypt.generate_symmetric_key(args.size_key)

            case Option.GENERATE_ASYMMETRIC_KEYS.value:
                if not (names_of_files["private_key"] and
                        names_of_files["public_key"]):
                    raise "Не переданы все необходимые пути"

                # генерируем ассиметричные ключи
                crypt = create_crypt_obj(names_of_files)
                crypt.generate_private_key()
                crypt.generate_public_key()

            case Option.ENCRYPT.value:
                if not (names_of_files["symmetric_key"] and
                        names_of_files["private_key"] and
                        names_of_files["initial_file"] and
                        names_of_files["encrypted_file"]):
                    raise "Не переданы все необходимые пути"

                crypt = create_crypt_obj(names_of_files)
                crypt.encrypt(names_of_files["initial_file"], names_of_files["encrypted_file"])

            case Option.DECRYPT.value:
                if not (names_of_files["symmetric_key"] and
                        names_of_files["private_key"] and
                        names_of_files["decrypted_file"] and
                        names_of_files["encrypted_file"]):
                    raise "Не переданы все необходимые пути"

                crypt = create_crypt_obj(names_of_files)
                crypt.decrypt(names_of_files["encrypted_file"], names_of_files["decrypted_file"])

    except Exception as e:
        err_text = f"Error {e}"
        print(err_text)
        logging.error(err_text)
