import re

test_input = [
    'ADVENT',
    'A(1x5)BC',
    '(3x3)XYZ',
    'A(2x2)BCD(2x2)EFG',
    '(6x1)(1x3)A',
    'X(8x2)(3x3)ABCY'
]

regex_pattern = r'\((\d+)x(\d+)\)'


def read_input_file():
    return open('input', 'r').readline()


def decompresse_text(compressed_text: str):
    decompressed_text = ''
    marker = 0

    while True:
        decompressed = compressed_text[marker:]
        regex_search = re.search(regex_pattern, decompressed)
        if regex_search:
            sequence_length = int(regex_search.group(1))
            multiplier = int(regex_search.group(2))
            start_marker = marker + regex_search.start()
            end_marker = marker + regex_search.end()
            decompressed_text += compressed_text[marker:start_marker]
            for _ in range(multiplier):
                decompressed_text += compressed_text[end_marker:end_marker + sequence_length]
            marker = end_marker + sequence_length
        else:
            decompressed_text += compressed_text[marker:]
            break
    return len(decompressed_text)


def test():
    assert decompresse_text(test_input[0]) == 6
    assert decompresse_text(test_input[1]) == 7
    assert decompresse_text(test_input[2]) == 9
    assert decompresse_text(test_input[3]) == 11
    assert decompresse_text(test_input[4]) == 6
    assert decompresse_text(test_input[5]) == 18


def main():
    test()
    input_data = read_input_file()
    print('Day 09 Part 1:', decompresse_text(input_data))


if __name__ == '__main__':
    main()
