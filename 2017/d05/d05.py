def readInputFile():
    input_file = open('input', 'r')
    lines = []
    for line in input_file:
        line = line.strip('\n')
        lines.append(int(line))
    return lines


def countSteps(list_of_jump_offsets):
    counter = 0
    next_element_pointer = 0
    while 0 <= next_element_pointer < len(list_of_jump_offsets):
        previous_element_pointer = next_element_pointer
        previous_element = list_of_jump_offsets[next_element_pointer]
        next_element_pointer += previous_element
        previous_element += 1
        list_of_jump_offsets[previous_element_pointer] = previous_element
        counter += 1
    return counter


def countSteps2(list_of_jump_offsets):
    counter = 0
    next_element_pointer = 0
    while 0 <= next_element_pointer < len(list_of_jump_offsets):
        previous_element_pointer = next_element_pointer
        previous_element = list_of_jump_offsets[next_element_pointer]
        next_element_pointer += previous_element
        if previous_element < 3:
            previous_element += 1
        else:
            previous_element -= 1
        list_of_jump_offsets[previous_element_pointer] = previous_element
        counter += 1
    return counter


def test():
    assert countSteps([0, 3, 0, 1, -3]) == 5
    assert countSteps2([0, 3, 0, 1, -3]) == 10


def main():
    test()
    list_of_jump_offsets1 = readInputFile()
    list_of_jump_offsets2 = readInputFile()
    print("Day 5 Part 1:", countSteps(list_of_jump_offsets1))
    print("Day 5 Part 2:", countSteps2(list_of_jump_offsets2))


if __name__ == '__main__':
    main()