import consts

from functions_for_task2 import sortedDictWithFrequency, readCSVFrequency, \
                                readFileWithText, statistic, autoReplaceSymbols, \
                                replacer, writeFrequencyForEncryptText, writeTextFile


if __name__ == "__main__":
    frequency = readCSVFrequency(consts.FILES["frequency_ru"])
    text = readFileWithText(consts.FILES["encrypt_text"], "r", "utf-8")
    our_frequency = sortedDictWithFrequency(statistic(text))
    print(text, "\n\n")

    new_text = text
    res = 0
    while 1:
        res = input(consts.COLOR_YELLOW + f"Вы хотите заменить буквы по статистике из файла:\
                     \n1) с общей статистикой({consts.FILES["frequency_ru"]})\
                     \n2) с уже созданной вами до этого статистикой({consts.FILES["frequency_for_encrypt_text"]})?\n" + consts.COLOR_RESET)
        if res == "1":
            new_text = autoReplaceSymbols(text, list(
                our_frequency.keys()), list(frequency.keys()))
            break
        elif res == "2":
            new_text = autoReplaceSymbols(text, list(our_frequency.keys()), list(
                readCSVFrequency(consts.FILES["frequency_for_encrypt_text"]).keys()))
            break

    while 1:
        print(consts.COLOR_BLUE + new_text + consts.COLOR_RESET)
        print(f"Статистика зашифрованного текста: {
              sortedDictWithFrequency(statistic(new_text))} \n")
        print(f"общая статистика символов: {frequency}")

        first_input = input(consts.COLOR_YELLOW + f"Введите два символа:\
                             \n1-й символ из зашифрованного текста\
                             \n2-й тот, на который хотите заменить\
                            \n\nТакже вы можете ввести 'exit', чтобы выйти из процедуры замены символов\
и при желании сохранить текущую статистику и итог. текст в файлы c итог. статистикой '{consts.FILES["ready_frequency"]}' \
и '{consts.FILES["ready_text"]}' и из процедуры замены символов\n" + consts.COLOR_RESET)

        if first_input.lower() == "exit":
            save = input(f"Сохранить данные?\n1)Да\n2)Нет\n")
            if int(save) == 1:
                writeTextFile(consts.FILES["ready_text"], new_text)
                writeFrequencyForEncryptText(
                    consts.FILES["ready_frequency"], sortedDictWithFrequency(statistic(new_text)))
            break
        second_input = input()

        if first_input in new_text:
            new_text, replace_char = replacer(
                new_text, first_input, second_input)
            new_text, replace_char = replacer(
                new_text, replace_char, first_input)

            writeFrequencyForEncryptText(
                consts.FILES["frequency_for_encrypt_text"], sortedDictWithFrequency(statistic(new_text)))
        else:
            print(consts.COLOR_RED +
                  "Вы ввели неправильный символ из текста, такого символа здесь нет\n" + consts.COLOR_RESET)
            continue
