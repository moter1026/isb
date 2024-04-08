import consts
import logging
import work_with_json

from functions_for_task2 import (sorted_dict_with_frequency,
                                 read_csv_frequency,
                                 read_file_with_text, statistic,
                                 auto_replace_symbols, replacer,
                                 write_frequency_for_encrypt_text, write_text_file)

frequency_ru, encrypt_text, frequency_for_encrypt_text, ready_frequency, ready_text =\
    work_with_json.read_json_file(consts.JSON_FILE)

if __name__ == "__main__":
    try:
        frequency = read_csv_frequency(frequency_ru)
        text = read_file_with_text(encrypt_text, "r", "utf-8")
        our_frequency = sorted_dict_with_frequency(statistic(text))
        print(text, "\n\n")

        new_text = text
        res = 0
        while 1:
            res = input(consts.COLOR_YELLOW +
                        f"Вы хотите заменить буквы по статистике из файла:" \
                        f"\n1) с общей статистикой({frequency_ru})" \
                        f"\n2) с уже созданной вами до этого статистикой" \
                        f"({frequency_for_encrypt_text})?\n" + consts.COLOR_RESET)
            if res == "1":
                new_text = auto_replace_symbols(text, list(
                    our_frequency.keys()), list(frequency.keys()))
                break
            elif res == "2":
                new_text = auto_replace_symbols(text, list(our_frequency.keys()),
                                                list(read_csv_frequency(ready_frequency).keys()))
                break

        while 1:
            print(consts.COLOR_BLUE + new_text + consts.COLOR_RESET)
            print(f"Статистика зашифрованного текста: "
                  f"{sorted_dict_with_frequency(statistic(new_text))} \n")
            print(f"общая статистика символов: {frequency}")

            first_input = input(consts.COLOR_YELLOW +
                                f"Введите два символа:" \
                                f"\n1-й символ из зашифрованного текста" \
                                f"\n2-й тот, на который хотите заменить" \
                                f"\n\nТакже вы можете ввести 'exit', " \
                                f"чтобы выйти из процедуры замены символов " \
                                f"и при желании сохранить текущую статистику и итог. текст в файлы " \
                                f"c итог. статистикой '{ready_frequency}' " \
                                f"и '{ready_text}' и из процедуры замены символов\n" \
                                + consts.COLOR_RESET)

            if first_input.lower() == "exit":
                save = input(f"Сохранить данные?\n1)Да\n2)Нет\n")
                if int(save) == 1:
                    write_text_file(ready_text, new_text)
                    write_frequency_for_encrypt_text(
                        ready_frequency,
                        sorted_dict_with_frequency(statistic(new_text)))
                break
            second_input = input()

            if first_input in new_text:
                new_text, replace_char = replacer(
                    new_text, first_input, second_input)
                new_text, replace_char = replacer(
                    new_text, replace_char, first_input)

                write_frequency_for_encrypt_text(
                    frequency_for_encrypt_text,
                    sorted_dict_with_frequency(statistic(new_text)))
            else:
                print(consts.COLOR_RED +
                      f"Вы ввели неправильный символ из текста,"
                      f" такого символа здесь нет\n" +
                      consts.COLOR_RESET)
                continue

        logging.info(f"Программа завершилась")

    except Exception as e:
        logging.error(f"Программа завершилась неудачей с ошибкой {e}")
