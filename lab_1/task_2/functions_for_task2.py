import math
import csv
import consts


def readCSVFrequency(file_name: str) -> dict:
    """Читает файл file_name формата csv с разделителем '=', возвращает словарь с ключом в виде символа и знач. в виде частоты"""
    frequency = {}
    with open(file_name, "r", encoding="utf-8") as readFile:
        file_reader = csv.reader(readFile, delimiter="=")
        for row in file_reader:
            if row[0].find("(пробел)") == -1:
                frequency[row[0].replace(" ", "")] = float(row[1])
            else:
                row[0] = row[0].replace(" ", "")
                frequency[row[0].replace("(пробел)", " ")] = float(row[1])

    return frequency


def readFileWithText(file_name: str, mode: str, _encoding: str) -> str:
    """Читает текст из файла."""
    text = ''
    with open(file_name, mode, encoding=_encoding) as readFile:
        text = readFile.read()
    return text


def writeFrequencyForEncryptText(file_name: str, freq: dict) -> None:
    """Записывает новую частотность в файл file_name из словаря freq"""
    with open(file_name, "w+", encoding="utf-8") as CSV_file:
        csw_writer = csv.writer(CSV_file, delimiter='=', lineterminator='\n')

        for key in freq:
            if key == " ":
                csw_writer.writerow(["(пробел) ", " " + str(freq[key])])
                continue
            csw_writer.writerow([str(key) + " ", " " + str(freq[key])])

def writeTextFile(file_name: str, text: str) -> None:
    """Записывает текст text в файл file_name"""
    print(consts.COLOR_RED + text + consts.COLOR_RESET)
    with open(file_name, "w+", encoding="utf-8") as text_file:
        text_file.write(text)

def replacer(text: str, old_char: str, new_char: str) -> str:
    """Заменяет символ old_char на new_char в переданном тексте и возвращает его копию.
    Если в тексте уже есть new_char, то они заменяются на символ, который не используется в тексте"""
    if old_char == new_char:
        return text, new_char
    # Получаю список символов из юникода, для возможности замены, если
    # в старом тексте уже будут иметься те символы, на которые я собираюсь заменять
    unicode_list = [chr(i) for i in range(50, 0xC8)]
    new_txt = text
    replace_char = new_char
    if replace_char in text:
        for char in unicode_list:
            if not (char in text):
                replace_char = char
                break

        # Если в исходн. тексте есть символ, на который мы хотим заменить,
        # то заменяем в исходн. тексте на символ, которого ещё нет в нём
        new_txt = text.replace(new_char, replace_char)
    new_txt = new_txt.replace(old_char, new_char)

    return new_txt, replace_char


def sortedDictWithFrequency(frequency: dict, count: int = 0) -> dict:
    """Cортирует по значениям словарь с частотностью символов
    возвращает первые count самых популярных знач"""
    arr_frequency = []

    for key in frequency:
        arr_frequency.append(frequency[key])

    arr_frequency.sort(reverse=True)
    new_dict = {}

    if count == 0:
        ind = 0
        while True:
            if len(arr_frequency) == ind:
                break
            for key in frequency:
                if frequency[key] == arr_frequency[ind]:
                    if key in list(new_dict.keys()):
                        continue
                    else:
                        new_dict[key] = frequency[key]
                        break
            ind += 1
    else:
        ind = 0
        while True:
            if (len(arr_frequency) == ind) or (ind == count):
                break
            for key in frequency:
                if math.isclose(frequency[key], arr_frequency[ind]):
                    if key in new_dict.keys():
                        continue
                    else:
                        new_dict[key] = frequency[key]
                        break
            ind += 1
        print(len(new_dict))

    return new_dict


def statistic(text: str) -> dict:
    """Возвращает статистику текста. Частотность символов в переданном тексте"""
    counter = {}
    all_symbols = len(text)

    for char in text:
        if char in counter.keys():
            counter[char] += 1
        else:
            counter[char] = 1
    our_frequency = counter

    for key in our_frequency:
        our_frequency[key] = our_frequency[key] / all_symbols

    return our_frequency


def autoReplaceSymbols(text: str, statistic_text: list, common_frequency: list, count: int = -1) -> str:
    """Рассчитывает получить зашифр. текст text и отсортированные списки в порядке убывания частоты
    statistic_text - список символов зашифрованного текста,
    common_frequency - список символов независимых текстов.
    Заменяет символы statistic_text на символы из common_frequency. 
    Возвращает новый текст и новый список statistic_text"""
    new_text = text
    ind = 0
    copy_statistic_text = statistic_text
    for char in common_frequency:
        if (len(common_frequency) == ind) or (len(copy_statistic_text) == ind) or ind == count:
            break
        # print(char, f"ind = {ind}", len(copy_statistic_text))
        new_text, new_char = replacer(new_text, copy_statistic_text[ind], char)
        if new_char != char:
            copy_statistic_text[copy_statistic_text.index(char)] = new_char
        copy_statistic_text[ind] = char
        # print(new_text)
        # print(copy_statistic_text)
        writeFrequencyForEncryptText(
            consts.FILES["frequency_for_encrypt_text"], sortedDictWithFrequency(statistic(new_text)))

        ind += 1

    return new_text
