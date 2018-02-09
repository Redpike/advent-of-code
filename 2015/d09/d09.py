from collections import defaultdict
from itertools import permutations


def read_input_file():
    return open('input', 'r').readlines()


def get_the_shortest_and_longest_route(input_data):
    shortert = 999
    longest = 0
    distances = defaultdict(lambda: defaultdict(int))

    for line in input_data:
        l, r = line.strip().split(" = ")
        c1, c2 = l.split(" to ")
        distances[c1][c2] = int(r)
        distances[c2][c1] = int(r)

    for perm in permutations(distances.keys(), len(distances)):
        dist = 0
        start = perm[0]
        for city in perm[1:]:
            dist += distances[start][city]
            start = city
        if dist < shortert:
            shortert = dist
        if dist > longest:
            longest = dist

    return shortert, longest


def main():
    input_data = read_input_file()
    shortest, longerst = get_the_shortest_and_longest_route(input_data)
    print('Day 09 Part 1:', shortest)
    print('Day 09 Part 2:', longerst)


if __name__ == '__main__':
    main()
