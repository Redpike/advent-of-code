def list_map(f, s):
    return list(map(f, s))


def addr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] + result[b]
    return result


def addi(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] + b
    return result


def mulr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] * result[b]
    return result


def muli(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] * b
    return result


def banr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] & result[b]
    return result


def bani(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] & b
    return result


def borr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] | result[b]
    return result


def bori(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] | b
    return result


def setr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a]
    return result


def seti(registers, a, b, c):
    result = registers[::]
    result[c] = a
    return result


def gtir(registers, a, b, c):
    result = registers[::]
    result[c] = bool(a > result[b])
    return result


def gtri(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] > b)
    return result


def gtrr(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] > result[b])
    return result


def eqir(registers, a, b, c):
    result = registers[::]
    result[c] = bool(a == result[b])
    return result


def eqri(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] == b)
    return result


def eqrr(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] == result[b])
    return result


OPERATIONS = [
    addr, addi,
    mulr, muli,
    banr, bani,
    borr, bori,
    setr, seti,
    gtir, gtri, gtrr,
    eqir, eqri, eqrr
]


def read_input():
    return open('input', 'r').read().splitlines()


def possible_operations(instruction, before, after):
    result = set()
    for operation in OPERATIONS:
        op_result = operation(before, *instruction[1:])
        if op_result == after:
            result.add(operation)
    return result


def run_test_program(input_data: list):
    i = 0
    experiments = []
    while input_data[i].strip():
        before, instruction, after = input_data[i:i + 3]
        i += 4
        experiments.append((
            list_map(int, instruction.split(' ')),
            eval(before[8:]),
            eval(after[8:])
        ))
    return experiments, i


def get_three_or_more_opcodes(input_data: list):
    experiments, i = run_test_program(input_data)
    return len([experiment for experiment in experiments if len(possible_operations(*experiment)) >= 3])


def get_value_from_register_0(input_data: list):
    experiments, i = run_test_program(input_data)
    operations = {opcode: set(OPERATIONS) for opcode in range(16)}
    for experiment in experiments:
        opcode = experiment[0][0]
        operations[opcode].intersection_update(possible_operations(*experiment))

    while True:
        unique_ops = {}
        for op, ops in operations.items():
            if len(ops) == 1:
                unique_ops[op] = ops
        for op_, ops_ in unique_ops.items():
            for op, ops in operations.items():
                if op != op_:
                    ops.difference_update(ops_)
        if len(unique_ops) == len(operations):
            break

    for op in operations:
        operations[op] = operations[op].pop()
    registers = [0, 0, 0, 0]
    for line in input_data[i:]:
        if not line.strip():
            continue
        opcode, a, b, c = list_map(int, line.split(' '))
        registers = operations[opcode](registers, a, b, c)
    return registers[0]


def main():
    input_data = read_input()
    print('Day 16 Part 1:', get_three_or_more_opcodes(input_data))
    print('Day 16 Part 2:', get_value_from_register_0(input_data))


if __name__ == '__main__':
    main()
