from collections import defaultdict

test_input = [
    'b inc 5 if a > 1',
    'a inc 1 if b < 5',
    'c dec -10 if a >= 1',
    'c inc -20 if c == 10'
]

increment_function = 'inc'


class Register:
    register_name = ''
    step_funtion = ''
    ammount = 0

    def __init__(self, register_name, step_function, ammount):
        self.register_name = register_name
        self.step_funtion = step_function
        self.ammount = ammount


class Condition:
    left_side = ''
    operator = ''
    right_side = 0

    def __init__(self, left_side, operator, right_side):
        self.left_side = left_side
        self.operator = operator
        self.right_side = right_side


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        line = line.strip('\n')
        input_data.append(line)
    return input_data


def createCondition(condition, registers):
    condition.left_side = registers[condition.left_side]
    condition = eval(str(condition.left_side) + condition.operator + str(condition.right_side))
    return condition


def getLargestValueOfRegisters(input_data, part):
    registers = defaultdict(int)
    largest_value = 0
    for line in input_data:
        line = line.strip('\n').split()
        register = Register(line[0], line[1], int(line[2]))
        condition = Condition(line[4], line[5], int(line[6]))
        if createCondition(condition, registers):
            if register.step_funtion == increment_function:
                registers[register.register_name] += register.ammount
            else:
                registers[register.register_name] -= register.ammount
            largest_value = max(registers[register.register_name], largest_value)

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
