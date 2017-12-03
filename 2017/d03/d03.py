from collections import defaultdict
from itertools import cycle


# Move functions
def up(x, y):
    y += 1
    return x, y


def right(x, y):
    x += 1
    return x, y


def down(x, y):
    y -= 1
    return x, y


def left(x, y):
    x -= 1
    return x, y


moves = [right, up, left, down]


def generateSquarePart1(last_square_number):
    cycle_moves = cycle(moves)
    square_no, times_to_move = 1, 1
    pos = 0, 0
    yield square_no, pos

    while True:
        for _ in range(2):
            next_move = next(cycle_moves)
            for _ in range(times_to_move):
                if square_no >= last_square_number:
                    return
                pos = next_move(*pos)
                square_no += 1
                yield square_no, pos
        times_to_move += 1


def getFirstHigherValue(last_square_number):
    cycle_moves = cycle(moves)
    square_no, times_to_move, value = 1, 1, 1
    list_of_squares = defaultdict(int)
    pos = (0, 0)
    list_of_squares[pos] = value

    while True:
        for _ in range(2):
            next_move = next(cycle_moves)
            for _ in range(times_to_move):
                if getValueFromPosition(list_of_squares, pos) >= last_square_number:
                    return getValueFromPosition(list_of_squares, pos)
                square_no += 1
                pos = next_move(*pos)
                list_of_squares[pos] = getValueFromPosition(list_of_squares, pos)
        times_to_move += 1


def countSteps(list_of_squares, square_number):
    steps = 0
    if square_number != 1:
        distance_x = abs(list_of_squares[square_number - 1][1][0] - list_of_squares[0][1][0])
        distance_y = abs(list_of_squares[square_number - 1][1][1] - list_of_squares[0][1][1])
        steps = distance_x + distance_y
    return steps


def getValueFromPosition(list_of_squares, pos):
    return list_of_squares[(pos[0] + 1, pos[1])] +\
               list_of_squares[(pos[0] - 1, pos[1])] +\
               list_of_squares[(pos[0], pos[1] + 1)] +\
               list_of_squares[(pos[0], pos[1] - 1)] +\
               list_of_squares[(pos[0] + 1, pos[1] + 1)] +\
               list_of_squares[(pos[0] + 1, pos[1] - 1)] +\
               list_of_squares[(pos[0] - 1, pos[1] + 1)] +\
               list_of_squares[(pos[0] - 1, pos[1] - 1)]


def test(list_of_squares):
    assert countSteps(list_of_squares, 1) == 0
    assert countSteps(list_of_squares, 12) == 3
    assert countSteps(list_of_squares, 23) == 2
    assert countSteps(list_of_squares, 1024) == 31


def main():
    number_of_squares = 277678
    list_of_squares = list(generateSquarePart1(number_of_squares))
    test(list_of_squares)
    print("Day 3 Part 1:", countSteps(list_of_squares, number_of_squares))
    print("Day 3 Part 2:", getFirstHigherValue(number_of_squares))


if __name__ == '__main__':
    main()
