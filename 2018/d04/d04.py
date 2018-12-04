from collections import defaultdict

test_input = [
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-01 23:58] Guard #99 begins shift',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-03 00:05] Guard #10 begins shift',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-05 00:45] falls asleep',
    '[1518-11-05 00:55] wakes up'
]


def read_input():
    return open('input', 'r').read().split('\n')


def parse_time(line: str):
    words = line.split()
    date, time = words[0][1:], words[1][:-1]
    return int(time.split(':')[1])


def get_id_of_guard(_input: list):
    guard, asleep = None, None
    C, CM = defaultdict(int), defaultdict(lambda: defaultdict(int))
    for line in _input:
        time = parse_time(line)
        if 'begins shift' in line:
            guard = int(line.split()[3][1:])
            asleep = None
        elif 'falls asleep' in line:
            asleep = time
        elif 'wakes up' in line:
            for t in range(asleep, time):
                CM[guard][t] += 1
                C[guard] += 1

    def arg_max(d: defaultdict):
        best = None
        for k, v in d.items():
            if best is None or v > d[best]:
                best = k
        return best

    best_guard = arg_max(C)
    best_min = arg_max(CM[best_guard])
    return best_guard * best_min


def test():
    assert get_id_of_guard(test_input) == 240


def main():
    test()
    _input = read_input()
    _input.sort()
    print('Day 04 Part 1:', get_id_of_guard(_input))


if __name__ == '__main__':
    main()
