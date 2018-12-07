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


def get_order_of_steps(_input: list, part: int):
    alllet = set()
    deps = defaultdict(set)
    for line in _input:
        matcher = re.match(regex_pattern, line)
        deps[matcher.group(2)].add(matcher.group(1))
        alllet.add(matcher.group(2))
        alllet.add(matcher.group(1))
    reml = sorted(alllet)
    done = set()
    done_time = {}
    busy_until = [0, 0, 0, 0, 0]
    time = 0
    order = ''
    if part == 1:
        while reml:
            for i, character in enumerate(reml):
                if not (deps[character] - done):
                    order += character
                    done.add(character)
                    del reml[i]
                    break
        return order
    elif part == 2:
        while reml:
            if all(t > time for t in busy_until):
                time = min(busy_until)
            for i, c in enumerate(reml):
                if all(d in done_time and done_time[d] <= time for d in deps[c]):
                    order += c
                    for ib, b in enumerate(busy_until):
                        if b <= time:
                            busy_until[ib] = time + 60 + ord(c) - 64
                            done_time[c] = busy_until[ib]
                            break
                    del reml[i]
                    break
            else:
                time = min(t for t in busy_until if t > time)
        return max(busy_until)


def test():
    assert get_order_of_steps(test_input, 1) == 'CABDFE'


def main():
    test()
    _input = read_input()
    print('Day 07 Part 1', get_order_of_steps(_input, 1))
    print('Day 07 Part 2', get_order_of_steps(_input, 2))


if __name__ == '__main__':
    main()
