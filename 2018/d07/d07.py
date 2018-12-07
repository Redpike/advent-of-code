test_input = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.'
]


def read_input():
    return open('input', 'r').read().splitlines()


def get_order_of_steps(_input: list):
    pass


def test():
    assert get_order_of_steps(test_input) == 'CABDFE'


def main():
    test()
    _input = read_input()
    print('Day 07 Part 1', get_order_of_steps(_input))


if __name__ == '__main__':
    main()
