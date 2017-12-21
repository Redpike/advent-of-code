test_input = [
    '../.# => ##./#../...',
    '.#./..#/### => #..#/..../..../#..#'
]

pattern = (
    '.#.',
    '..#',
    '###'
)


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        line = line.strip('\n')
        input_data.append(line)
    return input_data


def getRulesFromInput(input_data):
    rules = {}
    for line in input_data:
        _in, _out = line.split(' => ')
        _in = tuple(_in.split('/'))
        _out = tuple(_out.split('/'))
        for rule in rotateAndFlip(_in):
            rules[rule] = tuple(_out)
    return rules


def rotate(rule):
    result = []
    for x in range(len(rule)):
        single_line = []
        for y in range(len(rule)):
            single_line.append(rule[len(rule) - y - 1][x])
        single_line = ''.join(tuple(single_line))
        result.append(single_line)
    return tuple(result)


def flip(rule):
    return tuple(''.join(reversed(line)) for line in rule)


def rotateAndFlip(rule):
    result = set()
    result.add(rule)
    result.add(rotate(rule))
    result.add(rotate(rotate(rule)))
    result.add(rotate(rotate(rotate(rule))))
    for rule in tuple(result):
        result.add(flip(rule))
    return result


def makeSubgrid(grid, x, y, divine):
    result = []
    for yi in range(y * divine, y * divine + divine):
        line = ''
        for xi in range(x * divine, x * divine + divine):
            line += grid[yi][xi]
        result.append(line)
    return tuple(result)


def doIteration(grid, rules, divine):
    result = []
    for x in range(int(len(grid) / divine)):
        for y in range(int(len(grid) / divine)):
            subgrid = makeSubgrid(grid, x, y, divine)
            new_subgrid = rules[subgrid]
            for counter, line in enumerate(new_subgrid):
                if y * len(new_subgrid) + counter >= len(result):
                    result.append('')
                result[y * len(new_subgrid) + counter] += line
    return result


def generateNewGrid(grid, rules):
    new_grid = []
    if len(grid) % 2 == 0:
        new_grid = doIteration(grid, rules, 2)
    elif len(grid) % 3 == 0:
        new_grid = doIteration(grid, rules, 3)
    return new_grid


def countPixels(grid):
    return sum(line.count('#') for line in grid)


def getAnswer(grid, rules, stop):
    for n in range(stop):
        grid = generateNewGrid(grid, rules)
    return countPixels(grid)


def test():
    grid = pattern
    rules = getRulesFromInput(test_input)
    assert getAnswer(grid, rules, 2) == 12


def main():
    test()
    input_data = readInputFile()
    grid = pattern
    rules = getRulesFromInput(input_data)
    getAnswer(grid, rules, 5)
    print('Day 21 Part 1:', getAnswer(grid, rules, 5))
    print('Day 21 Part 2:', getAnswer(grid, rules, 18))


if __name__ == '__main__':
    main()
