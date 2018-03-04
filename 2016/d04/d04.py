import re

test_input = [
    'aaaaa-bbb-z-y-x-123[abxyz]',
    'a-b-c-d-e-f-g-h-987[abcde]',
    'not-a-real-room-404[oarel]',
    'totally-real-room-200[decoy]'
]

regex_pattern = r'([a-z]+\-)+'


class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self.name = self.get_name()
        self.sector_id = self.get_sector_id()
        self.checksum = self.get_checksum()
        self.real_name = self.get_real_name()

    def get_name(self):
        name_match = re.compile(regex_pattern).match(self.room_name)
        return name_match.group().rstrip('-')

    def get_sector_id(self):
        last_hyphen = [m.start() for m in re.finditer('-', self.room_name)][-1]
        beginning_index = last_hyphen + 1
        end_index = self.room_name.find('[')

        return int(self.room_name[beginning_index:end_index])

    def get_checksum(self):
        beginning_index = self.room_name.find('[') + 1
        end_index = self.room_name.find(']')

        return self.room_name[beginning_index:end_index]

    def get_real_name(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz' * 100

        def translate(char, steps):
            if char == '-':
                return ' '
            else:
                new_index = alphabet.find(char) + steps
                return alphabet[new_index]

        exploded = [translate(char, self.sector_id) for char in list(self.name)]
        return ''.join(exploded)


def read_input_file():
    return open('input', 'r').read().splitlines()


def validate(room):
    no_hyphens = room.name.replace("-", "")
    counts = {char: str(no_hyphens.count(char)) for char in set(no_hyphens)}
    count_frequencies = {}
    for char, value in counts.items():
        if value in count_frequencies.keys():
            count_frequencies[value].append(char)
        else:
            count_frequencies[value] = [char]

    order = []
    for frequency in iter(sorted(count_frequencies, reverse=True)):
        order = order + sorted(count_frequencies[frequency])

    return not any([char not in order[:5] for char in room.checksum])


def get_sum_of_real_rooms(input_data):
    sum_of_real_rooms = 0
    for name in input_data:
        room = Room(name)
        if validate(room):
            sum_of_real_rooms += room.sector_id
    return sum_of_real_rooms


def get_north_pole_id(input_data):
    for name in input_data:
        room = Room(name)
        if validate(room):
            if 'pole' in room.real_name:
                return room.sector_id


def test():
    assert get_sum_of_real_rooms(test_input) == 1514


def main():
    input_data = read_input_file()
    print('Day 04 Part 1:', get_sum_of_real_rooms(input_data))
    print('Day 04 Part 2:', get_north_pole_id(input_data))


if __name__ == "__main__":
    main()
