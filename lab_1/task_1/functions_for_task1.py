import logging
import consts
import work_with_json


logging.basicConfig(filename = consts.NAME_LOG_FILE, level = logging.DEBUG,\
                    format = '%(asctime)s - %(levelname)s - %(message)s', encoding = "utf-8")


FILES = work_with_json.read_json_file(consts.JSON_FILE)


def read_file_txt(file_name: str) -> str:
    """Читает файл"""
    text = ""
    try:
        with open(file_name, "r", encoding="utf-8") as file_txt:
            text = file_txt.read()
        logging.info(f"Чтение файла '{file_name}' прошло успешно")
        return text

    except FileNotFoundError:
        logging.error(f"Не удалось открыть {file_name} в функции read_file_txt")
    except:
        logging.error(f"Ошибка при чтении файла {file_name} в функции read_file_txt")

def write_file(file_name: str, text: str) -> None:
    """Записывает текст из text в файл с именем file_name"""
    try:
        with open(file_name, "w+", encoding="utf-8") as write_file:
            write_file.write(text)

        logging.info(f"Запись в файл '{file_name}' прошла успешно")

    except FileNotFoundError:
        logging.error(f"Не удалось открыть {file_name} в функции write_file")
    except: 
        logging.error(f"Ошибка при записи файла {file_name} в функции write_file")

def encrypt_text(text: str, key: str) -> str:
    """Шифрует текст по таблице Виженера"""
    encrypt_text = ""
    text = text.upper()
    text = text.replace("Ё", "Е")
    key = key.upper()
    key = key.replace("Ё", "Е")
    table_vig = make_table_vig(consts.ALPHABET)
    for str in table_vig:
        print(str)
    len_key = len(key)

    ind_key = 0
    try:
        for word in text:
            if ind_key >= len_key:
                ind_key = 0
                
            if not(key[ind_key] in table_vig[0]):
                ind_key += 1

            if ind_key >= len_key:
                ind_key = 0

            # Если word нет в таблице Виженера, то переходим на следующую итерацию
            # print(word)
            if not(word in table_vig[0]):
                encrypt_text += word
                continue

            ind_col = 0
            for symb in table_vig[0]:
                if symb != word:
                    ind_col += 1
                    continue
                break

            ind_row = 0
            for row in table_vig:
                if row[0] != key[ind_key]:
                    ind_row += 1
                    continue 
                encrypt_text += table_vig[ind_row][ind_col]
                ind_key += 1
                break
            ind_col += 1

        logging.info(f"Шифрование текста прошло успешно")
        return encrypt_text
    
    except IndexError:
        logging.error(f"Произошёл выход за границы объекта "\
                      "в функции encrypt_text")
    except:
        logging.error(f"Произошла ошибка в функции encrypt_text")

def shift_alphabet(arr: list, ind: int) -> list:
    """Смещает влево значения в списке arr до индекса ind"""
    try:
        new_arr = []
        len_arr = len(arr)
        for i in range(len_arr):
            if ind == len_arr:
                ind = 0
            new_arr.append(arr[ind])
            ind += 1

        logging.info(f"Смещение списка прощло успешно")
        return new_arr
    
    except IndexError:
        logging.error(f"Произошёл выход за границы объекта "\
                      "в функции shift_alphabet")
    except:
        logging.error(f"Произошла ошибка в функции shift_alphabet")

def make_table_vig(alphabet: list) -> list:
    """Создаёт таблицу Виженера"""
    try:
        table_vig = []
        len_alphabet = len(alphabet)
        ind = 0
        while ind < len_alphabet:
            arr = shift_alphabet(alphabet, ind)
            table_vig.append(arr)
            ind += 1

        return table_vig
    
    except:
        logging.error(f"Произошла ошибка в функции make_table_vig")



