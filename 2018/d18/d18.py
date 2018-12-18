import re
import copy


def read_input():
    return open('input', 'r').read().splitlines()


def get(ground: list, y: int, x: int):
    if y < 0 or x < 0:
        return ' '
    try:
        return ground[y][x]
    except IndexError:
        return ' '


def get_total_resource_value(input_data: list, time_param: int):
    ground = [list(line.strip()) for line in input_data]
    snapshots = []
    for time in range(1, 1000):
        ground2 = copy.deepcopy(ground)
        for (y, row) in enumerate(ground):
            for (x, val) in enumerate(row):
                neighbors = ''.join(get(ground, y + a, x + b) for (a, b) in
                                    [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                                     (0, 1), (1, -1), (1, 0), (1, 1)])
                if val == '.':
                    if re.search('[|].*[|].*[|]', neighbors):
                        ground2[y][x] = '|'
                elif val == '|':
                    if re.search('[#].*[#].*[#]', neighbors):
                        ground2[y][x] = '#'
                elif val == '#':
                    if not re.search('[#].*[|]|[|].*[#]', neighbors):
                        ground2[y][x] = '.'
        ground = ground2

        snapshot = '\n'.join(''.join(row) for row in ground)
        if snapshot in snapshots:
            i = snapshots.index(snapshot)
            period = time - (1 + i)
            while (i + 1) % period != 1000000000 % period:
                i += 1
            count1 = len(re.findall('[|]', snapshots[i]))
            count2 = len(re.findall('[#]', snapshots[i]))
            return count1 * count2
        snapshots.append(snapshot)

        if time == time_param:
            count1 = len(re.findall('[|]', snapshot))
            count2 = len(re.findall('[#]', snapshot))
            return count1 * count2


def main():
    input_data = read_input()
    print('Day 18 Part 1:', get_total_resource_value(input_data, time_param=10))
    print('Day 18 Part 2:', get_total_resource_value(input_data, time_param=1_000_000_000))


if __name__ == '__main__':
    main()
