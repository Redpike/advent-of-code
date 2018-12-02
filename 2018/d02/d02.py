from collections import Counter
from itertools import combinations, compress

test_input = [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab'
]

test_input_2 = [
    'abcde',
    'fghij',
    'klmno',
    'pqrst',
    'fguij',
    'axcye',
    'wvxyz'
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


def get_common_letters(_input: list):
    for one, two in combinations(_input, 2):
        difference = [e1 == e2 for e1, e2 in zip(one, two)]
        if sum(difference) == (len(one) - 1):
            return ''.join(list(compress(one, difference)))


def test():
    assert get_checksum(test_input) == 12
    assert get_common_letters(test_input_2) == 'fgij'


def main():
    test()
    _input = read_input()
    print('Day 02 Part 1:', get_checksum(_input))
    print('Day 02 Part 2:', get_common_letters(_input))


if __name__ == '__main__':
    main()
