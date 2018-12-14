_input = 765071


def get_digits_from_input(_input_num: int):
    return [int(digit) for digit in str(_input_num)]


def get_scores(__input: int):
    scores = [3, 7]
    elf1, elf2 = 0, 1
    while len(scores) < __input + 10:
        total = scores[elf1] + scores[elf2]
        scores.extend(divmod(total, 10) if total >= 10 else (total,))

        elf1 = (elf1 + 1 + scores[elf1]) % len(scores)
        elf2 = (elf2 + 1 + scores[elf2]) % len(scores)

    return ''.join(str(score) for score in scores[__input: __input + 10])


def get_recipes(__input: int):
    scores = [3, 7]
    elf1, elf2 = 0, 1
    digits = get_digits_from_input(__input)
    while scores[-len(digits):] != digits and scores[-len(digits) - 1: -1] != digits:
        total = scores[elf1] + scores[elf2]
        scores.extend(divmod(total, 10) if total >= 10 else (total,))

        elf1 = (elf1 + 1 + scores[elf1]) % len(scores)
        elf2 = (elf2 + 1 + scores[elf2]) % len(scores)

    return len(scores) - len(digits) - (0 if scores[-len(digits):] == digits else 1)


def main():
    print('Day 14 Part 1:', get_scores(_input))
    print('Day 14 Part 2:', get_recipes(_input))


if __name__ == '__main__':
    main()
