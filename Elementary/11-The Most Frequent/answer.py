def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    print([(data.count(x),x) for x in data])
    return max([(data.count(x),x) for x in data])[1]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
