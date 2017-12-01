def readInputFileAndSplit():
    input_file = open('input', 'r')
    input_data = input_file.readline()
    splitted_data = list(input_data)
    return splitted_data


def sum(splitted_data, step):
    sum_of_elements = 0
    for i in range(0, len(splitted_data)):
        neighbour_element_index = i - step
        if int(splitted_data[neighbour_element_index]) == int(splitted_data[i]):
            sum_of_elements += int(splitted_data[i])
    return sum_of_elements


def test():
    assert sum(['1', '1', '2', '2'], 1) == 3
    assert sum(['1', '1', '1', '1'], 1) == 4
    assert sum(['1', '2', '3', '4'], 1) == 0
    assert sum(['9', '1', '2', '1', '2', '1', '2', '9'], 1) == 9
    assert sum(['1', '2', '1', '2'], 2) == 6
    assert sum(['1', '2', '2', '1'], 2) == 0
    assert sum(['1', '2', '3', '4', '2', '5'], 3) == 4
    assert sum(['1', '2', '3', '1', '2', '3'], 3) == 12
    assert sum(['1', '2', '1', '3', '1', '4', '1', '5'], 4) == 4


def main():
    test()
    splitted_data = readInputFileAndSplit()
    print("Day 1 Part 1:", sum(splitted_data, 1))
    print("Day 1 Part 2:", sum(splitted_data, int((len(splitted_data)) / 2)))


if __name__ == '__main__':
    main()
