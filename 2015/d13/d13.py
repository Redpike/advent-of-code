import re
from collections import defaultdict
from itertools import permutations

test_input = [
    'Alice would gain 54 happiness units by sitting next to Bob.',
    'Alice would lose 79 happiness units by sitting next to Carol.',
    'Alice would lose 2 happiness units by sitting next to David.',
    'Bob would gain 83 happiness units by sitting next to Alice.',
    'Bob would lose 7 happiness units by sitting next to Carol.',
    'Bob would lose 63 happiness units by sitting next to David.',
    'Carol would lose 62 happiness units by sitting next to Alice.',
    'Carol would gain 60 happiness units by sitting next to Bob.',
    'Carol would gain 55 happiness units by sitting next to David.',
    'David would gain 46 happiness units by sitting next to Alice.',
    'David would lose 7 happiness units by sitting next to Bob.',
    'David would gain 41 happiness units by sitting next to Carol.'
]

regex_pattern = r'(\w+) would (\w+) (-?\d+) h.*to (\w+)'


def read_input_file():
    return open('input', 'r').read().splitlines()


def parse_line(line):
    regex_match = re.match(regex_pattern, line)
    guset1, gain_lose_flag, hap, guest2 = regex_match.group(1), regex_match.group(2), int(
        regex_match.group(3)), regex_match.group(4)
    if gain_lose_flag == 'lose':
        hap = -hap

    return guset1, guest2, int(hap)


def fill_guest_map(input_data, part):
    guests = defaultdict(defaultdict)
    for line in input_data:
        guest1, guest2, hap = parse_line(line)
        guests[guest1][guest2] = hap
        if part == 2:
            me = 'Redpike'
            guests[me][guest2] = 0
            guests[guest1][me] = 0

    return guests


def get_the_best_config(guests_map):
    seating_happiness = []
    for seating in permutations(guests_map.keys()):
        happiness = 0
        for seat1, seat2 in zip(seating, seating[1:] + seating[:1]):
            happiness += guests_map[seat1][seat2] + guests_map[seat2][seat1]
            seating_happiness.append(happiness)

    return max(seating_happiness)


def find_total_change_in_happiness(input_data, part):
    guests = fill_guest_map(input_data, part)
    the_best_happiness = get_the_best_config(guests)

    return the_best_happiness


def test():
    assert find_total_change_in_happiness(test_input, 1) == 330


def main():
    test()
    input_data = read_input_file()
    print('Day 13 Part 1:', find_total_change_in_happiness(input_data, 1))
    print('Day 13 Part 2:', find_total_change_in_happiness(input_data, 2))


if __name__ == '__main__':
    main()
