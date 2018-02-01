test_input = [
    '(())',
    '(((',
    '))(((((',
    '())',
    ')))'
]


def readInputFile():
    input_file = open('input', 'r')
    input_data = input_file.readline()
    return input_data


def getFloor(input_data):
    up_counter = input_data.count('(')
    down_counter = input_data.count(')')
    return up_counter - down_counter


def getTheFirstTimeOnBasement(input_data):
    position = 1
    floor = 0

    for element in list(input_data):
        if element == '(':
            floor += 1
        elif element == ')':
            floor -= 1

        if floor == -1:
            return position
        position += 1


def test():
    assert getFloor(test_input[0]) == 0
    assert getFloor(test_input[1]) == 3
    assert getFloor(test_input[2]) == 3
    assert getFloor(test_input[3]) == -1
    assert getFloor(test_input[4]) == -3


def main():
    test()
    input_data = readInputFile()
    print('Day 01 Part 1:', getFloor(input_data))
    print('Day 01 Part 2:', getTheFirstTimeOnBasement(input_data))


if __name__ == '__main__':
    main()
