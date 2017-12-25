test_input = [
    '0/2',
    '2/2',
    '2/3',
    '3/4',
    '3/5',
    '0/1',
    '10/1',
    '9/10'
]


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        line = line.strip('\n')
        input_data.append(line)
    return input_data


def parseData(input_data):
    data = []
    for line in input_data:
        a, b = line.split('/')
        data.append((int(a), int(b)))
    return data


def run(bridge, data):
    available = [a for a in data if bridge[1] in a]
    if len(available) == 0:
        yield bridge
    else:
        for a in available:
            d_ = data.copy()
            d_.remove(a)
            for q in run((bridge[0] + [a], a[0] if bridge[1] == a[1] else a[1]), d_):
                yield q


def getTheStrongestBridge(input_data):
    bridge = ([], 0)
    data = parseData(input_data)
    return max(map(lambda bridge: sum([a + b for a, b in bridge[0]]), run(bridge, data)))


def getTheLongestBridge(input_data):
    bridge = ([], 0)
    data = parseData(input_data)
    max_len = max(map(lambda bridge: len(bridge[0]), run(bridge, data)))
    long = filter(lambda bridge: len(bridge[0]) == max_len, run(bridge, data))
    return max(map(lambda bridge: sum([a + b for a, b in bridge[0]]), long))


def test():
    assert getTheStrongestBridge(test_input) == 31
    assert getTheLongestBridge(test_input) == 19


def main():
    test()
    input_data = readInputFile()
    print('Day 24 Part 1:', getTheStrongestBridge(input_data))
    print('Day 24 Part 2:', getTheLongestBridge(input_data))


if __name__ == '__main__':
    main()
