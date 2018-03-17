test_input = [
    'ihgpwlah',
    'kglvqrro',
    'ulqzkmiv'
]

input_data = 'dmypynyp'


def get_shortest_path(_input: str):
    return ''


def test():
    assert get_shortest_path(test_input[0]) == 'DDRRRD'
    assert get_shortest_path(test_input[1]) == 'DDUDRLRRUDRD'
    assert get_shortest_path(test_input[2]) == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'


def main():
    test()


if __name__ == '__main__':
    main()
