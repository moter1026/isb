import math
import csv

def sortedDictWithFrequency(frequency: dict, count: int = 0) -> dict:
    """Cортирует по значениям словарь с частотностью символов
    возвращает первые count самых популярных знач"""
    arr_frequency = []

    for key in frequency:
        arr_frequency.append(frequency[key])

    print(f"len arr_freq = {len(arr_frequency)}")
    arr_frequency.sort(reverse=True)
    new_dict = {}

    if count == 0:
        print(f"Вошёл в if")
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
        print(f"Вошёл в else")
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
    counter = {}
    all_symbols = len(text)

    for char in text:
        if char in counter.keys():
            counter[char] += 1
        else:
            counter[char] = 1
    print(f"длина counter = {len(counter)} ")
    our_frequency = counter

    for key in our_frequency:
        our_frequency[key] = our_frequency[key] / all_symbols
    
    return our_frequency

def readCSVFrequency(file_name: str) -> dict:
    """Читает файл формата csv с разделителем '=', возвращает словарь с ключом в виде символа и знач. в виде частоты"""
    frequency = {}
    with open(file_name, "r", encoding="utf-8") as readFile:
        file_reader = csv.reader(readFile, delimiter="=")
        for row in file_reader:
            frequency[row[0].replace(" ", "")] = float(row[1])
    return frequency

def readFileWithText(file_name: str, mode: str, _encoding: str) -> str:
    """Читает текст из файла."""
    text = ''
    with open(file_name, mode, encoding=_encoding) as readFile:
        text = readFile.read()
    return text