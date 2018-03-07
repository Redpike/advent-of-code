import re

test_input = [
    'abba[mnop]qrst',
    'abcd[bddb]xyyx',
    'aaaa[qwer]tyui',
    'ioxxoj[asdfgh]zxcvbn'
]

good_sequence_pattern = r'(\w)(\w)\2\1'
brackets_pattern = r'(?:\[|\])'


def read_input_file():
    return open('input', 'r').read().splitlines()


def is_sequence_good(sequence: str):
    is_good = re.search(good_sequence_pattern, sequence)
    if is_good and is_good.group(1) != is_good.group(2):
        return True
    else:
        return False


def is_supporting_tls(address: str):
    sequences = re.split(brackets_pattern, address)
    non_hypernet_sequences = sequences[0::2]
    hypernet_sequences = sequences[1::2]

    for seq in hypernet_sequences:
        if is_sequence_good(seq):
            return False

    for seq in non_hypernet_sequences:
        if is_sequence_good(seq):
            return True


def count_tls_addresses(input_data: list):
    counter = 0
    for address in input_data:
        if is_supporting_tls(address):
            counter += 1
    return counter


def test():
    assert count_tls_addresses(test_input) == 2


def main():
    test()
    input_data = read_input_file()
    print('Day 07 Part 1:', count_tls_addresses(input_data))


if __name__ == '__main__':
    main()
