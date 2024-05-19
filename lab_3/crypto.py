import logging
import os

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key

import work_with_files

from asymmetric_functions import Asymmetric
from symmetric_functions import Symmetric


class Cryptography:
    def __init__(self, symmetric_key_path: str, public_key_path: str, private_key_path: str) -> None:
        """
        Инициализирует класс Cryptography.

        :param symmetric_key (str): путь до файла симметричного ключа
        :param public_key (str): путь до файла асимметричного публичного ключа
        :param private_key (str): путь до файла асимметричного приватного ключа
        :return: None
        """
        self.symmetric_key_path = symmetric_key_path
        self.public_key_path = public_key_path
        self.private_key_path = private_key_path

    def get_private_key(self) -> rsa.RSAPrivateKey:
        local_private_key = work_with_files.read_file_in_bytes(self.private_key_path)
        return load_pem_private_key(local_private_key, password=None)

    def get_public_key(self) -> rsa.RSAPublicKey:
        """
        Получает публичный ключ из приветного ключа, записанного в файле
        self.private_key_path
        :return: rsa.RSAPublicKey
        """
        local_private_key = self.get_private_key()
        return local_private_key.public_key()

    def generate_keys(self, size_of_key: int) -> None:
        """
        Метод генерирует симметричный, и два ассиметричных ключа, и записывает их в
        файлы, указанные при создании класса.
        Симметричный ключ перед записью в файл шифруется при помощи публичного ассиметричного ключа.

        :param size_of_key: Количество бит (кратное 8, не меньше 32 и не больше 442)
        :return:
        """
        self.generate_private_key()
        self.generate_public_key()
        self.generate_symmetric_key(size_of_key)

    def generate_private_key(self) -> rsa.RSAPrivateKey:
        """
        Генерирует приватный ключ асимметричного алгоритма
        и записывает в файл self.private_key_path
        """
        local_private_key = Asymmetric.generate_private_key()

        work_with_files.write_file_in_bytes(
            self.private_key_path,
            local_private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PrivateFormat.TraditionalOpenSSL,
                                            encryption_algorithm=serialization.NoEncryption()))
        return local_private_key

    def generate_public_key(self) -> rsa.RSAPublicKey:
        """
        Получает публичный ключ асимметричного алгоритма
        и записывает его в файл self.public_key_path
        """
        local_public_key = self.get_public_key()

        work_with_files.write_file_in_bytes(
            self.public_key_path,
            local_public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                          format=serialization.PublicFormat.SubjectPublicKeyInfo))
        return local_public_key

    def generate_symmetric_key(self, key_size: int) -> bytes:
        """Генерирует и записывает в файл симметричный ключ"""
        if (key_size < 32 or key_size > 442) and key_size % 8 != 0:
            err_text = "Неправильный параметр key_size"
            logging.exception(err_text)
            raise err_text

        local_simmetric_key = os.urandom(key_size // 8)

        public_key = self.get_public_key()
        symmetric_enc_key = Asymmetric.encryption(local_simmetric_key, public_key)

        work_with_files.write_file_in_bytes(
            self.symmetric_key_path, symmetric_enc_key)
        return symmetric_enc_key

    def encrypt(self, path_of_decrypt_text: str, path_of_encrypt_text) -> None:
        """
        Метод кодирует текст из входного файла в выходной

        :param path_of_decrypt_text: входной файл
        :param path_of_encrypt_text: выходной файл
        :return:
        """
        local_symmetric_key = work_with_files.read_file_in_bytes(self.symmetric_key_path)

        local_private_key = self.get_private_key()

        # Расшифровываем симметричный ключ, ассимметричным приватным ключом
        local_symmetric_key = Asymmetric.decryption(local_symmetric_key,
                                                    local_private_key)

        text = work_with_files.read_file_in_bytes(path_of_decrypt_text)
        text = Symmetric.symmetric_encrypt(text, local_symmetric_key)

        work_with_files.write_file_in_bytes(path_of_encrypt_text, text)

    def decrypt(self, path_of_encrypt_text: str, path_of_decrypt_text: str) -> None:
        """
        Метод декодирует текст из входного файла в выходной

        :param path_of_encrypt_text: входной файл
        :param path_of_decrypt_text: выходной файл
        :return:
        """
        local_symmetric_key = work_with_files.read_file_in_bytes(self.symmetric_key_path)

        local_private_key = self.get_private_key()

        # Расшифровываем симметричный ключ, ассимметричным приватным ключом
        local_symmetric_key = Asymmetric.decryption(local_symmetric_key,
                                                    local_private_key)

        text = work_with_files.read_file_in_bytes(path_of_encrypt_text)
        text = Symmetric.symmetric_decrypt(text, local_symmetric_key)
        work_with_files.write_file(path_of_decrypt_text, text)
