import hashlib

input_data = 'bgvyzdsv'

test_input = [
    'abcdef',
    'pqrstuv'
]


def getHash(data, part):
    counter = 0
    while True:
        input_with_zero = data + str(counter)
        input_bytes = input_with_zero.encode()
        md5 = hashlib.md5()
        md5.update(input_bytes)
        hashed = md5.hexdigest()
        if part == 1 and hashed[:5] == '00000':
            return counter
        if part == 2 and hashed[:6] == '000000':
            return counter
        counter += 1


def test():
    assert getHash(test_input[0], 1) == 609043
    assert getHash(test_input[1], 1) == 1048970


def main():
    test()
    print('Day 04 Part 1:', getHash(input_data, 1))
    print('Day 04 Part 2:', getHash(input_data, 2))


if __name__ == '__main__':
    main()
