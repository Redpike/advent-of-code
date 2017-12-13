from collections import defaultdict

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


def prepareFirewall(input_data):
    firewall = defaultdict(int)
    for line in input_data:
        layer = int(line.split(': ')[0])
        depth = int(line.split(': ')[1])
        firewall.update({layer: depth})
    return firewall


def computeSeverity(firewall):
    severity = 0

    for layer in firewall:
        steps_to_start_position = 2 * (firewall.get(layer) - 1)
        if layer % steps_to_start_position == 0:
            severity += (layer * firewall.get(layer))

    return severity


def computeDelay(firewall):
    delay = 0
    caught = True
    while caught:
        is_scanner_there = False
        for layer in firewall:
            picosecond = layer + delay
            steps_to_start_position = 2 * (firewall.get(layer) - 1)
            if picosecond % steps_to_start_position == 0:
                is_scanner_there = True
                break

        if is_scanner_there:
            delay += 1
        else:
            caught = False

    return delay

    return delay


def test():
    firewall = prepareFirewall(test_input)
    assert computeSeverity(firewall) == 24


def selectInput(is_production):
    if is_production:
        return readInputFile()
    else:
        return test_input


def main():
    test()
    input_data = selectInput(True)
    firewall = prepareFirewall(input_data)
    print('Day 13 Part 1:', computeSeverity(firewall))
    print('Day 13 Part 2:', computeDelay(firewall))


if __name__ == '__main__':
    main()
