test_data = 5
input_data = 3001330


class Elf(object):
    n = 0

    def __init__(self, right=None):
        self.left = None
        self.right = right
        Elf.n += 1
        self.n = Elf.n

    def remove_self(self):
        self.left.right = self.right
        self.right.left = self.left
        return self.left


def play_a_game(elves_no: int, part_two=False):
    Elf.n = 0
    first_elf = Elf()
    last_elf = first_elf
    for i in range(elves_no - 1):
        new_elf = Elf(right=last_elf)
        last_elf.left = new_elf
        last_elf = new_elf
    last_elf.left = first_elf
    total_elves = elves_no

    current_elf = first_elf
    if part_two:
        for _ in range(elves_no // 2):
            current_elf = current_elf.left
    else:
        current_elf = current_elf.left

    while total_elves > 1:
        if part_two:
            current_elf = current_elf.remove_self()
            if total_elves % 2 == 1:
                current_elf = current_elf.left
        else:
            current_elf = current_elf.remove_self().left
        total_elves -= 1

    return current_elf.n


def test():
    assert play_a_game(test_data, part_two=True) == 2


def main():
    test()
    print('Day 19 Part 1', play_a_game(input_data))
    print('Day 19 Part 2', play_a_game(input_data, part_two=True))


if __name__ == '__main__':
    main()
