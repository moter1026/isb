import hashlib
import itertools
import logging
from typing import Any
import matplotlib
import multiprocessing as mp


class Check_cumber_of_card:
    def __init__(self, hash: str, last_numbers: str, bins: list,
                 path_of_serialization: str = "./found number.txt",
                 total_numbers: int = 16) -> None:
        self.hash = hash
        self.last_numbers = last_numbers
        self.bins = bins
        self.path_of_serialization = path_of_serialization
        self.total_numbers = total_numbers

        logging.basicConfig(filename="message.log", filemode="a", level=logging.INFO)

    @staticmethod
    def calculate_hash_sha384(number_of_card: str) -> str:
        """
        Вычисляет значение хэша по алгоритму sha384

        :param number_of_card: значение хэша
        :return: string
        """
        return hashlib.sha384(number_of_card.encode()).hexdigest()

    def generate_number_of_card(self, bin: str) -> list:
        """
        генерирует номер карты, подставляя в начало и в конец значения bin и last_numbers

        :param bin: Бин карты банка
        :return: сгенерированный номер карты
        """
        len_bin = len(bin)
        len_last = len(self.last_numbers)
        generate_numbers = self.total_numbers - len_last - len_bin
        range_for_generate = range(0, 10 ** (generate_numbers + 1))

        result = []
        for number in range_for_generate:
            result.append(f"{bin}{str(number).zfill(generate_numbers)}{self.last_numbers}")

        return result

    def check_numbers_sha384(self, our_card_number: str) -> Any:
        """
        Сравнивает хэш значения номеров карт

        :param our_card_number: номер карты, хэш которой необходимо сравнить
        :return: номер карты, если хэши совпали, иначе False
        """
        our_hash = self.calculate_hash_sha384(our_card_number)
        if our_hash == self.hash:
            res = our_card_number
        else:
            res = False
        return res

    def find_number_of_card(self) -> Any:
        """
        Ищет номер карты по хэшу, БИН банка, последним цифрам карты

        :return: номер карты, если он найден в виде строки или False иначе
        """
        numbers = []
        for bin in self.bins:
            numbers.append(self.generate_number_of_card(bin))

        cores = mp.cpu_count()
        try:
            with mp.Pool(processes=cores) as proc:
                for number in numbers:
                    for res in proc.map(self.check_numbers_sha384, number):
                        if res:
                            return res
            return False

        except Exception as e:
            logging.info(f"Ошибка в многопоточном режиме")

    def serialization_number(self, number: str) -> None:
        try:
            with open(self.path_of_serialization, "w", encoding="utf-8") as write_file:
                write_file.write(number)
        except FileNotFoundError as e:
            logging.info(f"Ошибка сериализации. Файл не открылся.")
        except Exception as e:
            logging.info(f"Ошибка во время сериализации")
