from collections import Counter

test_input = [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab'
]


def read_input():
    return open('input', 'r').read().split()


def get_checksum(_input: list):
    counter_two, counter_three = 0, 0
    for line in _input:
        chars_dict = Counter(line)
        if 2 in chars_dict.values():
            counter_two += 1
        if 3 in chars_dict.values():
            counter_three += 1
    return counter_two * counter_three


def test():
    assert get_checksum(test_input) == 12


def main():
    test()
    _input = read_input()
    print('Day 02 Part 1:', get_checksum(_input))


if __name__ == '__main__':
    main()
