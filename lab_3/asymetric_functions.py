import enum
import logging

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

logging.basicConfig(filename="message.log", filemode="a", level=logging.INFO)


class Mode(enum.Enum):
    """
    Класс, позволяющий выбрать необходимое действие при работе с
    ассиметричным алгоритмом
    """
    GENERATE = 0
    ENCRYPTION = 1
    DECRYPTION = 2


def asymmetric_actions(text: bytes, key: rsa.RSAPublicKey or rsa.RSAPrivateKey, mode: Mode) -> bytes:
    """
    Функция, генерирующая, декодирующая, кодирующа на основе публичного ключа
    ассиметричного алгоритма и переданного текста.

    :param text: байтовая информация, на основе которой будут происходить действия
    :param key: публичный ключ RSA, необходимый для генерации, декодирования, кодирования
    :param mode: вариация класса Mode для выбора действий

    :return bytes:
    """
    try:
        match mode:
            case Mode.ENCRYPTION:

                return key.encrypt(text,
                                   padding.OAEP(
                                       mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                       algorithm=hashes.SHA256(),
                                       label=None))

            case Mode.DECRYPTION:

                return key.decrypt(text,
                                   padding.OAEP(
                                       mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                       algorithm=hashes.SHA256(),
                                       label=None))

            case Mode.GENERATE:

                return key.encrypt(text,
                                   padding.OAEP(
                                       mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                       algorithm=hashes.SHA256(),
                                       label=None))

            case _:
                logging.info("Несуществующая вариация класса Mode")

    except Exception as e:
        logging.info(f"Ошибка {e} в функции asymmetric_actions")
