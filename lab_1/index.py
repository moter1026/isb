import os
import csv

def sortedDictWithFrequency(frequency: dict, count: int = 0) -> dict:
    """Cортирует по значениям словарь с частотностью символов
    возвращает первые count самых популярных знач"""
    arr_frequency = []
    for key in frequency:
        arr_frequency.append(frequency[key])
        # comment: 
    # end for
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
                    new_dict[key] = frequency[key]
                    # print(new_dict[key], ind)
                    break
                # comment: 
            # end for
            ind += 1
    else:
        print(f"Вошёл в else")
        ind = 0
        while True:
            if (len(arr_frequency) == ind) or (ind == count):
                break
            for key in frequency:
                if frequency[key] == arr_frequency[ind]:
                    new_dict[key] = frequency[key]
                    # print(new_dict[key], ind)
                    break
                # comment: 
            # end for
            ind += 1
    return new_dict

def decoder(text: str, frequency: dict, count: int) -> str:
    counter = {}
    all_symbols = 0
    for char in text:
        if char in counter.keys():
            counter[char] += 1
        else:
            counter[char] = 1
        all_symbols += 1
    # end for
    our_frequency = counter
    for key in our_frequency:
        our_frequency[key] = our_frequency[key] / all_symbols

    replace = sortedDictWithFrequency(our_frequency, count)
    print(replace, "\n")
    print(frequency)

    # print("\n",list(frequency.keys())[2])
    ind = 0
    for key in replace:
        if ind == len(replace):
            break
        replace[key] = list(frequency.keys())[ind]
        ind += 1
        # comment: 
    # end for

    new_txt = ""
    find_in_replace = False
    for char in text:
        for key in replace:
            if char == key:
                new_txt += replace[key]
                find_in_replace = True
                break
            # comment: 
        # end for
        if find_in_replace == False:
            new_txt += char
    new_txt = new_txt.replace("(пробел)", " ")

    return new_txt

def readCSVFrequency(file_name: str) -> dict:
    """Читает файл формата csv с разделителем '=', возвращает словарь с ключом в виде символа и знач. в виде частоты,
    если сам файл правильно создан."""
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

if __name__ == "__main__":
    
            # comment: 
        # end for
    # print(frequency)
    frequency = readCSVFrequency("./частота русских символов.csv")

    text = readFileWithText("./cod7.txt", "r", "utf-8")
    print(text, "\n\n")

    while True:
        count = ''
        count = int(input("Введите сколько символов из топ популярных необх. заменить. Или отриц. число, чтобы завершить программу "))
        if count < 0:
            break
        print(decoder(text, frequency, count))



