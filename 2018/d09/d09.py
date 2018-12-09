import re
from collections import defaultdict, deque
from itertools import cycle

test_input = [
    '10 players; last marble is worth 1618 points: high score is 8317',
    '13 players; last marble is worth 7999 points: high score is 146373',
    '17 players; last marble is worth 1104 points: high score is 2764',
    '21 players; last marble is worth 6111 points: high score is 54718',
    '30 players; last marble is worth 5807 points: high score is 37305'
]

regex_pattern = r'(\d+) players; last marble is worth (\d+)'


def read_input():
    return open('input', 'r').readline()


def parse_input(_input: str, part: int):
    regex_matcher = re.match(regex_pattern, _input)
    players, last_marble = int(regex_matcher.group(1)), int(regex_matcher.group(2))
    if part == 2:
        last_marble *= 100
    return players, last_marble
    

def get_winning_score(_input: str, part: int):
    players, last_marble = parse_input(_input, part)
    elves = defaultdict(int)
    circle = deque()

    for current_marble, current_elf in zip(range(last_marble + 1), cycle(range(players))):
        if current_marble and current_marble % 23 == 0:
            circle.rotate(7)
            elves[current_elf] += current_marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(current_marble)
    return max(elves.values())


def test():
    assert get_winning_score(test_input[0], part=1) == 8317
    assert get_winning_score(test_input[1], part=1) == 146373
    assert get_winning_score(test_input[2], part=1) == 2764
    assert get_winning_score(test_input[3], part=1) == 54718
    assert get_winning_score(test_input[4], part=1) == 37305


def main():
    test()
    _input = read_input()
    print('Day 09 Part 1:', get_winning_score(_input, part=1))
    print('Day 09 Part 2:', get_winning_score(_input, part=2))


if __name__ == '__main__':
    main()
