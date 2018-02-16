import re

tape = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

regex_pattern = r'Sue \d+: ([a-z]+): (\d+), ([a-z]+): (\d+), ([a-z]+): (\d+)'


def read_input_file():
    return open('input', 'r').read().splitlines()


def parse_aunt_data(input_data):
    aunts = []
    for line in input_data:
        regex_match = re.match(regex_pattern, line)
        attribute1, value1, attribute2, value2, attribute3, value3 = regex_match.group(1, 2, 3, 4, 5, 6)
        value1, value2, value3 = int(value1), int(value2), int(value3)
        aunts.append({attribute1: value1, attribute2: value2, attribute3: value3})
    return aunts


def compare(aunt):
    return all(tape[i] == value for i, value in aunt.items())


def get_aunt(input_data):
    aunts = parse_aunt_data(input_data)
    good_aunts = [i + 1 for i, aunt in enumerate(aunts) if compare(aunt)]
    return good_aunts[0]


def main():
    input_data = read_input_file()
    print('Day 16 Part 1:', get_aunt(input_data))
    print('Day 16 Part 2:', )


if __name__ == '__main__':
    main()
