import hashlib

input_data = 'reyedfim'
test_input = 'abc'


def generate_password(_data):
    counter = 0
    password = ''
    while len(password) < 8:
        input_with_zero = _data + str(counter)
        input_bytes = input_with_zero.encode()
        md5 = hashlib.md5()
        md5.update(input_bytes)
        hashed = md5.hexdigest()
        if hashed[:5] == '00000':
            password += hashed[5]
        counter += 1
    return password


def test():
    assert generate_password(test_input) == '18f47a30'


def main():
    test()
    print('Day 05 Part 1:', generate_password(input_data))
    print('Day 05 Part 2:', )


if __name__ == '__main__':
    main()
