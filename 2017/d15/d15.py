test_input = (65, 8921)
input_data = (722, 354)
factor_generator = (16807, 48271)

dividing = 2147483647
pair_range_1 = 40000000
pair_range_2 = 5000000


def generator(start_value, factor, divide):
    next_a = start_value
    while True:
        next_a = (next_a * factor) % dividing
        if next_a % divide == 0:
            yield next_a


def compareBits(a_bin, b_bin):
    return a_bin & 65535 == b_bin & 65535


def countPairs(data):
    counter = 0
    next_a = data[0]
    next_b = data[1]
    for i in range(pair_range_1):
        next_a = (next_a * factor_generator[0]) % dividing
        next_b = (next_b * factor_generator[1]) % dividing

        if compareBits(next_a, next_b):
            counter += 1

    return counter


def countPairs2(data):
    counter = 0
    generator_a = generator(data[0], factor_generator[0], 4)
    generator_b = generator(data[1], factor_generator[1], 8)

    for i in range(pair_range_2):
        next_a = next(generator_a)
        next_b = next(generator_b)

        if compareBits(next_a, next_b):
            counter += 1

    return counter


def test():
    assert countPairs(test_input) == 588
    assert countPairs2(test_input) == 309


def selectInput(is_production):
    if is_production:
        return input_data
    else:
        return test_input


def main():
    test()
    data = selectInput(True)
    print('Day 15 Part 1:', countPairs(data))
    print('Day 15 Part 2:', countPairs2(data))


if __name__ == '__main__':
    main()