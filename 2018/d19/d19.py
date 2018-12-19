def addr(regs, a, b):
    return regs[a] + regs[b]


def addi(regs, a, b):
    return regs[a] + b


def mulr(regs, a, b):
    return regs[a] * regs[b]


def muli(regs, a, b):
    return regs[a] * b


def banr(regs, a, b):
    return regs[a] & regs[b]


def bani(regs, a, b):
    return regs[a] & b


def borr(regs, a, b):
    return regs[a] | regs[b]


def bori(regs, a, b):
    return regs[a] | b


def setr(regs, a, b):
    return regs[a]


def seti(regs, a, b):
    return a


def gtir(regs, a, b):
    return int(a > regs[b])


def gtri(regs, a, b):
    return int(regs[a] > b)


def gtrr(regs, a, b):
    return int(regs[a] > regs[b])


def eqir(regs, a, b):
    return int(a == regs[b])


def eqri(regs, a, b):
    return int(regs[a] == b)


def eqrr(regs, a, b):
    return int(regs[a] == regs[b])


def read_input():
    with open('input') as puzzle_file:
        ip = int(puzzle_file.readline().strip()[3:])
        instructions = [(globals()[op], int(a), int(b), int(c))
                        for line in puzzle_file for op, a, b, c in (line.split(),)]
    return ip, instructions


def sum_factors(n):
    total, d = 0, 1
    while d * d < n:
        if n % d == 0:
            total += d + n // d
        d += 1
    if d * d == n:
        total += d
    return total


def cheat(regs, ip, instructions):
    base = regs[ip]
    if base + 14 >= len(instructions):
        return False
    op, a, b, i = instructions[base]
    if op != seti or a != 1 or i == ip:
        return False
    op, a, b, j = instructions[base + 1]
    if op != seti or a != 1 or j in (ip, i):
        return False
    op, a, b, k = instructions[base + 2]
    if op != mulr or a != i or b != j or k in (ip, i, j):
        return False
    op, a, n, c = instructions[base + 3]
    if op != eqrr or a != k or n in (ip, i, j, k) or c != k:
        return False
    op, a, b, c = instructions[base + 4]
    if op != addr or a != k or b != ip or c != ip:
        return False
    op, a, b, c = instructions[base + 5]
    if op != addi or a != ip or b != 1 or c != ip:
        return False
    op, a, b, m = instructions[base + 6]
    if op != addr or a != i or b != 0 or m in (ip, i, j, k, n):
        return False
    op, a, b, c = instructions[base + 7]
    if op != addi or a != j or b != 1 or c != j:
        return False
    op, a, b, c = instructions[base + 8]
    if op != gtrr or a != j or b != n or c != k:
        return False
    op, a, b, c = instructions[base + 9]
    if op != addr or a != ip or b != k or c != ip:
        return False
    op, a, _, c = instructions[base + 10]
    if op != seti or a != base + 1 or c != ip:
        return False
    op, a, b, c = instructions[base + 11]
    if op != addi or a != i or b != 1 or c != i:
        return False
    op, a, b, c = instructions[base + 12]
    if op != gtrr or a != i or b != n or c != k:
        return False
    op, a, b, c = instructions[base + 13]
    if op != addr or a != k or b != ip or c != ip:
        return False
    op, a, _, c = instructions[base + 14]
    if op != seti or a != base or c != ip:
        return False
    goal = regs[n]
    if goal < 1:
        return False
    regs[ip], regs[i], regs[j], regs[k] = base + 15, goal + 1, goal + 1, 1
    regs[m] += sum_factors(goal)
    return True


def run(regs, ip, instructions):
    while 0 <= regs[ip] < len(instructions):
        if cheat(regs, ip, instructions):
            continue
        op, a, b, c = instructions[regs[ip]]
        regs[c] = op(regs, a, b)
        regs[ip] += 1
    return regs


def main():
    ip, instructions = read_input()
    print('Day 19 Part 1:', run(6 * [0], ip, instructions)[0])
    print('Day 19 Part 2:', run([1] + 5 * [0], ip, instructions)[0])


if __name__ == '__main__':
    main()
