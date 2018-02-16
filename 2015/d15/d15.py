import re
from itertools import combinations_with_replacement

test_input = [
    'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
    'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
]

regex_pattern = r'(\w+): capacity (-?\d+){1}, durability (-?\d+){1}, flavor (-?\d+){1}, texture (-?\d+){1},' \
                r' calories (-?\d+){1}'


class Component(object):
    name = ''
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    def __init__(self, name='', capacity=0, durability=0, flavor=0, texture=0, calories=0):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def __str__(self):
        return self.name, self.capacity, self.durability, self.flavor, self.texture, self.calories

    def __repr__(self):
        return self.name + ' ,c: ' + str(self.capacity) + ' ,d: ' + str(self.durability) + ' ,f: ' + \
               str(self.flavor) + ' ,t: ' + str(self.texture) + ' ,c: ' + str(self.calories)


def read_input_file():
    return open('input', 'r').read().splitlines()


def parse_component_data(line):
    try:
        regex_match = re.match(regex_pattern, line)
        component = Component(regex_match.group(1), int(regex_match.group(2)), int(regex_match.group(3)),
                              int(regex_match.group(4)), int(regex_match.group(5)), int(regex_match.group(6)))
    except Exception:
        raise Warning('Can\'t match regex!')

    return component


def get_components(input_data):
    components = []
    for line in input_data:
        component = parse_component_data(line)
        components.append(component)

    return components


def compute_total_score(components):
    max_score = 0
    for coockie in combinations_with_replacement(components, 100):
        total_capacity, total_durability, total_flavor, total_texture = 0, 0, 0, 0
        for component in coockie:
            total_capacity += component.capacity
            total_durability += component.durability
            total_flavor += component.flavor
            total_texture += component.texture
            if total_capacity <= 0 or total_durability <= 0 or total_flavor <= 0 or total_texture <= 0:
                continue
            score = total_capacity * total_durability * total_flavor * total_texture
            if score > max_score:
                max_score = score

    return max_score


def compute_total_score_with_calories(components):
    max_score = 0
    for cookie in combinations_with_replacement(components, 100):
        total_capacity, total_durability, total_flavor, total_texture, total_calories = 0, 0, 0, 0, 0
        for component in cookie:
            total_capacity += component.capacity
            total_durability += component.durability
            total_flavor += component.flavor
            total_texture += component.texture
            total_calories += component.calories
            if total_capacity <= 0 or total_durability <= 0 or total_flavor <= 0 or total_texture <= 0:
                continue
            if total_calories != 500:
                continue
            score = total_capacity * total_durability * total_flavor * total_texture
            if score > max_score:
                max_score = score

    return max_score


def get_total_score(input_data, part):
    components = get_components(input_data)
    if part == 1:
        total_score = compute_total_score(components)
    else:
        total_score = compute_total_score_with_calories(components)
    return total_score


def test():
    assert get_total_score(test_input, 1) == 62842880
    assert get_total_score(test_input, 2) == 57600000


def main():
    test()
    input_file = read_input_file()
    print('Day 15 Part 1:', get_total_score(input_file, 1))
    print('Day 15 Part 2:', get_total_score(input_file, 2))


if __name__ == '__main__':
    main()
