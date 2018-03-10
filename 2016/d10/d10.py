from collections import defaultdict

from functools import reduce


class Bot(object):
    def __init__(self):
        self.values = []
        self.low = None
        self.high = None

    def receive(self, value):
        self.values.append(value)
        self.check()

    def check(self):
        if self.low and self.high and len(self.values) == 2:
            self.low.receive(min(self.values))
            self.high.receive(max(self.values))


class OutputBin(object):
    def __init__(self):
        self.values = []

    def receive(self, value):
        self.values.append(value)

    def __repr__(self):
        return 'Bin with ' + ', '.join(map(str, self.values))


def read_input_file():
    return open('input', 'r').read().splitlines()


def parse_input(commands: list, part: int):
    bots = defaultdict(Bot)
    outputs = defaultdict(OutputBin)

    for command in commands:
        terms = command.split()
        if terms[0] == 'value':
            bots[int(terms[5])].receive(int(terms[1]))
        else:  # terms[0] == 'bot'
            lower_dict = bots if terms[5] == 'bot' else outputs
            higher_dict = bots if terms[10] == 'bot' else outputs
            lower = lower_dict[int(terms[6])]
            higher = higher_dict[int(terms[11])]
            bots[int(terms[1])].low = lower
            bots[int(terms[1])].high = higher
            bots[int(terms[1])].check()

    if part == 1:
        return [k for k, v in bots.items() if sorted(v.values) == [17, 61]][0]
    else:  # part == 2
        return reduce(lambda a, b: a * b, [outputs[x].values[0] for x in (0, 1, 2)])


def main():
    input_data = read_input_file()
    print('Day 10 Part 1:', parse_input(input_data, part=1))
    print('Day 10 Part 2:', parse_input(input_data, part=2))


if __name__ == '__main__':
    main()
