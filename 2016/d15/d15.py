import re

test_input = [
    'Disc #1 has 5 positions; at time=0, it is at position 4.'
    'Disc #2 has 2 positions; at time=0, it is at position 1.'
]

regex_pattern = r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)'


class Disc(object):
    def __init__(self, disc_id: int, positions: int, position: int):
        self.disc_id = disc_id
        self.positions = positions
        self.position = position

    def __repr__(self):
        return 'Disc #{}, positions: {}, current position: {}'.format(self.disc_id, self.positions, self.position)

    def get_state_at(self, time: int):
        return (self.position + time) % self.positions


def read_input_file():
    return open('input', 'r').read().splitlines()


def parse_data(input_data: list):
    discs = []
    for line in input_data:
        regex_matcher = re.match(regex_pattern, line)
        disc = Disc(*map(int, regex_matcher.group(1, 2, 3)))
        discs.append(disc)
    return discs


def parse_data_2(input_data: list):
    discs = []
    for line in input_data:
        regex_matcher = re.match(regex_pattern, line)
        disc = Disc(*map(int, regex_matcher.group(1, 2, 3)))
        discs.append(disc)
    disc = Disc(7, 11, 0)
    discs.append(disc)
    return discs


def is_done(discs: list, time: int):
    return all(disc.get_state_at(time + index + 1) == 0 for (index, disc) in enumerate(discs))


def get_a_capsule(discs: list):
    time = 0
    while not is_done(discs, time):
        time += 1
    return time


def test():
    discs = parse_data(test_input)
    assert get_a_capsule(discs) == 0


def main():
    test()
    input_file = read_input_file()
    discs = parse_data(input_file)
    print('Day 15 Part 1:', get_a_capsule(discs))
    discs = parse_data_2(input_file)
    print('Day 15 Part 2:', get_a_capsule(discs))


if __name__ == '__main__':
    main()
