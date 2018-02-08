import re

test_input = [
    '""',
    '"abc"',
    '"aaa\\"aaa"',
    '"\\x27"'
]


def readInputFile():
    return open('input', 'r').read().splitlines()


def get_number_of_chars(line):
    return len(eval(line))


def count_chars(input_data):
    total, in_memory, new_encoded = 0, 0, 0

    for line in input_data:
        total += len(line)
        in_memory += get_number_of_chars(line)
        new_encoded += len(re.escape(line)) + 2

    return total, in_memory, new_encoded


def substract(total, in_memory):
    return total - in_memory


def test():
    total, in_memory, new_encoded = count_chars(test_input)
    assert substract(total, in_memory) == 12
    assert substract(new_encoded, total) == 19


def main():
    test()
    input_data = readInputFile()
    total, in_memory, new_encoded = count_chars(input_data)
    print('Day 08 Part 1:', substract(total, in_memory))
    print('Day 08 Part 2:', substract(new_encoded, total))


if __name__ == '__main__':
    main()
