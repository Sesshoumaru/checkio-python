def safe_pawns(pawns):
    # 方法1 面向过程
    # num = 0
    # for pawn in pawns:
    #     x, y = ord(pawn[0]), int(pawn[1])
    #     left_bottom = chr(x - 1) + str((y - 1))
    #     right_bottom = chr(x + 1) + str((y - 1))
    #
    #     if left_bottom in pawns or right_bottom in pawns:
    #         num += 1
    # return num

    # 方法2 列表推导式
    return(sum([(chr(ord(pawn[0]) - 1) + str(int(pawn[1] )- 1)) in pawns or (chr(ord(pawn[0]) + 1) + str(int(pawn[1] )- 1)) in pawns for pawn in pawns]))

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
