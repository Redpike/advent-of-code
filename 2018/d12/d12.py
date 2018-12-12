def read_input():
    return open('input', 'r').read().splitlines()


def parse_data(_input: list):
    state = _input[0].split(': ')[1]
    plants = [i for i, c in enumerate(state) if c == "#"]
    rules = dict((line[:5], line[9] == "#") for line in _input[2:])
    return plants, rules


def get_amount_of_plants(_input: list, generations: int):
    plants, rules = parse_data(_input)
    for generation in range(generations):
        lowest_plant = min(plants)
        highest_plant = max(plants)
        last_possible = highest_plant - lowest_plant + 7
        pots = ''.join(['#' if i in plants
                        else '.' for i in range(lowest_plant - 4, highest_plant + 5)])
        plants = []
        for i in range(2, last_possible):
            possible_key = pots[i - 2: i + 3]
            if rules[possible_key]:
                plants.append(i - 4 + lowest_plant)
    return sum(plants)


def main():
    _input = read_input()
    print('Day 12 Part 1:', get_amount_of_plants(_input, 20))
    score_199 = get_amount_of_plants(_input, 199)
    score_200 = get_amount_of_plants(_input, 200)
    constant_increase = score_200 - score_199
    print('Day 12 Part 2:', get_amount_of_plants(_input,  200) + ((50000000000 - 200) * constant_increase))


if __name__ == '__main__':
    main()
