from itertools import cycle

test_input = [
    [1, 1, 1],
    [1, 1, -2],
    [-1, -2, -3]
]

test_input_2 = [
    [1, -1],
    [3, 3, 4, -2, -4],
    [-6, 3, 8, 5, -6],
    [7, 7, -2, -7, -4]
]


def read_input():
    return [int(num) for num in open('input', 'r').read().split()]


def sum_of_frequences(input_data: list):
    return sum(input_data)


def first_frequence_reached_twice(input_data: list):
    cycled_input_data = cycle(input_data)
    _sum = 0
    _sums = {}
    for item in cycled_input_data:
        _sum += item
        if _sum not in _sums.keys():
            _sums[_sum] = 1
        else:
            return _sum


def test():
    assert sum_of_frequences(test_input[0]) == 3
    assert sum_of_frequences(test_input[1]) == 0
    assert sum_of_frequences(test_input[2]) == -6
    assert first_frequence_reached_twice(test_input[0]) == 0
    assert first_frequence_reached_twice(test_input[1]) == 10
    assert first_frequence_reached_twice(test_input[2]) == 5
    assert first_frequence_reached_twice(test_input[3]) == 14


def main():
    input_data = read_input()
    print('Day 01 Part 1:', sum_of_frequences(input_data))
    print('Day 01 Part 2:', first_frequence_reached_twice(input_data))


if __name__ == '__main__':
    main()
