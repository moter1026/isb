import os

from functions_for_task2 import sortedDictWithFrequency, readCSVFrequency, readFileWithText, statistic

def decoder(text: str, frequency: dict, count: int) -> str:
    
    our_frequency = statistic(text)
    
    replace = sortedDictWithFrequency(our_frequency, count)
    print(f"replace - {replace} \n")
    print(f"frequency - {frequency}")
    # print(replace, "\n")
    # print(frequency)

    ind = 0
    for key in replace:
        if ind == len(replace):
            break
        replace[key] = list(frequency.keys())[ind]
        ind += 1
    print(f"\n {replace}")

    new_txt = ""
    find_in_replace = False
    for char in text:
        for key in replace:
            if char == key:
                new_txt += replace[key]
                find_in_replace = True
                break

        if find_in_replace == False:
            new_txt += char

        find_in_replace = False
    new_txt = new_txt.replace("(пробел)", " ")

    return new_txt



if __name__ == "__main__":
    
    frequency = readCSVFrequency("./частота русских символов.csv")

    text = readFileWithText("./cod7.txt", "r", "utf-8")
    print(text, "\n\n")

    while True:
        count = ''
        count = int(input("Введите сколько символов из топ популярных необх. заменить. Или отриц. число, чтобы завершить программу "))
        print(text)
        if count < 0:
            break
        print(decoder(text, frequency, count))



