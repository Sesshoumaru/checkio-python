def count_words(text, words):

    text = text.lower()

    # 方法1 面向过程
    # result = 0
    # for word in words:
    #     if text.count(word):
    #         result += 1
    #
    # return result

    # 方法2 列表推导式 + count + sum求和
    #return sum((bool(text.count(word)) for word in words))

    # 方法3 列表推导式 + in + sum求和
    return sum((word in text for word in words))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
