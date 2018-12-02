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
    pass


def test():
    pass


def main():
    test()
    _input = read_input()
    print('Day 02 Part 1:', get_checksum(_input))


if __name__ == '__main__':
    main()
