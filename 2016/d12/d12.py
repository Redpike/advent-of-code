test_input = [
    'cpy 41 a',
    'inc a',
    'inc a',
    'dec a',
    'jnz a 2',
    'dec a'
]

registers = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0
}

registers_2 = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}


def read_input_file():
    return open('input', 'r').read().splitlines()


def value(key, dic):
    return dic[key] if key in dic else int(key)


def execute_assembunny_code(input_data: list, registers_dict: dict):
    ind = 0
    while ind != len(input_data):
        splitted_line = input_data[ind].split(' ')

        if splitted_line[0] == 'inc':
            registers_dict[splitted_line[1]] += 1
        elif splitted_line[0] == 'dec':
            registers_dict[splitted_line[1]] -= 1
        elif splitted_line[0] == 'cpy':
            registers_dict[splitted_line[2]] = value(splitted_line[1], registers_dict)
        elif splitted_line[0] == 'jnz' and value(splitted_line[1], registers_dict) != 0:
            ind += int(splitted_line[2])
            continue
        ind += 1


def test():
    execute_assembunny_code(test_input, registers)
    assert registers['a'] == 42


def main():
    test()
    input_data = read_input_file()
    execute_assembunny_code(input_data, registers)
    print('Day 12 Part 1:', registers['a'])
    execute_assembunny_code(input_data, registers_2)
    print('Day 12 Part 2:', registers_2['a'])


if __name__ == '__main__':
    main()
