test_input = [
    '0: 3',
    '1: 2',
    '4: 4',
    '6: 4'
]


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        line = line.strip('\n')
        input_data.append(line)
    return input_data


def test():
    pass


def selectInput(is_production):
    if is_production:
        return readInputFile()
    else:
        return test_input


def main():
    test()
    input_data = selectInput(False)
    print(input_data)
    print('Day 13 Part 1:', )
    print('Day 13 Part 2:', )


if __name__ == '__main__':
    main()
