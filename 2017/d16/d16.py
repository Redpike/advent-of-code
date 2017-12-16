from collections import deque

test_programs = deque('abcde')
test_instructions = ['s1', 'x3/4', 'pe/b']
input_programs = deque('abcdefghijklmnop')
iterations = 1000000000


def readInputFile():
    with open('input') as input_file:
        instructions = input_file.readline().split(',')

    return instructions


def dance(programs, instructions):
    for instruction in instructions:
        if instruction.startswith('s'):
            root = int(instruction[1:])
            programs.rotate(root)
        elif instruction.startswith('x'):
            a, b = map(int, instruction[1:].split('/'))
            programs[a], programs[b] = programs[b], programs[a]
        elif instruction.startswith('p'):
            x, y = instruction[1:].split('/')
            a = programs.index(x)
            b = programs.index(y)
            programs[a], programs[b] = programs[b], programs[a]
    return ''.join(programs)


def dance2(cycles, programs, instructions):
    for i in range(cycles):
        for instruction in instructions:
            if instruction.startswith('s'):
                root = int(instruction[1:])
                programs.rotate(root)
            elif instruction.startswith('x'):
                a, b = map(int, instruction[1:].split('/'))
                programs[a], programs[b] = programs[b], programs[a]
            elif instruction.startswith('p'):
                x, y = instruction[1:].split('/')
                a = programs.index(x)
                b = programs.index(y)
                programs[a], programs[b] = programs[b], programs[a]
        if programs == input_programs:
            return i + 1
    return ''.join(programs)


def test():
    assert dance(test_programs, test_instructions) == 'baedc'
    assert dance(deque('baedc'), test_instructions) == 'ceadb'


def main():
    test()
    instructions = readInputFile()
    print('Day 16 Part 1:', dance(deque(input_programs), instructions))
    cycle = dance2(iterations, deque(input_programs), instructions)
    next_cycle = iterations % cycle
    print('Day 16 Part 2:', dance2(next_cycle, deque(input_programs), instructions))


if __name__ == '__main__':
    main()
