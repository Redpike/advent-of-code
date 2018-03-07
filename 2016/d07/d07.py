import re

test_input = [
    'abba[mnop]qrst',
    'abcd[bddb]xyyx',
    'aaaa[qwer]tyui',
    'ioxxoj[asdfgh]zxcvbn'
]

test_input_2 = [
    'aba[bab]xyz',
    'xyx[xyx]xyx',
    'aaa[kek]eke',
    'zazbz[bzb]cdb'
]

tls_good_sequence_pattern = r'(\w)(\w)\2\1'
ssl_good_sequence_pattern = r'(?=(\w)(\w)\1)'
brackets_pattern = r'(?:\[|\])'


def read_input_file():
    return open('input', 'r').read().splitlines()


def is_sequence_tls(sequence: str):
    is_good = re.search(tls_good_sequence_pattern, sequence)
    if is_good and is_good.group(1) != is_good.group(2):
        return True
    else:
        return False


def is_sequence_ssl(sequence: str):
    aba_finded = re.findall(ssl_good_sequence_pattern, sequence)
    aba_filtered = list(filter(lambda i: i[0] != i[1], aba_finded))
    if len(aba_filtered) > 0:
        return aba_filtered
    else:
        return False


def is_supporting_tls(address: str):
    sequences = re.split(brackets_pattern, address)
    non_hypernet_sequences = sequences[0::2]
    hypernet_sequences = sequences[1::2]

    for seq in hypernet_sequences:
        if is_sequence_tls(seq):
            return False

    for seq in non_hypernet_sequences:
        if is_sequence_tls(seq):
            return True


def is_supporting_ssl(address: str):
    sequences = re.split(brackets_pattern, address)
    non_hypernet_sequences = sequences[0::2]
    hypernet_sequences = sequences[1::2]
    aba_list = []
    bab_list = []
    bab_inverted_list = []

    for seq in non_hypernet_sequences:
        aba = is_sequence_ssl(seq)
        if aba:
            aba_list.extend(aba)

    for seq in hypernet_sequences:
        bab = is_sequence_ssl(seq)
        if bab:
            bab_list.extend(bab)

    for bab in bab_list:
        bab_inverted_list.append((bab[1], bab[0]))

    if len(set(aba_list).intersection(set(bab_inverted_list))) > 0:
        return True
    else:
        return False



def count_tls_addresses(input_data: list):
    counter = 0
    for address in input_data:
        if is_supporting_tls(address):
            counter += 1
    return counter


def count_ssl_addresses(input_data: list):
    counter = 0
    for address in input_data:
        if is_supporting_ssl(address):
            counter += 1
    return counter


def test():
    assert count_tls_addresses(test_input) == 2
    assert count_ssl_addresses(test_input_2) == 3


def main():
    test()
    input_data = read_input_file()
    print('Day 07 Part 1:', count_tls_addresses(input_data))
    print('Day 07 Part 2:', count_ssl_addresses(input_data))


if __name__ == '__main__':
    main()
