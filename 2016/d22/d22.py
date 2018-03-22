import re
from itertools import combinations

test_input = [
    'Filesystem            Size  Used  Avail  Use%',
    '/dev/grid/node-x0-y0   10T    8T     2T   80%',
    '/dev/grid/node-x0-y1   11T    6T     5T   54%',
    '/dev/grid/node-x0-y2   32T   28T     4T   87%',
    '/dev/grid/node-x1-y0    9T    7T     2T   77%',
    '/dev/grid/node-x1-y1    8T    0T     8T    0%',
    '/dev/grid/node-x1-y2   11T    7T     4T   63%',
    '/dev/grid/node-x2-y0   10T    6T     4T   60%',
    '/dev/grid/node-x2-y1    9T    8T     1T   88%',
    '/dev/grid/node-x2-y2    9T    6T     3T   66%'
]


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


def count_viable_pairs(nodes: dict):
    counter = 0
    values = nodes.values()
    for comb in combinations(values, 2):
        if comb[0]['used'] != 0 and comb[0]['used'] <= comb[1]['avail']:
            counter += 1
        if comb[1]['used'] != 0 and comb[1]['used'] <= comb[0]['avail']:
            counter += 1
    return counter


def find_path_to_goal(nodes: dict, start, end, obst=None):
    lx = max([val[0] for val in nodes.keys()]) + 1
    ly = max([val[1] for val in nodes.keys()]) + 1
    for value in nodes.values():
        value['dist'] = float('inf')
        value['prev'] = None
    queue = [start]
    nodes[start]['dist'] = 0
    while len(queue) > 0:
        n = queue.pop(0)
        for x, y in [(n[0] + 1, n[1]), (n[0] - 1, n[1]), (n[0], n[1] + 1), (n[0], n[1] - 1)]:
            if 0 <= x < lx and 0 <= y < ly and nodes[(x, y)]['used'] < 100 and (x, y) != obst:
                if nodes[(x, y)]['dist'] > nodes[n]['dist'] + 1:
                    nodes[(x, y)]['dist'] = nodes[n]['dist'] + 1
                    nodes[(x, y)]['prev'] = n
                    queue.append((x, y))
                if (x, y) == end:
                    path = [(x, y)]
                    while nodes[path[-1]]['prev'] is not None:
                        path.append(nodes[path[-1]]['prev'])
                    return path[-2::-1]


def get_fewest_number_of_steps(nodes: dict):
    lx = max([val[0] for val in nodes.keys()]) + 1
    start = (0, 0)
    goal = (lx - 1, 0)
    empty = (None, None)
    for key in nodes:
        if nodes[key]['used'] == 0:
            empty = key
            break
    path_gs = find_path_to_goal(nodes, goal, start)
    counter = 0
    while goal != start:
        path_ = find_path_to_goal(nodes, empty, path_gs.pop(0), obst=goal)
        counter += len(path_) + 1
        empty = goal
        goal = path_[-1]
    return counter


def test():
    nodes = parse_data(test_input)
    assert get_fewest_number_of_steps(nodes) == 7


def main():
    test()
    input_data = read_input_file()
    nodes = parse_data(input_data)
    print('Day 22 Part 1:', count_viable_pairs(nodes))
    print('Day 22 Part 2:', get_fewest_number_of_steps(nodes))


if __name__ == '__main__':
    main()
