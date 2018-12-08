test_input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'


def read_input():
    return open('input', 'r').read().split()


def parse_input_data(_input: list):
    _input = [int(x) for x in _input]
    children, metas = _input[:2]
    data = _input[2:]
    scores = []
    totals = 0

    for i in range(children):
        total, score, data = parse_input_data(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0:
        return totals, sum(data[:metas]), data[metas:]
    else:
        return (
            totals,
            sum(scores[k - 1] for k in data[:metas] if 0 < k <= len(scores)),
            data[metas:]
        )


def test():
    sum_of_metadata, score, remains = parse_input_data(test_input.split())
    assert sum_of_metadata == 138
    assert score == 66


def main():
    test()
    _input = read_input()
    sum_of_metadata, score, remains = parse_input_data(_input)
    print('Day 08 Part 1', sum_of_metadata)
    print('Day 08 Part 2', score)


if __name__ == '__main__':
    main()
