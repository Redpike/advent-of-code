from itertools import permutations


def readInputFileAndSplit():
    input_file = open('input', 'r')
    lines = []
    for line in input_file:
        line = line.strip('\n').split('\t')
        lines.append(list(map(int, line)))
    return lines


def countSum(lines, part):
    sum_of_elements = 0
    for line in lines:
        if part == 1:
            sum_of_elements += (max(line) - min(line))
        elif part == 2:
            for (x, y) in permutations(line, 2):
                if x % y == 0:
                    sum_of_elements += int(x / y)
    return sum_of_elements


def test():
    assert countSum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]], 1) == 18
    assert countSum([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]], 2) == 9


def main():
    test()
    lines = readInputFileAndSplit()
    print("Day 2 Part 1:", countSum(lines, 1))
    print("Day 2 Part 2:", countSum(lines, 2))


if __name__ == '__main__':
    main()
