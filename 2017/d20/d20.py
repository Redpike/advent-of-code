from collections import defaultdict

test_input = [
    'p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>',
    'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>',
    'p=< 4,0,0>, v=< 1,0,0>, a=<-1,0,0>',
    'p=< 2,0,0>, v=<-2,0,0>, a=<-2,0,0>',
    'p=< 4,0,0>, v=< 0,0,0>, a=<-1,0,0>',
    'p=<-2,0,0>, v=<-4,0,0>, a=<-2,0,0>',
    'p=< 3,0,0>, v=<-1,0,0>, a=<-1,0,0>',
    'p=<-8,0,0>, v=<-6,0,0>, a=<-2,0,0>'
]


class Particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        line = line.strip('\n')
        input_data.append(line)
    return input_data


def getTokens(tokens_in_line):
    position_in_line = tokens_in_line[0][3:-2].split(',')
    velocity_in_line = tokens_in_line[1][3:-2].split(',')
    acceleration_in_line = tokens_in_line[2][3:-2].split(',')
    return position_in_line, velocity_in_line, acceleration_in_line


def getClosest(input_data):
    index = 0
    position = defaultdict(int)
    velocity = defaultdict(int)
    acceleration = defaultdict(int)
    for line in input_data:
        tokens_in_line = line.split()
        position_in_line, velocity_in_line, acceleration_in_line = getTokens(tokens_in_line)


def test():
    pass


def main():
    test()
    input_data = readInputFile()
    print('Day 20 Part 1:', getClosest(input_data))
    print('Day 20 Part 2:', )


if __name__ == '__main__':
    main()
