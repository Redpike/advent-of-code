from collections import defaultdict
from itertools import combinations

test_input = [
    20,
    15,
    10,
    5,
    5
]


def read_input_file():
    input_data = []
    input_file = open('input', 'r').read().splitlines()
    for line in input_file:
        input_data.append(int(line))
    return input_data


def get_amount_of_combinations(input_data, liters):
    combinations_dict = defaultdict(int)
    for i in range(len(input_data)):
        for j in combinations(input_data, i):
            if sum(j) == liters:
                combinations_dict[i] += 1
    return sum(combinations_dict.values())


def test():
    assert get_amount_of_combinations(test_input, 25) == 4


def main():
    test()
    input_data = read_input_file()
    print('Day 17 Part 1:', get_amount_of_combinations(input_data, 150))


if __name__ == '__main__':
    main()
