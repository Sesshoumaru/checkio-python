#Your optional code here
#You can import some modules or create additional functions


def checkio(data:list):
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.

    # 方法1 面向过程
    # result = []
    # for x in data:
    #     if data.count(x) > 1:
    #         result.append(x)
    #
    # return result

    # 方法2 列表推导式后循环
    # for y in ([x for x in data if data.count(x) == 1]):
    #     data.remove(y)

    # 方法3 双重列表推导式
    # [data.remove(y) for y in ([x for x in data if data.count(x) == 1])]

    # 方法4 列表推导式
    data = [x for x in data if data.count(x) > 1]
    print(data)

    # replace this for solution
    return data

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")