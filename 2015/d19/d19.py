from collections import defaultdict

test_input = {
    'H': ['HO', 'OH'],
    'O': ['HH']
}

test_input2 = {
    'e': ['H', 'O'],
    'H': ['HO', 'OH'],
    'O': ['HH']
}


def read_input_file():
    return open('input', 'r').read().splitlines()


def convert_input_data(input_data):
    replacement_dict = defaultdict(list)
    for line in input_data:
        if line != input_data[-1] and line != '':
            splitted_line = line.split(' => ')
            replacement_dict[splitted_line[0]].append(splitted_line[1])
    return replacement_dict


def convert_molecules(string, replacement_dict):
    molecules = set()
    for i, char in enumerate(string):
        if char in replacement_dict:
            for replacement in replacement_dict[char]:
                molecules.add(string[:i] + replacement + string[i + 1:])
        else:
            for replacement in replacement_dict[string[i: i + 2]]:
                molecules.add(string[:i] + replacement + string[i + 2:])

    return len(molecules)


def test():
    assert convert_molecules('HOH', test_input) == 4


def main():
    test()
    input_data = read_input_file()
    replacement_dict = convert_input_data(input_data)
    print('Day 19 Part 1:', convert_molecules(input_data[-1], replacement_dict))


if __name__ == '__main__':
    main()
