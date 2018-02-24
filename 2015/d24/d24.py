import operator
from functools import reduce
from itertools import combinations

test_input = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]


def read_input_file():
    input_file = open('input').read()
    packages = [int(package) for package in input_file.splitlines()]
    return packages


def get_right_balance(input_data, division):
    group_size = sum(input_data)
    weight = group_size // division

    for i in range(len(input_data)):
        quantum_entanglements = [reduce(operator.mul, comb) for comb in combinations(input_data, i) if sum(comb) == weight]
        if quantum_entanglements:
            return min(quantum_entanglements)


def test():
    assert get_right_balance(test_input, 3) == 99


def main():
    test()
    input_data = read_input_file()
    print('Day 24 Part 1:', get_right_balance(input_data, 3))
    print('Day 24 Part 2:', get_right_balance(input_data, 4))


if __name__ == '__main__':
    main()
