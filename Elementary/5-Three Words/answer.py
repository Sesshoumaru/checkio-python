def checkio(words):
    array = [1 if x.isalpha() else 0 for x in words.split(" ")]
    for i in range(1, len(array)):
        if array[i]  > 0 and array[i-1] > 0:
            array[i] = array[i] + array[i - 1]

    return max(array) > 2

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
