import logging
import os

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key

import work_with_files

from asymetric_functions import asymmetric_actions, Mode
from symmetric_functions import symmetric_encrypt, symmetric_decrypt


class Cryptography:
    def __init__(self, symmetric_key: str, public_key: str, private_key: str) -> None:
        """
        Инициализирует класс Cryptography.

        :param symmetric_key (str): путь до файла, в котором будет записан симметричный ключ
        :param public_key (str): путь до файла, в котором будет записан асимметричный публичный ключ
        :param private_key (str): путь до файла, в котором будет записан асимметричный приватный ключ
        :return: None
        """
        self.symmetric_key = symmetric_key
        self.public_key = public_key
        self.private_key = private_key

    def generate_keys(self, size_of_key: int) -> None:
        """
        Метод генерирует симметричный, и два ассиметричных ключа, и записывает их в
        файлы, указанные при создании класса.
        Симметричный ключ перед записью в файл шифруется при помощи публичного ассиметричного ключа.

        :param size_of_key: Количество бит (кратное 8, не меньше 32 и не больше 442)
        :return:
        """
        if (size_of_key < 32 or size_of_key > 442) and size_of_key % 8 != 0:
            logging.exception("Неправильный параметр key_size")
        local_simmetric_key = os.urandom(size_of_key // 8)

        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        local_private_key = keys
        local_public_key = keys.public_key()

        work_with_files.write_file_in_bytes(
            self.symmetric_key,
            asymmetric_actions(
                local_simmetric_key, local_public_key, Mode.GENERATE))
        work_with_files.write_file_in_bytes(
            self.public_key,
            local_public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                          format=serialization.PublicFormat.SubjectPublicKeyInfo))
        work_with_files.write_file_in_bytes(
            self.private_key,
            local_private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PrivateFormat.TraditionalOpenSSL,
                                            encryption_algorithm=serialization.NoEncryption()))

    def encrypt(self, path_of_decrypt_text: str, path_of_encrypt_text) -> None:
        """
        Метод кодирует текст из входного файла в выходной

        :param path_of_decrypt_text: входной файл
        :param path_of_encrypt_text: выходной файл
        :return:
        """
        local_symmetric_key = work_with_files.read_file_in_bytes(self.symmetric_key)

        local_private_key = work_with_files.read_file_in_bytes(self.private_key)
        local_private_key = load_pem_private_key(local_private_key, password=None)

        # # Расшифровываем симметричный ключ, ассимметричным приветным ключом
        local_symmetric_key = asymmetric_actions(local_symmetric_key,
                                                 local_private_key,
                                                 Mode.DECRYPTION)

        text = work_with_files.read_file_in_bytes(path_of_decrypt_text)
        text = symmetric_encrypt(text, local_symmetric_key)

        work_with_files.write_file_in_bytes(path_of_encrypt_text, text)

    def decrypt(self, path_of_encrypt_text: str, path_of_decrypt_text: str) -> None:
        """
        Метод декодирует текст из входного файла в выходной

        :param path_of_encrypt_text: входной файл
        :param path_of_decrypt_text: выходной файл
        :return:
        """
        local_symmetric_key = work_with_files.read_file_in_bytes(self.symmetric_key)

        local_private_key = work_with_files.read_file_in_bytes(self.private_key)
        local_private_key = load_pem_private_key(local_private_key, password=None)

        # # Расшифровываем симметричный ключ, ассимметричным приветным ключом
        local_symmetric_key = asymmetric_actions(local_symmetric_key,
                                                 local_private_key,
                                                 Mode.DECRYPTION)

        text = work_with_files.read_file_in_bytes(path_of_encrypt_text)
        text = symmetric_decrypt(text, local_symmetric_key)
        work_with_files.write_file(path_of_decrypt_text, text)
