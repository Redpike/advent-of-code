test_input = [
    'inc a',
    'jio a, +2',
    'tpl a',
    'inc a'
]

registers = {
    'a': 0,
    'b': 0
}


def read_input_file():
    return open('input', 'r').read().splitlines()


def get_jump_after_instruction(instruction, register):
    jump = 1
    if instruction == 'hlf':
        registers[register] //= 2
    elif instruction == 'tpl':
        registers[register] *= 3
    elif instruction == 'inc':
        registers[register] += 1
    elif instruction == 'jmp':
        jump = int(register)
    elif instruction == 'jie':
        reg, offset = register.split(', ')
        if registers[reg] % 2 == 0:
            jump = int(offset)
    elif instruction == 'jio':
        reg, offset = register.split(', ')
        if registers[reg] == 1:
            jump = int(offset)
    else:
        raise ValueError

    return jump


def execute_puzzle(input_data, _register):
    index = 0
    while index < len(input_data):
        line = input_data[index]
        instruction, register = line.split(' ', 1)
        jump = get_jump_after_instruction(instruction, register)
        index += jump
    return registers[_register]


def test():
    assert execute_puzzle(test_input, 'a') == 2


def main():
    test()
    global registers
    registers = registers.fromkeys(registers, 0)
    input_data = read_input_file()
    print('Day 23 Part 1:', execute_puzzle(input_data, 'b'))
    registers = registers.fromkeys(registers, 0)
    registers['a'] = 1
    print('Day 23 Part 2:', execute_puzzle(input_data, 'b'))


if __name__ == '__main__':
    main()
