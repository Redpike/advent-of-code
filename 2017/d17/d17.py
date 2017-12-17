input_data = 355


def buffer():
    buffer = [0]
    current = 0
    for i in range(1, 2018):
        current = ((current + input_data) % len(buffer)) + 1
        buffer.insert(current, i)
    return buffer[buffer.index(2017) + 1]


def buffer2():
    current, num_after = 0, 0
    for i in range(1, 50000001):
        current = ((current + input_data) % i) + 1
        if current == 1:
            num_after = i
    return num_after


def main():
    print('Day 17 Part 1:', buffer())
    print('Day 17 Part 2:', buffer2())


if __name__ == '__main__':
    main()
