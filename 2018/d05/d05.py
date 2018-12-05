def read_input():
    return open('input', 'r').readline()


def get_remaining_units(_input: str):
    line = _input
    temp_line = None
    while temp_line != line:
        temp_line = line
        for i in range(0, 26):
            line = line.replace(chr(ord('a') + i) + chr(ord('A') + i), '')
            line = line.replace(chr(ord('A') + i) + chr(ord('a') + i), '')
    return len(line)


def remove_pattern(_input: str):
    line = _input
    best = len(line)
    for j in range(0, 26):
        line = _input
        line = line.replace(chr(ord('a') + j), '')
        line = line.replace(chr(ord('A') + j), '')
        temp_line = None
        while temp_line != line:
            temp_line = line
            for i in range(0, 26):
                line = line.replace(chr(ord('a') + i) + chr(ord('A') + i), '')
                line = line.replace(chr(ord('A') + i) + chr(ord('a') + i), '')
        best = len(line) if len(line) < best else best
    return best


def test():
    assert get_remaining_units('dabAcCaCBAcCcaDA') == 10
    assert remove_pattern('dabAcCaCBAcCcaDA') == 4


def main():
    test()
    _input = read_input()
    print('Day 05 Part 1:', get_remaining_units(_input))
    print('Day 05 Part 2:', remove_pattern(_input))


if __name__ == '__main__':
    main()
