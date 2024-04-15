import math
import consts

from scipy.special import gammainc


def check_binary_subsequence(subsequnce: str) -> None:
    """
    Проверяет последовательность на бинарность.
    В случае отрицательного результата кидает
    исключение "Not binary subsequence"
    """
    for symb in subsequnce:
        if symb != "1" and symb != "0":
            raise NameError("Not binary subsequence")


def frequency_binary_test(subsequence: str) -> float:
    """
    Получает строку с последовательностью 0 и 1

    Если возвращаемое значение близко к 1, 
    то последовательность достаточно случайна
    """
    check_binary_subsequence(subsequnce=subsequence)

    sum_x = 0

    for bit in subsequence:
        if bit == "1":
            sum_x += 1
        else:
            sum_x -= 1
    
    Sn = abs((1 / math.sqrt(len(subsequence))) * sum_x)
    return math.erfc(Sn / math.sqrt(2))


def the_same_bits_test(subsequence: str) -> float:
    """
    Получает строку с последовательностью 0 и 1

    Если возвращаемое значение близко к 1, 
    то последовательность достаточно случайна
    """
    check_binary_subsequence(subsequnce=subsequence)
    len_subsequnce = len(subsequence)
    sum_x = 0

    for bit in subsequence:
        if bit == "1":
            sum_x += 1
    
    sigma = sum_x / len_subsequnce

    if not(abs(sigma - 0.5) < (2 / math.sqrt(len_subsequnce))):
        return 0
    
    Vn = 0
    prev = 0
    is_first = True
    for bit in subsequence:
        if is_first:
            prev = bit
            is_first = False
            continue

        if prev != bit:
            Vn += 1
            prev = bit
        else:
            prev = bit
    
    return math.erfc(abs(Vn - 2 * len_subsequnce * sigma * (1 - sigma)) /
                    (2 * math.sqrt(2 * len_subsequnce) * sigma * (1 - sigma)))


def longest_sequence_of_ones(subsequence: str) -> float:
    """
    Получает строку с последовательностью 0 и 1
    
    Для всех тестов справедливо, что если
    возвращаемое значение ≥ 0.01, то 
    последовательность признается случайной
    """
    len_subsequnce = len(subsequence)
    count_ones = [0,0,0,0]
    
    ind = 0
    while ind < (len_subsequnce / consts.BLOCK_M):
        ind_start = consts.BLOCK_M * ind
        ind_end = ind_start + consts.BLOCK_M
        block_str = subsequence[ind_start: ind_end]

        max_count = 0
        count = 0
        was_one = False
        for bit in block_str:
            if bit == "1":
                count += 1
                was_one = True
                continue

            if was_one:
                max_count = count if max_count < count else max_count
                count = 0
                was_one = False

        if max_count < count:
            max_count = count

        if max_count <= 1:
            count_ones[0] += 1 
        elif max_count == 2:
            count_ones[1] += 1
        elif max_count == 3:
            count_ones[2] += 1
        elif max_count >= 4:
            count_ones[3] += 1

        ind += 1

    hi_quadro = 0
    ind = 0
    for Vi in count_ones:
        hi_quadro += math.pow((Vi - 16 * consts.PI[ind]), 2) /\
                    (16 * consts.PI[ind])
        
    return gammainc(3 / 2, hi_quadro / 2)
