import string

test_input = [
    '     |          ',
    '     |  +--+    ',
    '     A  |  C    ',
    ' F---|----E|--+ ',
    '     |  |  |  D ',
    '     +B-+  +--+ '
]


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        line = line.strip('\n')
        input_data.append(line)
    return input_data


def getStartingPoint(input_data):
    x = input_data[0].index('|')
    y = 0
    return x, y


def getCharFromCords(input_data, x, y):
    try:
        return input_data[y][x]
    except IndexError:
        return ' '


def getStringOrSteps(input_data, part):
    x, y = getStartingPoint(input_data)
    dx, dy = 0, 1 #direction -> currently DOWN
    string_in_map = ''
    steps = 0
    while True:
        next_char = getCharFromCords(input_data, x, y)
        if next_char == ' ':
            break
        elif next_char in string.ascii_uppercase:
            string_in_map += next_char
        elif next_char == '+':
            if getCharFromCords(input_data, x + dy, y + dx) != ' ':
                dx, dy = dy, dx #moving RIGHT or DOWN
            elif getCharFromCords(input_data, x - dy, y - dx) != ' ':
                dx, dy = -dy, -dx #moving LEFT or UP
        x += dx
        y += dy
        steps += 1
    if part == 1:
        return string_in_map
    else:
        return steps


def test():
    assert getStringOrSteps(test_input, 1) == 'ABCDEF'
    assert getStringOrSteps(test_input, 2) == 38


def main():
    test()
    input_data = readInputFile()
    print('Day 19 Part 1:', getStringOrSteps(input_data, 1))
    print('Day 19 Part 2:', getStringOrSteps(input_data, 2))


if __name__ == '__main__':
    main()
