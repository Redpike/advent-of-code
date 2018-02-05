import re

test_input = [
    'ugknbfddgicrmopn',
    'aaa',
    'jchzalrnumimnmhp',
    'haegwjzuvuyypxyu',
    'dvszwmarrgswjxmb',
    'qjhvhtzxzqqjkmpb',
    'xxyxx',
    'uurcxstgmygtbstg',
    'ieodomkazucvgmuy'
]


def readInputFile():
    input_file = open('input', 'r').read()
    input_data = []
    for line in input_file.splitlines():
        input_data.append(line)
    return input_data


def hasThreeVowels(string):
    vowels = re.findall(r'[aeiou]', string)
    return len(vowels) >= 3


def hasOneLetterTwiceInARow(string):
    double_letters = re.search(r'(.)\1', string)
    return double_letters


def doesContainStrings(string):
    bad_strings = re.search(r'ab|cd|pq|xy', string)
    return bad_strings


def doesContainPairOfLetters(string):
    pair_of_letters = re.search(r'(..).*\1', string)
    return pair_of_letters


def doesMatchBetween(string):
    match_between = re.search(r'(.).\1', string)
    return match_between


def isItNiceString(string):
    if not hasThreeVowels(string):
        return False

    if not hasOneLetterTwiceInARow(string):
        return False

    if doesContainStrings(string):
        return False

    return True


def isItNiceOfTheNiceString(string):
    if not doesContainPairOfLetters(string):
        return False

    if not doesMatchBetween(string):
        return False

    return True


def countNiceStrings(input_data):
    nice_strings = 0
    for string in input_data:
        if isItNiceString(string):
            nice_strings += 1
    return nice_strings


def countNiceOfTheNiceStrings(input_data):
    nice_of_the_nice_strings = 0
    for string in input_data:
        if isItNiceOfTheNiceString(string):
            nice_of_the_nice_strings += 1
    return nice_of_the_nice_strings


def test():
    assert isItNiceString(test_input[0])
    assert isItNiceString(test_input[1])
    assert not isItNiceString(test_input[2])
    assert not isItNiceString(test_input[3])
    assert not isItNiceString(test_input[4])
    assert isItNiceOfTheNiceString(test_input[5])
    assert isItNiceOfTheNiceString(test_input[6])
    assert not isItNiceOfTheNiceString(test_input[7])
    assert not isItNiceOfTheNiceString(test_input[8])


def main():
    test()
    input_data = readInputFile()
    print('Day 05 Part 1:', countNiceStrings(input_data))
    print('Day 05 Part 2:', countNiceOfTheNiceStrings(input_data))


if __name__ == '__main__':
    main()
