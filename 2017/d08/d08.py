from collections import defaultdict

test_input = [
    'b inc 5 if a > 1',
    'a inc 1 if b < 5',
    'c dec -10 if a >= 1',
    'c inc -20 if c == 10'
]

increment_function = 'inc'


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        line = line.strip('\n')
        input_data.append(line)
    return input_data


def createCondition(left_side, operator, right_side, registers):
    left_side = registers[left_side]
    condition = eval(str(left_side) + operator + str(right_side))
    return condition

#TODO Need refactor!!!!!!
def getLargestValueOfRegisters(input_data, part):
    registers = defaultdict(int)
    largest_value = 0
    for line in input_data:
        line = line.strip('\n').split()
        register = line[0]
        reg_function = line[1]
        ammount = int(line[2])
        left_side = line[4]
        operator = line[5]
        right_side = int(line[6])
        if createCondition(left_side, operator, right_side, registers):
            if reg_function == increment_function:
                registers[register] += ammount
            else:
                registers[register] -= ammount
            largest_value = max(registers[register], largest_value)

    if part == 1:
        return max(registers.values())
    else:
        return largest_value


def test():
    assert getLargestValueOfRegisters(test_input, 1) == 1
    assert getLargestValueOfRegisters(test_input, 2) == 10


def selectInput(is_production):
    if is_production:
        return readInputFile()
    else:
        return test_input


def main():
    test()
    input_data = selectInput(True)
    print('Day 8 Part 1:', getLargestValueOfRegisters(input_data, 1))
    print('Day 8 Part 2:', getLargestValueOfRegisters(input_data, 2))


if __name__ == '__main__':
    main()
