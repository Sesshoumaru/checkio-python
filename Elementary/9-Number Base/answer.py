def checkio(str_number, radix):

    def get_radixs(radix):
        result = []
        for i in range(0,radix):
            if i < 10:
                result.append(str(i))
            else:
                result.append(chr(65 + i - 10))
        return result

    radixs = get_radixs(radix)

    result = 0
    length = len(str_number)
    for i in range(0,length):
        if str_number[i] not in radixs:
            return -1

        print(pow(radix,length-i-1))
        print(radixs.index(str_number[i]))
        result = result + pow(radix,length-i-1)*radixs.index(str_number[i])

    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")