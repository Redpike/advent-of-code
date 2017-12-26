from collections import defaultdict

L, R = (-1, 1)

test_input = {
    'A': ((1, R, 'B'), (0, L, 'B')),
    'B': ((1, L, 'A'), (1, R, 'A'))
}


def readInputFile():
    states = {
        'A': ((1, R, 'B'), (0, L, 'C')),
        'B': ((1, L, 'A'), (1, R, 'D')),
        'C': ((0, L, 'B'), (0, L, 'E')),
        'D': ((1, R, 'A'), (0, R, 'B')),
        'E': ((1, L, 'F'), (1, L, 'C')),
        'F': ((1, R, 'D'), (1, R, 'A')),
    }
    return states


def computeChecksum(input_data, steps):
    tape = defaultdict(int)
    state = 'A'
    cursor = 0
    for i in range(steps):
        current_value = tape[cursor]
        write, move, next_state = input_data[state][current_value]
        if write:
            tape[cursor] = write
        else:
            del tape[cursor]
        cursor += move
        state = next_state
    return len(tape)


def test():
    assert computeChecksum(test_input, 6) == 3


def main():
    test()
    input_data = readInputFile()
    print('Day 25 Part 1:', computeChecksum(input_data, 12481997))
    print('Day 25 Part 2:', 'Merry Christmas!')


if __name__ == '__main__':
    main()
