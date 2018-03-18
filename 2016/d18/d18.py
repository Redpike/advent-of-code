test_input = '.^^.^.^^^^'

traps = (
    (True, True, False),
    (False, True, True),
    (True, False, False),
    (False, False, True)
)


def read_input_file():
    return open('input', 'r').readline()


def get_safe_tiles(_input: str, times: int):
    current_row = [x == '^' for x in _input]
    counter = current_row.count(False)
    for _ in range(times - 1):
        next_row = []
        for i in range(len(current_row)):
            left, center, right = i > 0 and current_row[i - 1], current_row[i], i < len(current_row) - 1 and current_row[i + 1]
            next_row.append((left, center, right) in traps)
        counter += next_row.count(False)
        current_row = next_row
    return counter


def test():
    assert get_safe_tiles(test_input, 10) == 38


def main():
    test()
    input_data = read_input_file()
    print('Day 18 Part 1:', get_safe_tiles(input_data, 40))


if __name__ == '__main__':
    main()
