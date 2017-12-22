test_input = [
    '.........',
    '.........',
    '.........',
    '.....#...',
    '...#.....',
    '.........',
    '.........',
    '.........'
]

directions = [
    (-1, 0),    # UP
    (0, -1),    # LEFT
    (1, 0),     # DOWN
    (0, 1)      # RIGHT
]

# Flags for part 2
CLEAN = 'C'
INFECTED = "I"
WEAK = 'W'
FLAGGED = 'F'


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        line = line.strip('\n')
        input_data.append(line)
    return input_data


def getInfected(input_data):
    infected = set()
    offset = len(input_data) // 2
    for y in range(len(input_data)):
        for x in range(len(input_data)):
            if input_data[y][x] == '#':
                infected.add((y - offset, x - offset))
    return infected


def countBursts(input_data):
    d, counter = 0, 0
    virus_cords = (0, 0)
    infected = getInfected(input_data)
    for _ in range(10000):
        if virus_cords in infected:
            d = (d - 1) % 4
            infected.remove(virus_cords)
        else:
            d = (d + 1) % 4
            infected.add(virus_cords)
            counter += 1
        virus_cords = (virus_cords[0] + directions[d][0], virus_cords[1] + directions[d][1])
    return counter


def countBursts2(input_data):
    d, counter = 0, 0
    virus_cords = (0, 0)
    infected = getInfected(input_data)
    states = {k: INFECTED for k in infected}
    for _ in range(10000000):
        current_state = states.get(virus_cords, 'C')
        if current_state == CLEAN:
            d = (d + 1) % 4
            states[virus_cords] = WEAK
        elif current_state == WEAK:
            states[virus_cords] = INFECTED
            counter += 1
        elif current_state == INFECTED:
            d = (d - 1) % 4
            states[virus_cords] = FLAGGED
        elif current_state == FLAGGED:
            d = (d + 2) % 4
            del states[virus_cords]
        virus_cords = (virus_cords[0] + directions[d][0], virus_cords[1] + directions[d][1])
    return counter


def test():
    assert countBursts(test_input) == 5587
    assert countBursts2(test_input) == 2511944


def main():
    test()
    input_data = readInputFile()
    print('Day 22 Part 1:', countBursts(list(input_data)))
    print('Day 22 Part 2:', countBursts2(list(input_data)))


if __name__ == '__main__':
    main()
