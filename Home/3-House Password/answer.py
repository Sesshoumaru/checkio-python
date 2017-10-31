import re


def checkio(data: str):
    if len(data) < 10:
        return False

    # 方法1 面向过程
    # result = [0,0,0]
    # for ch in data:
    #     if ch.isdigit():
    #         result[0] = result[0] + 1
    #     elif ch.isalpha():
    #         if ch.isupper():
    #             result[1] = result[1] + 1
    #         else:
    #             result[2] = result[2] + 1
    #
    # print(result)
    # # return bool(result[0] and result[1] and result[2])
    # return all(result)

    # 方法2 列表推导式
    # print(len([x for x in data if x.isdigit()]) )
    # print(len([x for x in data if x.isalpha() and x.isupper()]))
    # print(len([x for x in data if x.isalpha() and x.islower()]))
    # return len([x for x in data if x.isdigit()]) > 0 and len([x for x in data if x.isalpha() and x.isupper()]) > 0 and len([x for x in data if x.isalpha() and x.islower()]) > 0

    # 方法2 列表推导式
    return all(([x for x in data if x.isdigit()], [x for x in data if x.isupper()], [x for x in data if x.islower()]))


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
