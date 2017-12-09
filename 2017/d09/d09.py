test_input = [
    '{}',
    '{{{}}}',
    '{{},{}}',
    '{{{},{},{{}}}}',
    '{<a>,<a>,<a>,<a>}',
    '{{<ab>},{<ab>},{<ab>},{<ab>}}',
    '{{<!!>},{<!!>},{<!!>},{<!!>}}',
    '{{<a!>},{<a!>},{<a!>},{<ab>}}'
]


test_input2 = [
    '<>',
    '<random characters>',
    '<<<<>',
    '<{!>}>',
    '<!!>',
    '<!!!>>',
    '<{o"i!a,<{i<a>'
]


def readInputFile():
    input_file = open('input', 'r')
    input_data = ''
    for line in input_file:
        input_data = line
    return input_data


def computePoints(input_line, part):
    group_score, gc_score, nested_level = 0, 0, 0
    is_garbage, skip_next_char = False, False
    for char in input_line:
        if is_garbage:
            if skip_next_char:
                skip_next_char = False
            elif char == '>':
                is_garbage = False
            elif char == '!':
                skip_next_char = True
            else:
                gc_score += 1
        else:
            if char == '{':
                nested_level += 1
            elif char == '}':
                group_score += nested_level
                nested_level -= 1
            elif char == '<':
                is_garbage = True
    if part == 1:
        return group_score
    else:
        return gc_score


def test():
    assert computePoints(test_input[0], 1) == 1
    assert computePoints(test_input[1], 1) == 6
    assert computePoints(test_input[2], 1) == 5
    assert computePoints(test_input[3], 1) == 16
    assert computePoints(test_input[4], 1) == 1
    assert computePoints(test_input[5], 1) == 9
    assert computePoints(test_input[6], 1) == 9
    assert computePoints(test_input[7], 1) == 3
    assert computePoints(test_input2[0], 2) == 0
    assert computePoints(test_input2[1], 2) == 17
    assert computePoints(test_input2[2], 2) == 3
    assert computePoints(test_input2[3], 2) == 2
    assert computePoints(test_input2[4], 2) == 0
    assert computePoints(test_input2[5], 2) == 0
    assert computePoints(test_input2[6], 2) == 10


def selectInput(is_production):
    if is_production:
        return readInputFile()
    else:
        return test_input


def main():
    test()
    input_data = selectInput(True)
    print('Day 9 Part 1:', computePoints(input_data, 1))
    print('Day 9 Part 2:', computePoints(input_data, 2))


if __name__ == '__main__':
    main()
