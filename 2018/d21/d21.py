def read_input():
    lines = open('input', 'r').read().splitlines()
    seti_list, bori_list, bani_list, muli_list = [], [], [], []
    for line in lines:
        line_parts = line.split()
        if line_parts[0] == 'seti':
            seti_list.append(int(line_parts[1]))
        elif line_parts[0] == 'bori':
            bori_list.append(int(line_parts[2]))
        elif line_parts[0] == 'bani':
            bani_list.append(int(line_parts[2]))
        elif line_parts[0] == 'muli':
            muli_list.append(int(line_parts[2]))
    return max(seti_list), max(bori_list), max(bani_list), max(muli_list)


def activate_system(seti: int, bori: int, bani: int, muli: int, part: int):
    seen = set()
    c = 0
    last_unique_c = -1

    while True:
        a = c | bori
        c = seti

        while True:
            c = (((c + (a & 255)) & bani) * muli) & bani

            if 256 > a:
                if part == 1:
                    return c
                else:
                    if c not in seen:
                        seen.add(c)
                        last_unique_c = c
                        break
                    else:
                        return last_unique_c
            else:
                a //= 256


def main():
    seti, bori, bani, muli = read_input()
    print('Day 21 Part 1:', activate_system(seti, bori, bani, muli, part=1))
    print('Day 21 Part 2:', activate_system(seti, bori, bani, muli, part=2))


if __name__ == '__main__':
    main()
