import consts


def readFileTXT(file_name: str) -> str:
    """Читает файл"""
    text = ""
    with open(file_name, "r", encoding="utf-8") as file_txt:
        text = file_txt.read()
    return text

def writeFile(file_name: str, text: str) -> None:
    """Записывает текст из text в файл с именем file_name"""
    if file_name == '' or file_name == ' ':
        return
    with open(file_name, "w+", encoding="utf-8") as write_file:
        write_file.write(text)

def encryptText(text: str, key: str) -> str:
    """Шифрует текст по таблице Виженера"""
    encrypt_text = ""
    text = text.upper()
    key = key.upper()
    table_vig = makeTableVig(consts.ALPHABET)
    len_key = len(key)

    ind_key = 0
    for word in text:
        if ind_key >= len_key:
            ind_key = 0
            
        if not(key[ind_key] in table_vig[0]):
            ind_key += 1

        if ind_key >= len_key:
            ind_key = 0

        # Если word нет в таблице Виженера, то переходим на следующую итерацию
        if not(word in table_vig[0]):
            continue

        ind_col = 0
        for symb in table_vig[0]:
            if symb != word:
                ind_col += 1
                continue;
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

    return encrypt_text

def shiftAlphabet(arr: list, ind: int) -> list:
    """Смещает влево значения в списке arr до индекса ind"""
    new_arr = []
    len_arr = len(arr)
    for i in range(len_arr):
        if ind == len_arr:
            ind = 0
        new_arr.append(arr[ind])
        ind += 1
    return new_arr

def makeTableVig(alphabet: list) -> list:
    """Создаёт таблицу Виженера"""
    table_vig = []
    len_alphabet = len(alphabet)
    ind = 0;
    while ind < len_alphabet:
        arr = shiftAlphabet(alphabet, ind)
        table_vig.append(arr)
        ind += 1

    return table_vig