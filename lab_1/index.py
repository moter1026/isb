import os

from functions_for_task2 import sortedDictWithFrequency, readCSVFrequency, readFileWithText, statistic, autoReplaceSymbols





if __name__ == "__main__":
    
    frequency = readCSVFrequency("./частота русских символов.csv")

    text = readFileWithText("./cod7.txt", "r", "utf-8")
    print(text, "\n\n")

    our_frequency = statistic(text)

    our_frequency = sortedDictWithFrequency(our_frequency)
    print(our_frequency, "\n\n")

    new_text, copy_stat_list =  autoReplaceSymbols(text, list(our_frequency.keys()), list(frequency.keys()))

    print(new_text, "\n", copy_stat_list, "\n\n")



    # while True:
    #     # count = ''
    #     # count = int(input("Введите сколько символов из топ популярных необх. заменить. Или отриц. число, чтобы завершить программу "))
    #     print(text)
    #     print(f"Статистика зашифрованного текста: {sortedDictWithFrequency(statistic(text))} \n")
    #     print(f"общая статистика символов: {frequency}")

    #     char1 = input(f"Введите два символа. 1-й символ из зашифрованного текста, 2-й тот, на который хотите заменить\t")

    #     char2 = input()

    #     if char1 in text:
    #         text = replacer(text, char1, char2)
    #         # print("\n", text, "\n")
    #     else:
    #         print("Вы ввели неправильный символ из текста, такого символа здесь нет\n")
    #         continue

    #     # print(decoder(text, frequency, count))



