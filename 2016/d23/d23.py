registers = {
    'a': 7,
    'b': 0,
    'c': 0,
    'd': 0
}


def read_input_file():
    return open('input', 'r').read().splitlines()


def is_num(s):
    try:
        int(s)
    except:
        return False
    return True


def get_value(x):
    if is_num(x):
        return int(x)
    else:
        return registers[x]


def toggle(line: str):
    sp = line.split(' ')
    instr = sp[0]
    if instr == 'inc':
        return ' '.join(['dec'] + sp[1:])
    elif instr == 'dec' or instr == 'tgl':
        return ' '.join(['inc'] + sp[1:])
    elif instr == 'jnz':
        return ' '.join(['cpy'] + sp[1:])
    elif instr == 'cpy':
        return ' '.join(['jnz'] + sp[1:])
    else:
        raise ValueError


def get_safe_value(instructions: list):
    pc = 0

    while True:
        if pc >= len(instructions):
            break
        line = instructions[pc]

        a, b = line.split(' ', 1)

        if a == 'cpy':
            b, c = b.split(' ')
            b = get_value(b)
            if c in registers:
                registers[c] = b
            pc += 1
        elif a == 'inc':
            if b in registers:
                if pc + 3 < len(instructions) and pc - 1 >= 0 and instructions[pc - 1].startswith('cpy ') and \
                        instructions[pc + 1].startswith('dec') and instructions[pc + 2].startswith('jnz') and \
                        instructions[pc + 3].startswith('dec') and instructions[pc + 4].startswith('jnz'):

                    incop = b

                    cpysrc, cpydest = instructions[pc - 1].split(' ')[1:]
                    dec1op = instructions[pc + 1].split(' ')[1]
                    jnz1cond, jnz1off = instructions[pc + 2].split(' ')[1:]
                    dec2op = instructions[pc + 3].split(' ')[1]
                    jnz2cond, jnz2off = instructions[pc + 4].split(' ')[1:]

                    if cpydest == dec1op and dec1op == jnz1cond and \
                            dec2op == jnz2cond and \
                            jnz1off == '-2' and jnz2off == '-5':
                        registers[incop] += (get_value(cpysrc) * get_value(dec2op))
                        registers[dec1op] = 0
                        registers[dec2op] = 0
                        pc += 5
                        continue

                registers[b] += 1
            pc += 1
        elif a == 'dec':
            if b in registers:
                registers[b] -= 1
            pc += 1
        elif a == 'jnz':
            b, c = b.split(' ')
            b = get_value(b)
            c = get_value(c)
            if b != 0:
                pc = pc + int(c)
            else:
                pc += 1
        elif a == 'tgl':
            xr = b
            x = get_value(xr)
            iidx = pc + x
            if 0 <= iidx < len(instructions):
                tline = instructions[iidx]
                instructions[iidx] = toggle(tline)
            pc += 1
        else:
            raise ValueError
    return registers['a']


def main():
    input_data = read_input_file()
    print('Day 23 Part 1:', get_safe_value(list(input_data)))
    registers['a'] = 12
    print('Day 23 Part 2:', get_safe_value(list(input_data)))


if __name__ == '__main__':
    main()
