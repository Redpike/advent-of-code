from collections import deque


def read_input():
    return open('input', 'r').read().splitlines()


def get_points(input_data):
    stars = []
    for line in input_data:
        stars.append([int(x) for x in line.split(",")])
    return stars


def manhattan_distance(a, b):
    s = 0
    for i in range(len(a)):
        s += abs(a[i] - b[i])
    return s


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) + abs(a[3] - b[3])


def solve(input_data: list):
    points = get_points(input_data)

    ret = 0
    all_used = set()

    while True:
        used = set()
        to_check = deque()
        for i in range(len(points)):
            if i not in all_used:
                to_check.append(i)
                break

        while len(to_check) > 0:
            cur = to_check.popleft()
            used.add(cur)
            all_used.add(cur)
            for i in range(len(points)):
                if i not in used and i not in all_used:
                    if dist(points[i], points[cur]) <= 3:
                        to_check.append(i)

        if len(used) == 0:
            break
        ret += 1

    return ret


def main():
    input_data = read_input()
    print('Day 25 Part 1:', solve(input_data))


if __name__ == '__main__':
    main()
