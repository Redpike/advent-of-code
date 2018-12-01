test_input = [
    [1, 1, 1],
    [1, 1, -2],
    [-1, -2, -3]
]


def read_input():
    return [int(num) for num in open('input', 'r').read().split()]


def sum_of_frequences(input_data: list):
    print(input_data)
    return sum(input_data)


def test():
    assert sum_of_frequences(test_input[0]) == 3
    assert sum_of_frequences(test_input[1]) == 0
    assert sum_of_frequences(test_input[2]) == -6


def main():
    input_data = read_input()
    print('Day 01 Part 1:', sum_of_frequences(input_data))


if __name__ == '__main__':
    main()
