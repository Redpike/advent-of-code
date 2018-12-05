def read_input():
    return open('input', 'r').readline()


def get_remaining_units(_input: str):
    temp_line = None
    while temp_line != _input:
        temp_line = _input
        for i in range(0, 26):
            _input = _input.replace(chr(ord('a') + i) + chr(ord('A') + i), '')
            _input = _input.replace(chr(ord('A') + i) + chr(ord('a') + i), '')
    return len(_input)


def test():
    assert get_remaining_units('dabAcCaCBAcCcaDA') == 10


def main():
    test()
    _input = read_input()
    print('Day 05 Part 1:', get_remaining_units(_input))


if __name__ == '__main__':
    main()
