import re
import math

weapons = [
    {'name': 'Dagger', 'cost': 8, 'dmg': 4},
    {'name': 'Shortsword', 'cost': 10, 'dmg': 5},
    {'name': 'Warhammer', 'cost': 25, 'dmg': 6},
    {'name': 'Longsword', 'cost': 40, 'dmg': 7},
    {'name': 'Greataxe', 'cost': 74, 'dmg': 8}
]

armours = [
    {'name': 'None', 'cost': 0, 'def': 0},  # It's not necessary to wear armour
    {'name': 'Leather', 'cost': 13, 'def': 1},
    {'name': 'Chainmail', 'cost': 31, 'def': 2},
    {'name': 'Splintmail', 'cost': 53, 'def': 3},
    {'name': 'Bandedmail', 'cost': 75, 'def': 4},
    {'name': 'Platemail', 'cost': 102, 'def': 5},
]

rings = [
    {'name': 'None', 'cost': 0, 'def': 0, 'dmg': 0},    # It's not necessary to wear rings
    {'name': 'None', 'cost': 0, 'def': 0, 'dmg': 0},
    {'name': 'DMG+1', 'cost': 25, 'def': 0, 'dmg': 1},
    {'name': 'DMG+2', 'cost': 50, 'def': 0, 'dmg': 2},
    {'name': 'DMG+3', 'cost': 100, 'def': 0, 'dmg': 3},
    {'name': 'DEF+1', 'cost': 20, 'def': 1, 'dmg': 0},
    {'name': 'DEF+2', 'cost': 40, 'def': 2, 'dmg': 0},
    {'name': 'DEF+3', 'cost': 80, 'def': 3, 'dmg': 0}
]

hp_pattern = r'Hit Points: (\d+)'
damage_pattern = r'Damage: (\d+)'
armor_pattern = r'Armor: (\d+)'


class Character(object):
    name = ''
    hp = 0
    damage = 0
    armor = 0

    def __init__(self, name, hp=100, damage=0, armor=0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def __repr__(self):
        return self.name + ' -> HP: ' + str(self.hp) + ', Damage: ' + str(self.damage) + ', Armor: ' + str(self.armor) \
               + ' |'


def read_input_file():
    return open('input', 'r').read().splitlines()


def parse_boss_stats(input_data):
    boss_hp = int(re.match(hp_pattern, input_data[0]).group(1))
    boss_damage = int(re.match(damage_pattern, input_data[1]).group(1))
    boss_armor = int(re.match(armor_pattern, input_data[2]).group(1))
    return Character('Boss', boss_hp, boss_damage, boss_armor)


def create_players(input_data):
    player = Character('Redpike', 100)
    boss = parse_boss_stats(input_data)
    return player, boss


def make_combo_of_rings():
    ring_combos = []
    for i in range(0, len(rings)):
        for j in range(i + 1, len(rings)):
            ring_combos.append([rings[i], rings[j]])
    return ring_combos


def start_game(input_data):
    player, boss = create_players(input_data)
    min_cost = 999
    max_cost = 0
    ring_combos = make_combo_of_rings()
    for weapon in weapons:
        for armour in armours:
            for ring in ring_combos:
                r1 = ring[0]
                r2 = ring[1]
                player.damage = weapon['dmg'] + r1['dmg'] + r2['dmg']
                player.armor = armour['def'] + r1['def'] + r2['def']
                cost = weapon['cost'] + armour['cost'] + r1['cost'] + r2['cost']
                pd = max(player.damage - boss.armor, 1)
                bd = max(boss.damage - player.armor, 1)
                pm = math.ceil(boss.hp / pd)
                bm = math.ceil(player.hp / bd)
                if pm <= bm:
                    if cost < min_cost:
                        min_cost = cost
                else:
                    if cost > max_cost:
                        max_cost = cost
    return min_cost, max_cost


def main():
    input_data = read_input_file()
    min_cost, max_cost = start_game(input_data)
    print('Day 21 Part 1:', min_cost)
    print('Day 21 Part 2:', max_cost)


if __name__ == '__main__':
    main()
