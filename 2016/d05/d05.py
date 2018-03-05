import hashlib
from string import digits

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


def generate_password_2(_data):
    password = list('________')
    counter = 0
    while '_' in password:
        input_with_zero = _data + str(counter)
        input_bytes = input_with_zero.encode()
        md5 = hashlib.md5()
        md5.update(input_bytes)
        hashed = md5.hexdigest()
        if hashed[:5] == '00000':
            if hashed[5] in digits and int(hashed[5]) < 8:
                if password[int(hashed[5])] == '_':
                    password[int(hashed[5])] = hashed[6]
        counter += 1
    return ''.join(password)


def test():
    assert generate_password(test_input) == '18f47a30'
    assert generate_password_2(test_input) == '05ace8e3'


def main():
    test()
    print('Day 05 Part 1:', generate_password(input_data))
    print('Day 05 Part 2:', generate_password_2(input_data))


if __name__ == '__main__':
    main()
