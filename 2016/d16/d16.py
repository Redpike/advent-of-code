test_input = '10000'
input_data = '01110110101001000'


def next_string(string: str):
    b = ''.join('0' if char == '1' else '1' for char in reversed(string))
    return '{}0{}'.format(string, b)


def generate(start_string: str, length: int):
    while len(start_string) < length:
        start_string = next_string(start_string)
    return start_string[:length]


def checksum(string: str):
    crc = []
    for a, b in zip(string[::2], string[1::2]):
        if a == b:
            crc.append('1')
        else:
            crc.append('0')
    if len(crc) % 2 != 0:
        return ''.join(crc)
    else:
        return checksum(''.join(crc))


def test():
    assert checksum(generate(test_input, 20)) == '01100'


def main():
    test()
    print('Day 16 Part 1:', checksum(generate(input_data, 272)))
    print('Day 16 Part 2:', checksum(generate(input_data, 35651584)))


if __name__ == '__main__':
    main()
