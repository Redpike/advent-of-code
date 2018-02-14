import re
from enum import Enum

test_input = [
    'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
    'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'
]

regex_pattern = r'(\w+) c.*y (\d+) km/s for (\d+) s.*for (\d+) seconds.'


class State(Enum):
    FLY = 0
    REST = 1


class Reindeer(object):
    name = ''
    speed = 0
    fly_time = 0
    rest_time = 0
    distance = 0
    points = 0
    counter = 0
    state = State.FLY

    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.distance = 0
        self.points = 0
        self.counter = fly_time
        self.state = State.FLY

    def change_params_when_fly(self):
        self.distance += self.speed
        self.counter -= 1
        if self.counter == 0:
            self.state = State.REST
            self.counter = self.rest_time

    def change_params_when_rest(self):
        self.counter -= 1
        if self.counter == 0:
            self.state = State.FLY
            self.counter = self.fly_time

    def __str__(self):
        return self.name, self.distance, self.state.name


def read_input_data():
    return open('input', 'r').read().splitlines()


def collect_reindeers(input_data):
    reindeers = []
    for line in input_data:
        reindeer = get_reindeer_data(line)
        reindeers.append(reindeer)

    return reindeers


def get_reindeer_data(line):
    regex_match = re.match(regex_pattern, line)
    reindeer = Reindeer(regex_match.group(1), int(regex_match.group(2)), int(regex_match.group(3)), int(
        regex_match.group(4)))

    return reindeer


def get_winner(input_data, run_time, part):
    reindeers = collect_reindeers(input_data)
    for timer in range(1, run_time + 1):
        for reindeer in reindeers:
            if reindeer.state == State.FLY:
                reindeer.change_params_when_fly()
            else:
                reindeer.change_params_when_rest()

        for reindeer in reindeers:
            if reindeer.distance == max(reindeer.distance for reindeer in reindeers):
                reindeer.points += 1

    if part == 1:
        return max(reindeer.distance for reindeer in reindeers)
    else:
        return max(reindeer.points for reindeer in reindeers)


def test():
    assert get_winner(test_input, 1000, 1) == 1120
    assert get_winner(test_input, 1000, 2) == 689


def main():
    test()
    input_data = read_input_data()
    print('Day 14 Part 1:', get_winner(input_data, 2503, 1))
    print('Day 14 Part 2:', get_winner(input_data, 2503, 2))


if __name__ == '__main__':
    main()
