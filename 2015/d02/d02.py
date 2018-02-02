test_input = [
    '2x3x4',
    '1x1x10'
]


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file.read().splitlines():
        input_data.append(line)
    return input_data


def computeSquareFeets(input_data):
    l, w, h, sum_of_values = 0, 0, 0, 0

    for line in input_data:
        l = int(line.split('x')[0])
        w = int(line.split('x')[1])
        h = int(line.split('x')[2])
        lw = 2 * l * w
        wh = 2 * w * h
        lh = 2 * l * h
        minimum = min([lw // 2, wh // 2, lh // 2])
        sum_of_values += (lw + wh + lh + minimum)
    return sum_of_values


# tricky method
def computeFeetOfRibbon(input_data):
    l, w, h, sum_of_values = 0, 0, 0, 0

    for line in input_data:
        l = int(line.split('x')[0])
        w = int(line.split('x')[1])
        h = int(line.split('x')[2])
        collection = [l, w, h]
        minimum1 = min(collection)
        collection.remove(minimum1)
        minimum2 = min(collection)
        sum_of_values += ((2 * minimum1 + 2 * minimum2) + (l * w * h))
    return sum_of_values


def test():
    assert computeSquareFeets(test_input) == 101
    assert computeFeetOfRibbon(test_input) == 48


def main():
    test()
    input_data = readInputFile()
    print('Day 02 Part 1:', computeSquareFeets(input_data))
    print('Day 02 Part 2:', computeFeetOfRibbon(input_data))


if __name__ == '__main__':
    main()
