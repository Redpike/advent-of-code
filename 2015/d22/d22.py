# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
import random
import re

hp_pattern = r'Hit Points: (\d+)'
damage_pattern = r'Damage: (\d+)'

spells = [
    {'name': 'Magic Missile',   'cost': 53,     'damage': 4, 'heal': 0, 'mana': 0,      'armor': 0, 'turns': 0},
    {'name': 'Drain',           'cost': 73,     'damage': 2, 'heal': 2, 'mana': 0,      'armor': 0, 'turns': 0},
    {'name': 'Shield',          'cost': 113,    'damage': 0, 'heal': 0, 'mana': 0,      'armor': 7, 'turns': 6},
    {'name': 'Poison',          'cost': 173,    'damage': 3, 'heal': 0, 'mana': 0,      'armor': 0, 'turns': 6},
    {'name': 'Recharge',        'cost': 229,    'damage': 0, 'heal': 0, 'mana': 101,    'armor': 0, 'turns': 5}
]


class Character(object):
    name = ''
    hp = 0
    mana = 0
    damage = 0
    armor = 0
    effect = ''
    duration = 0

    def __init__(self, name, hp, mana=0, damage=0, armor=0):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.damage = damage
        self.armor = armor

    def put_effect(self, effect, duration):
        if len(self.effect) == 0:
            self.effect = effect
            self.duration = duration

    def is_effect_on_character(self, spell_name):
        if spell_name == 'Shield' and self.armor > 0 \
                or spell_name == 'Poison' and self.duration > 0 \
                or spell_name == 'Recharge' and self.duration > 0:
            return True
        else:
            return False

    def use_effect_for_boss(self):
        if self.effect == 'Poison':
            self.hp -= 3
            self.duration -= 1

    def use_effect_for_player(self):
        if self.effect == 'Shield':
            self.armor = 7
            self.duration = 6
        elif self.effect == 'Recharge':
            self.mana += 101
            self.duration -= 1

    def __repr__(self):
        return '[' + self.name + ' -> HP: ' + str(self.hp) + ', Mana: ' + str(self.mana) \
                + ', Effect: ' + self.effect + ', Duration of Effect: ' + str(self.duration)


# TEST INPUTS
test_player = Character('Test Player', 10, 250)
test_boss_1 = Character('Test Boss 1', 13, 0, 8)
test_boss_2 = Character('Test Boss 2', 14, 0, 8)
optimum = 100_000


def read_input_file():
    return open('input', 'r').read().splitlines()


def parse_boss_stats(input_data):
    boss_hp = int(re.match(hp_pattern, input_data[0]).group(1))
    boss_damage = int(re.match(damage_pattern, input_data[1]).group(1))
    return Character('Boss', boss_hp, 0, boss_damage, 0)


def create_players(input_data):
    player = Character('Redpike', 100)
    boss = parse_boss_stats(input_data)
    return player, boss


def simulate_fight(player, boss):
    mana_spent = 0
    for turn in range(50):
        if mana_spent > optimum:
            return 0

        boss.use_effect_for_boss()
        player.use_effect_for_boss()

        if turn % 2 == 0:
            while True:
                spell = random.choice(spells)
                print(spell['name'])
                if player.is_effect_on_character(spell['name']) or boss.is_effect_on_character(spell['name']):
                    continue
                else:
                    break
            mana_spent += spell['cost']
            if spell['name'] == 'Magic Missile':
                boss.hp -= spell['damage']
                player.mana -= spell['cost']
            elif spell['name'] == 'Drain':
                boss.hp -= spell['damage']
                player.hp += spell['heal']
                player.mana -= spell['cost']



def test():
    assert simulate_fight(test_player, test_boss_1)
    assert simulate_fight(test_player, test_boss_2)


def main():
    test()
    input_data = read_input_file()
    player, boss = create_players(input_data)
    simulate_fight(player, boss)
    print('Day 22 Part 1:', )
    print('Day 22 Part 2:', )


if __name__ == '__main__':
    main()
