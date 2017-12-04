from itertools import combinations


def readInputFile():
    input_file = open('input', 'r')
    lines = []
    for line in input_file:
        line = line.strip('\n').split()
        lines.append(list(map(str, line)))
    return lines


def checkLineWordsAndCountBadLines(lines):
    counter_of_bad_lines = 0
    for line in lines:
        for x, y in combinations(line, 2):
            if x == y:
                counter_of_bad_lines += 1
                break
    return counter_of_bad_lines


def checkLineWordsAndCountBadLines2(lines):
    counter_of_bad_lines = 0
    for line in lines:
        single_line_words_array = list(map(lambda word: (' '.join(sorted(list(word)))), line))
        if len(single_line_words_array) != len(set(single_line_words_array)):
            counter_of_bad_lines += 1
    return counter_of_bad_lines


def test():
    assert checkLineWordsAndCountBadLines([['aa', 'bb', 'cc', 'dd', 'ee'],
                                           ['aa', 'bb', 'cc', 'dd', 'aa'],
                                           ['aa', 'bb', 'cc', 'dd', 'aaa']]) == 1
    assert checkLineWordsAndCountBadLines2([['abcde', 'fghij'],
                                            ['abcde', 'xyz', 'ecdab'],
                                            ['a', 'ab', 'abc', 'abf', 'abj'],
                                            ['iiii', 'oiii', 'ooii', 'oooi', 'oooo'],
                                            ['oiii', 'ioii', 'iioi', 'iiio']]) == 2


def main():
    test()
    lines = readInputFile()
    good_lines1 = len(lines) - checkLineWordsAndCountBadLines(lines)
    good_lines2 = len(lines) - checkLineWordsAndCountBadLines2(lines)
    print("Day 4 Part 1:", good_lines1)
    print("Day 4 Part 2:", good_lines2)


if __name__ == '__main__':
    main()