input_data = 1358


def is_wall(x: int, y: int):
    value = x * x + 3 * x + 2 * x * y + y + y * y + input_data
    one_bits = bin(value).count('1')
    return one_bits % 2 == 1


def get_possible_moves(old_x: int, old_y: int):
    possible_moves = [(old_x + 1, old_y), (old_x - 1, old_y), (old_x, old_y + 1), (old_x, old_y - 1)]
    return possible_moves


# BFS Algorithm
def search_path(part: int):
    traversed = {(1, 1)}
    steps = 0
    new_places = traversed
    while True:
        places_to_check = new_places.copy()
        new_places = set()
        for old_x, old_y in places_to_check:
            for x, y in get_possible_moves(old_x, old_y):
                if x < 0 or y < 0 or (x, y) in traversed or is_wall(x, y):
                    continue
                traversed.add((x, y))
                new_places.add((x, y))
        steps += 1
        if part == 1 and (31, 39) in new_places:
            return steps
        elif part == 2 and steps == 50:
            return len(traversed)


def main():
    print('Day 13 Part 1:', search_path(1))
    print('Day 13 Part 2:', search_path(2))


if __name__ == '__main__':
    main()
