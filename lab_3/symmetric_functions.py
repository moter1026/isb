import logging
import os

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

logging.basicConfig(filename="message.log", filemode="a", level=logging.INFO)


def symmetric_encrypt(text: bytes, key: bytes) -> bytes:
    """
    Функция шифрует данные из переменной text при помощи ключа key

    :param text: данные для шифрования
    :param key: ключ для шифрования
    :return: bytes
    """
    padder = padding.ANSIX923(64).padder()
    padded_text = padder.update(text) + padder.finalize()
    iv = os.urandom(8)
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    c_text = iv + encryptor.update(padded_text) + encryptor.finalize()
    return c_text


def symmetric_decrypt(c_text: bytes, key: bytes) -> str:
    """
    Функция дешифрует данные из переменной text при помощи ключа key

    :param c_text: данные для дешифрования
    :param key: ключ для дешифрования
    :return: bytes
    """
    iv = c_text[:8]
    c_text = c_text[8:]
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))

    decrypt = cipher.decryptor()
    dc_text = decrypt.update(c_text) + decrypt.finalize()

    unpadder_obj = padding.ANSIX923(64).unpadder()
    unpadded_dc_text = unpadder_obj.update(dc_text) + unpadder_obj.finalize()

    return unpadded_dc_text.decode('UTF-8')
