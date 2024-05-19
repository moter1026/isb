import logging
import argparse

from crypto import Cryptography
from work_with_files import read_json_file


def create_crypt_obj(names_dict: dict) -> Cryptography:
    return Cryptography(names_dict["symmetric_key"],
                        names_dict["public_key"],
                        names_dict["private_key"])


if __name__ == "__main__":
    logging.basicConfig(filename="message.log", filemode="a", level=logging.INFO)
    try:
        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-genall', '--generation_all', action='store_true',
                           help='Запускает режим генерации ключей')
        group.add_argument('-gensy', '--generation_symmetric', action='store_true',
                           help='Запускает режим генерации симметричного ключа. \n'
                                'Для успешного запуска необходим публичный ключ')
        group.add_argument('-genass', '--generation_asymmetric', action='store_true',
                           help='Запускает режим генерации асимметричных ключей')
        group.add_argument('-enc', '--encryption', action='store_true',
                           help='Запускает режим шифрования')
        group.add_argument('-dec', '--decryption', action='store_true',
                           help='Запускает режим дешифрования')

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
        if args.generation_all:
            # генерируем ключи
            crypt = create_crypt_obj(names_of_files)
            crypt.generate_keys(args.size_key)

        elif args.generation_symmetric and args.asymmetric_public_path:
            # генерируем симметричный ключ
            crypt = create_crypt_obj(names_of_files)
            crypt.generate_symmetric_key(args.size_key)

        elif args.generation_asymmetric:
            # генерируем ассиметричные ключи
            crypt = create_crypt_obj(names_of_files)
            crypt.generate_private_key()
            crypt.generate_public_key()

        elif args.encryption:
            crypt = create_crypt_obj(names_of_files)
            crypt.encrypt(names_of_files["initial_file"], names_of_files["encrypted_file"])

        elif args.decryption:
            crypt = create_crypt_obj(names_of_files)
            crypt.decrypt(names_of_files["encrypted_file"], names_of_files["decrypted_file"])
        else:
            # дешифруем
            print()

    except Exception as e:
        err_text = f"Error {e}"
        print(err_text)
        logging.error(err_text)
