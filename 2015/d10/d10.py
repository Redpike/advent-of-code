input_data = '1321131112'


def generate_new_string(_input):
    out = ''
    last = _input[0]
    count = 1
    for char in _input[1:]:
        if char != last:
            out += str(count) + last
            last = char
            count = 1
        else:
            count += 1
    out += str(count) + last
    return out


def length_of_the_result(_input, times):
    for _ in range(times):
        _input = generate_new_string(_input)
    return len(_input)


def main():
    print('Day 10 Part 1:', length_of_the_result(input_data, 40))
    print('Day 10 Part 2:', length_of_the_result(input_data, 50))


if __name__ == '__main__':
    main()
