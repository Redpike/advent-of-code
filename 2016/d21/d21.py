from itertools import permutations

test_string = 'abcde'
input_string = 'abcdefgh'
password = 'fbgdceah'
test_input = [
    'swap position 4 with position 0',
    'swap letter d with letter b',
    'reverse positions 0 through 4',
    'rotate left 1 step',
    'move position 1 to position 4',
    'move position 3 to position 0',
    'rotate based on position of letter b',
    'rotate based on position of letter d'
]


def read_input_file():
    return open('input', 'r').read().splitlines()


def rotate_right(string: list, n):
    return string[-n:] + string[:-n]


def rotate_left(string: list, n):
    return string[n:] + string[:n]


def do_instruction(string: list, line: str, splitted_line: list, digits: list):
    if line.startswith('swap position'):
        x, y = digits
        string[x], string[y] = string[y], string[x]
    elif line.startswith('swap letter'):
        x, y = splitted_line[2], splitted_line[-1]
        i, j = string.index(x), string.index(y)
        string[i], string[j] = string[j], string[i]
    elif line.startswith('rotate left'):
        x = digits[0]
        string = rotate_left(string, x)
    elif line.startswith('rotate right'):
        x = digits[0]
        string = rotate_right(string, x)
    elif line.startswith('rotate based'):
        c = splitted_line[-1]
        i = string.index(c)
        i += (i >= 4) + 1
        string = rotate_right(string, i % len(string))
    elif line.startswith('reverse'):
        x, y = digits
        string[x:y + 1] = string[x:y + 1][::-1]
    else:
        x, y = digits
        a = string.pop(x)
        string = string[:y] + [a] + string[y:]
    return string


def scrabble(instructions: list, string: str):
    string = list(string)
    for line in instructions:
        splitted_line = line.split()
        digits = [int(x) for x in splitted_line if x.isdigit()]
        string = do_instruction(string, line, splitted_line, digits)
    return ''.join(string)


def inverse_scrabble(instructions: list, target: str):
    for perm in permutations(target):
        if scrabble(instructions, perm) == target:
            return ''.join(perm)


def test():
    assert scrabble(test_input, test_string) == 'decab'


def main():
    test()
    input_data = read_input_file()
    print('Day 21 Part 1:', scrabble(input_data, input_string))
    pre_scrabbled_string = inverse_scrabble(input_data, password)
    print('Day 22 Part 2:', pre_scrabbled_string)
    assert scrabble(input_data, pre_scrabbled_string) == password


if __name__ == '__main__':
    main()
