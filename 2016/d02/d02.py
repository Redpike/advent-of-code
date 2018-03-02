test_input = [
    'ULL',
    'RRDDD',
    'LURDL',
    'UUUUD'
]

keypad_part_1 = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', '1', '2', '3', ' '],
    [' ', '4', '5', '6', ' '],
    [' ', '7', '8', '9', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

keypad_part_2 = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', '1', ' ', ' ', ' '],
    [' ', ' ', '2', '3', '4', ' ', ' '],
    [' ', '5', '6', '7', '8', '9', ' '],
    [' ', ' ', 'A', 'B', 'C', ' ', ' '],
    [' ', ' ', ' ', 'D', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ']
]


def read_input_file():
    return open('input', 'r').read().splitlines()


def get_digit_from_instruction(keypad: list, instruction: str, position_x: int, position_y: int):
    for move in instruction:
        if move == 'U' and keypad[position_y - 1][position_x] != ' ':
            position_y -= 1
        elif move == 'D' and keypad[position_y + 1][position_x] != ' ':
            position_y += 1
        elif move == 'R' and keypad[position_y][position_x + 1] != ' ':
            position_x += 1
        elif move == 'L' and keypad[position_y][position_x - 1] != ' ':
            position_x -= 1

    return keypad[position_y][position_x], position_x, position_y


def decode_part_1(input_data, keypad):
    code = ''
    position_x, position_y = 2, 2
    for instruction in input_data:
        part_code, position_x, position_y = get_digit_from_instruction(keypad, instruction, position_x, position_y)
        code += part_code
    return code


def decode_part_2(input_data, keypad):
    code = ''
    position_x, position_y = 1, 3
    for instruction in input_data:
        part_code, position_x, position_y = get_digit_from_instruction(keypad, instruction, position_x, position_y)
        code += part_code
    return code


def test():
    assert decode_part_1(test_input, keypad_part_1) == '1985'
    assert decode_part_2(test_input, keypad_part_2) == '5DB3'


def main():
    test()
    input_data = read_input_file()
    print('Day 02 Part 1:', decode_part_1(input_data, keypad_part_1))
    print('Day 02 Part 2:', decode_part_2(input_data, keypad_part_2))


if __name__ == '__main__':
    main()
