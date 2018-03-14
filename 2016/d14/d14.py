import re
import functools
from hashlib import md5

test_input = 'abc{}'
input_data = 'yjdafjpo{}'
regex = re.compile(r'([abcdef0-9])\1{2}')


@functools.lru_cache(maxsize=None)
def get_md5(string: str):
    return md5(string.encode()).hexdigest()


@functools.lru_cache(maxsize=None)
def get_long_md5(string: str):
    for _ in range(2017):
        string = md5(string.encode()).hexdigest()
    return string


def get_index(salt: str, long=False):
    md5_function = get_long_md5 if long else get_md5
    i = 0
    j = 0
    while True:
        is_found = re.search(regex, md5_function(salt.format(i)))
        if is_found:
            check = is_found.group()[0] * 5
            if any(check in md5_function(salt.format(j)) for j in range(i + 1, i + 1001)):
                j += 1
                if j == 64:
                    return i
        i += 1


def test():
    assert get_index(test_input) == 22728


def main():
    test()
    print('Day 14 Part 1:', get_index(input_data))
    print('Day 14 Part 1:', get_index(input_data, long=True))


if __name__ == '__main__':
    main()
