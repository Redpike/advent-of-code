from collections import defaultdict

import re

test_input = [
    '0 <-> 2',
    '1 <-> 1',
    '2 <-> 0, 3, 4',
    '3 <-> 2, 4',
    '4 <-> 2, 3, 6',
    '5 <-> 6',
    '6 <-> 4, 5'
]

node_with_children_pattern = '^((\d+) <-> (.*))$'


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        line = line.strip('\n')
        input_data.append(line)
    return input_data


def fillDictionaryByData(input_data):
    programs = defaultdict(set)
    for line in input_data:
        regex_line = re.search(node_with_children_pattern, line)
        programs.update({int(regex_line[2]): set(int(x) for x in regex_line[3].split(', '))})
    return programs


def getGroup(programs, program_id):
    group = {program_id}
    new_group = {program_id}
    while new_group:
        next_new_group = set()
        for item in new_group:
            next_new_group.update(programs[item])
        new_group = next_new_group.difference(group)
        group.update(next_new_group)
    return group


def getRemaining(programs):
    remaining_set = set(programs)
    remaining_groups = 0
    while remaining_set:
        remaining_groups += 1
        group = getGroup(programs, remaining_set.pop())
        remaining_set = remaining_set.difference(group)
    return remaining_groups


def test():
    programs = fillDictionaryByData(test_input)
    assert len(getGroup(programs, 0)) == 6
    assert getRemaining(programs) == 2


def selectInput(is_production):
    if is_production:
        return readInputFile()
    else:
        return test_input


def main():
    test()
    input_data = selectInput(True)
    programs = fillDictionaryByData(input_data)
    print('Day 12 Part 1:', len(getGroup(programs, 0)))
    print('Day 12 Part 2:', getRemaining(programs))


if __name__ == '__main__':
    main()
