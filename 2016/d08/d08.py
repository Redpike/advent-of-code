import numpy

test_input = [
    'rect 3x2',
    'rotate column x=1 by 1',
    'rotate row y=0 by 4',
    'rotate column x=1 by 1'
]


def read_input_file():
    return open('input').read().splitlines()


def get_structure(input_data):
    structure = numpy.zeros(shape=(6, 50))
    for l in input_data:
        if l.startswith('rect'):
            a, b = l.split()[1].split('x')
            b, a = int(a), int(b)
            structure[:a, :b] = 1
        elif l.startswith('rotate row'):
            a, b = map(int, l.split('=')[1].split(' by '))
            a, b = int(a), int(b)
            structure[a] = numpy.roll(structure[a], b)
        elif l.startswith('rotate column'):
            a, b = map(int, l.split('=')[1].split(' by '))
            a, b = int(a), int(b)
            structure[:, a] = numpy.roll(structure[:, a], b)
    return structure


def print_text(structure):
    for row in structure:
        for column in row:
            print(".#"[int(column)], end='')
        print()
    print()


def test():
    structure = get_structure(test_input)
    assert sum(sum(structure)) == 6


def main():
    test()
    input_data = read_input_file()
    structure = get_structure(input_data)
    print('Day 8 Part 1:', int(sum(sum(structure))))
    print('Day 8 Part 2:')
    print_text(structure)


if __name__ == '__main__':
    main()
