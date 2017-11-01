def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    line_length = len(line)
    if line_length <= 1:
        return line_length

    count_list = [0]
    current_count = 1
    current_ch = ''
    for i in range(0,line_length):
        ch = line[i]
        if ch == current_ch:
            current_count += 1

            if i == line_length - 1:
                count_list.append(current_count)
        else:
            count_list.append(current_count)
            current_count = 1
            current_ch = ch

    print(count_list)
    return max(count_list)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('') == 0, "Third"
    assert long_repeat('aa') == 2, "Four"
    print('"Run" is good. How is "Check"?')
