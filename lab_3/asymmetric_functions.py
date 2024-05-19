import enum
import logging

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

logging.basicConfig(filename="message.log", filemode="a", level=logging.INFO)


class Asymmetric:
    @staticmethod
    def encryption(text: bytes, key: rsa.RSAPublicKey) -> bytes:
        """
        Функция кодирующая на основе публичного ключа
        ассиметричного алгоритма и переданного текста.

        :param text: байтовая информация, на основе которой будут происходить действия
        :param key: публичный ключ RSA, необходимый для генерации, декодирования, кодирования
        :return bytes:
        """
        try:
            return key.encrypt(text,
                               padding.OAEP(
                                   mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                   algorithm=hashes.SHA256(),
                                   label=None))
        except Exception as e:
            logging.info(f"Ошибка {e} в функции encryption")

    @staticmethod
    def decryption(text: bytes, key: rsa.RSAPrivateKey) -> bytes:
        """
        Функция декодирующая на основе приветного ключа
        ассиметричного алгоритма и переданного текста.

        :param text:
        :param key:
        :return: bytes
        """
        try:
            return key.decrypt(text,
                               padding.OAEP(
                                   mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                   algorithm=hashes.SHA256(),
                                   label=None))
        except Exception as e:
            logging.info(f"Ошибка {e} в функции decryption")

    @staticmethod
    def generate_private_key() -> rsa.RSAPrivateKey:
        return rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
