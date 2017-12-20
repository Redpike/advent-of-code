from collections import defaultdict

parts = defaultdict()


class Particle(object):
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def nextStep(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]

    def distance(self):
        return sum([abs(position) for position in self.p])


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        line = line.strip('\n')
        input_data.append(line)
    return input_data


def parseParticle(line, index):
    ts = line.strip().split(", ")
    positions = [int(x) for x in ts[0].split("=")[1][1:-1].split(",")]
    velocities = [int(x) for x in ts[1].split("=")[1][1:-1].split(",")]
    accelerations = [int(x) for x in ts[2].split("=")[1][1:-1].split(",")]
    parts[index] = Particle(positions, velocities, accelerations)


def getClosest(input_data):
    for index in range(len(input_data)):
        parseParticle(input_data[index], index)
    while True:
        min_d = None
        min_part = None
        for i, part in parts.items():
            part.nextStep()
            if min_d is None or part.distance() < min_d:
                min_part = i
                min_d = part.distance()
        print(min_part)


def getParticles(input_data):
    for index in range(len(input_data)):
        parseParticle(input_data[index], index)
    while True:
        min_d = None
        min_part = None
        for i, part in parts.items():
            part.nextStep()
            if min_d is None or part.distance() < min_d:
                min_part = i
                min_d = part.distance()

        if True:
            pos_dict = defaultdict(list)
            for i, part in parts.items():
                k = tuple(part.p)
                pos_dict[k].append(i)

            for k, v in pos_dict.items():
                if len(v) > 1:
                    for i in v:
                        del parts[i]
            print(len(parts))


def selectPart(input_data, part):
    if part == 1:
        print('Day 20 Part 1:', getClosest(input_data))
    else:
        print('Day 20 Part 2:', getParticles(input_data))


def main():
    input_data = readInputFile()
    selectPart(input_data, 1)


if __name__ == '__main__':
    main()
