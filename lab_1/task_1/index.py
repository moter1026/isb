import consts

from functions_for_task1 import readFileTXT, encryptText, writeFile


if __name__ == "__main__":
    text = readFileTXT(consts.FILES["text_start"])
    key = readFileTXT(consts.FILES["key"])

    encrypt_text = encryptText(text, key)

    print(encrypt_text)

    writeFile(consts.FILES["text_end"], encrypt_text)



