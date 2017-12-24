from collections import defaultdict


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        line = line.strip('\n')
        input_data.append(line)
    return input_data


def getValue(registers, value):
    try:
        return int(value)
    except:
        return registers[value]


def solve(part, input_data):
    registers = defaultdict(int)
    registers['a'] = part - 1
    i = 0
    while i < 11:
        op, reg, val = input_data[i].split()
        if op == 'set':
            registers[reg] = getValue(registers, val)
        elif op == 'sub':
            registers[reg] -= getValue(registers, val)
        elif op == 'mul':
            registers[reg] *= getValue(registers, val)
        elif op == 'jnz':
            if getValue(registers, reg) != 0:
                i += getValue(registers, val)
                continue
        i += 1

    if part == 1:
        return (registers['b'] - registers['e']) * (registers['b'] - registers['d'])
    else:
        nonprimes = 0
        for b in range(registers['b'], registers['c'] + 1, 17):
            if any(b % d == 0 for d in range(2, int(b ** 0.5))):
                nonprimes += 1
        return nonprimes


def main():
    input_data = readInputFile()
    print('Day 23 Part 1:', solve(1, input_data))
    print('Day 23 Part 2:', solve(2, input_data))


if __name__ == '__main__':
    main()
