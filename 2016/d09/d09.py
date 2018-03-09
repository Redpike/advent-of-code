import re

test_input = [
    'ADVENT',
    'A(1x5)BC',
    '(3x3)XYZ',
    'A(2x2)BCD(2x2)EFG',
    '(6x1)(1x3)A',
    'X(8x2)(3x3)ABCY'
]

test_input2 = [
    '(3x3)XYZ',
    'X(8x2)(3x3)ABCY',
    '(27x12)(20x12)(13x14)(7x10)(1x12)A',
    '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
]

regex_pattern = r'\((\d+)x(\d+)\)'


def read_input_file():
    return open('input', 'r').readline()


def decompress_text(compressed_text: str):
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


def decompress_text_2(compressed_text: str):
    regex_search = re.search(regex_pattern, compressed_text)
    if regex_search:
        sequence_length = int(regex_search.group(1))
        multiplier = int(regex_search.group(2))
        start_marker = regex_search.start()
        end_marker = regex_search.end()

        inside_marker_part = compressed_text[end_marker:end_marker + sequence_length]
        outside_marker_part = compressed_text[end_marker + sequence_length:]

        length_of_text = start_marker + (decompress_text_2(inside_marker_part) * multiplier) \
                         + decompress_text_2(outside_marker_part)
        return length_of_text
    else:
        return len(compressed_text)


def test():
    assert decompress_text(test_input[0]) == 6
    assert decompress_text(test_input[1]) == 7
    assert decompress_text(test_input[2]) == 9
    assert decompress_text(test_input[3]) == 11
    assert decompress_text(test_input[4]) == 6
    assert decompress_text(test_input[5]) == 18
    assert decompress_text_2(test_input2[0]) == 9
    assert decompress_text_2(test_input2[1]) == 20
    assert decompress_text_2(test_input2[2]) == 241920
    assert decompress_text_2(test_input2[3]) == 445


def main():
    test()
    input_data = read_input_file()
    print('Day 09 Part 1:', decompress_text(input_data))
    print('Day 09 Part 2:', decompress_text_2(input_data))


if __name__ == '__main__':
    main()
