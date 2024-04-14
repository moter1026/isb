import tests
import consts


def main() -> None:
    sequence_cpp = ""
    sequence_java = ""
    try:
        with open(consts.SEQUENCE_CPP, "r", encoding="utf-8") as read_file:
            sequence_cpp = read_file.read()
    except Exception as err:
        print(f"{consts.COLOR_RED} Ошибка {err} при открытии файла {consts.SEQUENCE_CPP}")

    try:
        with open(consts.SEQUENCE_JAVA, "r", encoding="utf-8") as read_file:
            sequence_java = read_file.read()
    except Exception as err:
        print(f"{consts.COLOR_RED} Ошибка {err} при открытии файла {consts.SEQUENCE_JAVA}")


    with open(consts.RESULT_FILE, mode="w", encoding="utf-8") as write_file:
        write_file.write(f"Частотный побитовый тест файла {consts.SEQUENCE_CPP} = " +
          f"{tests.frequency_binary_test(sequence_cpp)} \n"
          f"Тест на одинаковые подряд идущие биты в файле {consts.SEQUENCE_CPP} = " +
          f"{tests.the_same_bits_test(sequence_cpp)} \n"
          f"Тест на самую длинную последовательность единиц в блоке " +
          f"в файле {consts.SEQUENCE_CPP} = {tests.longest_sequence_of_ones(sequence_cpp)}\n"
          f"\n\n"
          f"Частотный побитовый тест файла {consts.SEQUENCE_JAVA} = " +
          f"{tests.frequency_binary_test(sequence_java)} \n"
          f"Тест на одинаковые подряд идущие биты в файле {consts.SEQUENCE_JAVA} = " +
          f"{tests.the_same_bits_test(sequence_java)} \n"
          f"Тест на самую длинную последовательность единиц в блоке " +
          f"в файле {consts.SEQUENCE_JAVA} = {tests.longest_sequence_of_ones(sequence_java)}")
    

if __name__ == "__main__":
    main()