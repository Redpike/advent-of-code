import re
from functools import reduce

test_input = [
    '5-8',
    '0-2',
    '4-7'
]

regex_pattern = r'(\d+)-(\d+)'
total = 2 ** 32


def read_input_file():
    return open('input', 'r').read().splitlines()


def contains(range, value):
    if isinstance(value, tuple):
        return range[0] <= value[0] and value[1] <= range[1]
    else:
        return range[0] <= value <= range[1]


def make_reducer(acc, span: tuple):
    if contains(acc[0], span):
        return acc
    elif contains(acc[0], span[0]) or span[0] == acc[0][1] + 1:
        return [(acc[0][0], span[1])] + acc[1:]
    else:
        return [span] + acc


def get_spans(input_data: list):
    spans = []
    for block_item in input_data:
        regex_matcher = re.match(regex_pattern, block_item)
        left_ip, right_ip = int(regex_matcher.group(1)), int(regex_matcher.group(2))
        spans.append((left_ip, right_ip))
    return spans


def merge_spans(spans: list):
    spans = sorted(spans, key=lambda x: x[0])
    reducer = make_reducer
    reduced_spans = reduce(reducer, spans, [spans[0]])[::-1]
    return reduced_spans


def get_the_lowest_valued_ip(input_data: list):
    spans = get_spans(input_data)
    reduced_spans = merge_spans(spans)
    return reduced_spans


def count_allowed_ip(spans: list):
    total_unblocked = total
    for start, end in spans:
        total_unblocked -= (end - start + 1)
    return total_unblocked


def test():
    reduces_spans = get_the_lowest_valued_ip(test_input)
    assert reduces_spans[0][1] == 2


def main():
    test()
    input_data = read_input_file()
    reduced_spans = get_the_lowest_valued_ip(input_data)
    print('Day 20 Part 1:', reduced_spans[0][1] + 1)
    print('Day 20 Part 2:', count_allowed_ip(reduced_spans))


if __name__ == '__main__':
    main()
