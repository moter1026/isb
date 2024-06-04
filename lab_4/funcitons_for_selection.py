import hashlib
import logging
import math
import multiprocessing as mp
import time

from typing import Any
from matplotlib import pyplot as plt


class Check_number_of_card:
    def __init__(self, hash: str, last_numbers: str, bins: list,
                 path_of_serialization: str = "./found number.txt",
                 total_numbers: int = 16) -> None:
        self.hash = hash
        self.last_numbers = last_numbers
        self.bins = bins
        self.path_of_serialization = path_of_serialization
        self.total_numbers = int(total_numbers)

        logging.basicConfig(filename="message.log", filemode="a", level=logging.INFO, encoding="utf-8")

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

    def find_number_of_card(self, cores: Any) -> Any:
        """
        Ищет номер карты по хэшу, БИН банка, последним цифрам карты

        :param cores: сколько ядер использовать
        :return: номер карты, если он найден в виде строки или False иначе
        """
        numbers = []
        for bin in self.bins:
            numbers.append(self.generate_number_of_card(bin))

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
        """
        Сериализует полученное значение в файл, переданный при создании объекта класса

        :param number: значение, которое необходимо сериализовать
        :return: None
        """
        try:
            with open(self.path_of_serialization, "w", encoding="utf-8") as write_file:
                write_file.write(number)
        except FileNotFoundError as e:
            logging.error(f"Ошибка сериализации. Файл не открылся.")
        except Exception as e:
            logging.error(f"Ошибка во время сериализации")

    def create_plot(self) -> None:
        """
        Строит график зависимости времени выполнения программы от количества использованных ядер процессора

        :return: None
        """
        try:
            count_cores = mp.cpu_count()
            range_cycle = range(1,  math.floor(1.5*count_cores))
            time_list = []
            cores_list = []
            for cores in range_cycle:
                start_time = time.time()
                self.find_number_of_card(cores)
                time_list.append(time.time() - start_time)
                cores_list.append(cores)

            plt.ylabel("time")
            plt.xlabel("cores")
            plt.plot(cores_list, time_list, color='navy', linestyle='--', marker='o', linewidth=1, markersize=4)
            plt.show()
        except Exception as e:
            logging.error(f"Ошибка при создании графика")

    @staticmethod
    def check_luna(sequence: str) -> bool:
        """
        Алгоритм Луна - это алгоритм вычисления контрольной цифры номера пластиковой карты
        в соответствии со стандартом ISO/IEC 7812.

        выявляет ошибки, вызванные непреднамеренным искажением данных
        :param sequence: последовательность, которую необходимо проверить
        :return: булевое значение
        """
        if len(sequence) <= 1:
            raise ValueError("Последовательность не может быть меньше 2 значений")
        control_sum = 0
        for i in range(-2, -len(sequence) - 1, -1):
            summand = int(sequence[i])
            if i % 2 == 0:
                summand = summand * 2
                if summand >= 10:
                    summand = summand // 10 + summand % 10
            control_sum += summand
        control_digit = (10 - ((control_sum % 10) % 10))
        return control_digit == int(sequence[-1])
