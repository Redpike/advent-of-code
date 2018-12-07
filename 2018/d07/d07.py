import re
from collections import defaultdict

test_input = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.'
]

regex_pattern = r'^Step (.) must be finished before step (.) can begin.$'


def read_input():
    return open('input', 'r').read().splitlines()


def get_order_of_steps(_input: list):
    alllet = set()
    deps = defaultdict(set)
    for line in _input:
        matcher = re.match(regex_pattern, line)
        deps[matcher.group(2)].add(matcher.group(1))
        alllet.add(matcher.group(2))
        alllet.add(matcher.group(1))
    reml = sorted(alllet)
    done = set()
    order = ''
    while reml:
        for i, character in enumerate(reml):
            if not (deps[character] - done):
                order += character
                done.add(character)
                del reml[i]
                break
    return order


def test():
    assert get_order_of_steps(test_input) == 'CABDFE'


def main():
    test()
    _input = read_input()
    print('Day 07 Part 1', get_order_of_steps(_input))


if __name__ == '__main__':
    main()
