from collections import defaultdict

input_data = 29_000_000
test_input = 150


def get_the_lowest_house_number(_input, loops):
    houses = defaultdict(int)

    for elf in range(1, _input):
        for house in range(elf, loops, elf):
            houses[house] += (elf * 10)
        if houses[elf] >= _input:
            return elf


def get_the_lowest_house_number_2(_input, loops):
    houses = defaultdict(int)

    for elf in range(1, _input):
        for house in range(elf, min(elf * 50 + 1, loops), elf):
            houses[house] += (elf * 11)
        if houses[elf] >= _input:
            return elf


def test():
    assert get_the_lowest_house_number(140, 70) == 8
    assert get_the_lowest_house_number_2(140, 70) == 8


def main():
    test()
    loops = 1_000_000
    print('Day 20 Part 1:', get_the_lowest_house_number(input_data, loops))
    print('Day 20 Part 2:',get_the_lowest_house_number_2(input_data, loops))


if __name__ == '__main__':
    main()
