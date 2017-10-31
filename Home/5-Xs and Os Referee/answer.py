def checkio(game_result):

    # 方法1 面向过程
    # for row in game_result:
    #     if row[0] == row[1] == row[2] and row[0] != '.':
    #         return row[0]
    #
    # for row in zip(*game_result):
    #     if row[0] == row[1] == row[2] and row[0] != '.':
    #         return row[0]
    #
    # if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != '.':
    #     return  game_result[0][0]
    #
    # if game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[0][2] != '.':
    #     return game_result[0][2]
    #
    # return "D"


    # 方法2 先把可能的结果列出来，再推断
    game_result.extend(list(zip(*game_result)))
    game_result.extend(((game_result[0][0],game_result[1][1],game_result[2][2]),(game_result[0][2],game_result[1][1],game_result[2][0]),('D','D','D')))
    return [row for row in game_result if row.count('.') == 0 and row.count(row[0]) == 3][0][0]



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

