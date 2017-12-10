test_input_part = [3, 4, 1, 5]


def readInputFile(part):
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        if part == 1:
            input_data = line.strip().split(',')
            input_data = [int(x) for x in input_data]
        else:
            input_data = line.strip()
            input_data = [ord(x) for x in input_data] + [17, 31, 73, 47, 23]
    return input_data


def createSequence(input_data, times, list_size):
    position = 0
    skip = 0
    sequence = list(range(list_size))
    for _ in range(times):
        for number in input_data:
            for i in range(number // 2):
                now = (position + i) % len(sequence)
                later = (position + number - 1 - i) % len(sequence)
                sequence[now], sequence[later] = sequence[later], sequence[now]
            position += number + skip
            skip += 1
    return sequence


def returnMultiply(sequence):
    return sequence[0] * sequence[1]


def createKnotHash():
    sequence_part_2 = createSequence(readInputFile(2), 64, 256)
    hashed_data = ''
    for i in range(len(sequence_part_2) // 16):
        num = 0
        for j in range(16):
            num ^= sequence_part_2[i * 16 + j]
        hashed_data += hex(num)[2:].zfill(2)
    return hashed_data


def test():
    test_sequence = createSequence(test_input_part, 4, 5)
    assert returnMultiply(test_sequence) == 12


def main():
    test()
    sequence_part_1 = createSequence(readInputFile(1), 1, 256)
    print('Day 10 Part 1:', returnMultiply(sequence_part_1))
    print('Day 10 Part 2:', createKnotHash())


if __name__ == '__main__':
    main()
