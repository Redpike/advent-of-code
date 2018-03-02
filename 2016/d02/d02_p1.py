test_input = [
    'ULL',
    'RRDDD',
    'LURDL',
    'UUUUD'
]

keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def read_input_file():
    return open('input', 'r').read().splitlines()


def get_digit_from_instruction(instruction: str, position_x: int, position_y: int):
    for move in instruction:
        if move == 'U':
            position_y -= 1
        elif move == 'D':
            position_y += 1
        elif move == 'R':
            position_x += 1
        elif move == 'L':
            position_x -= 1

        if position_y > 2:
            position_y = 2
        elif position_y < 0:
            position_y = 0
        elif position_x > 2:
            position_x = 2
        elif position_x < 0:
            position_x = 0

    return str(keypad[position_y][position_x]), position_x, position_y


def decode(input_data):
    code = ''
    position_x, position_y = 1, 1
    for instruction in input_data:
        part_code, position_x, position_y = get_digit_from_instruction(instruction, position_x, position_y)
        code += part_code
    return code


def test():
    assert decode(test_input) == '1985'


def main():
    test()
    input_data = read_input_file()
    print('Day 02 Part 1:', decode(input_data))


if __name__ == '__main__':
    main()
