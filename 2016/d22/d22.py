import re
from itertools import combinations


def read_input_file():
    return open('input', 'r').read().splitlines()


def parse_data(input_data: list):
    nodes = {}
    for line in input_data:
        if line[0] != '/':
            continue
        x, y, size, used, avail, perc = map(int, re.findall(r'(\d+)', line))
        nodes[(x, y)] = {'used': used, 'avail': avail}
    return nodes


def count_viable_pairs(input_data: list):
    counter = 0
    nodes = parse_data(input_data)
    values = nodes.values()
    for comb in combinations(values, 2):
        if comb[0]['used'] != 0 and comb[0]['used'] <= comb[1]['avail']:
            counter += 1
        if comb[1]['used'] != 0 and comb[1]['used'] <= comb[0]['avail']:
            counter += 1
    return counter


def main():
    input_data = read_input_file()
    print('Day 22 Part 1:', count_viable_pairs(input_data))


if __name__ == '__main__':
    main()
