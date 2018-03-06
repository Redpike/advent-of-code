from collections import defaultdict

test_input = [
    'eedadn',
    'drvtee',
    'eandsr',
    'raavrd',
    'atevrs',
    'tsrnev',
    'sdttsa',
    'rasrtv',
    'nssdts',
    'ntnada',
    'svetve',
    'tesnvt',
    'vntsnd',
    'vrdear',
    'dvrsen',
    'enarar'
]


def read_input_file():
    return open('input', 'r').read().splitlines()


def get_error_message(input_data: list):
    transposed_data = list(zip(*input_data))
    error_message = ''
    for text in transposed_data:
        ranking_dict = defaultdict(str)
        for char in text:
            ranking_dict[char] = text.count(char)
        error_message += max(ranking_dict.keys(), key=lambda k: ranking_dict[k])
    return error_message


def test():
    assert get_error_message(test_input) == 'easter'


def main():
    test()
    input_data = read_input_file()
    print('Day 06 Part 1:', get_error_message(input_data))


if __name__ == '__main__':
    main()
