import re
from copy import deepcopy
from sys import maxsize

spells = [
    {'name': 'Magic Missile', 'cost': 53, 'damage': 4, 'heal': 0, 'armor': 0, 'mana': 0, 'duration': 0},
    {'name': 'Drain', 'cost': 73, 'damage': 2, 'heal': 2, 'armor': 0, 'mana': 0, 'duration': 0},
    {'name': 'Shield', 'cost': 113, 'damage': 0, 'heal': 0, 'armor': 7, 'mana': 0, 'duration': 6},
    {'name': 'Poison', 'cost': 173, 'damage': 3, 'heal': 0, 'armor': 0, 'mana': 0, 'duration': 6},
    {'name': 'Recharge', 'cost': 229, 'damage': 0, 'heal': 0, 'armor': 0, 'mana': 101, 'duration': 5}
]

at_least_mana_used = maxsize
part_2 = False

hp_pattern = r'Hit Points: (\d+)'
damage_pattern = r'Damage: (\d+)'


def read_input_file():
    lines = open('input').read().splitlines()
    boss_hp = int(re.match(hp_pattern, lines[0]).group(1))
    boss_damage = int(re.match(damage_pattern, lines[1]).group(1))
    return boss_hp, boss_damage


def prepare_new_spell(active_spell):
    name = active_spell['name']
    cost = active_spell['cost']
    damage = active_spell['damage']
    heal = active_spell['heal']
    armor = active_spell['armor']
    mana = active_spell['mana']
    duration = active_spell['duration'] - 1
    return {'name': name, 'cost': cost, 'damage': damage, 'heal': heal, 'armor': armor, 'mana': mana,
            'duration': duration}


def simulate_fight(boss_hp, boss_damage, player_hp, player_mana, active_spells, player_turn, total_mana_used):
    player_armor = 0

    if part_2 and player_turn:
        player_hp -= 1
        if player_hp <= 0:
            return False

    new_active_spells = []
    for active_spell in active_spells:
        if active_spell['duration'] >= 0:
            boss_hp -= active_spell['damage']
            player_hp += active_spell['heal']
            player_armor += active_spell['armor']
            player_mana += active_spell['mana']

        new_active_spell = prepare_new_spell(active_spell)
        if new_active_spell['duration'] > 0:
            new_active_spells.append(new_active_spell)

    if boss_hp <= 0:
        global at_least_mana_used
        if total_mana_used < at_least_mana_used:
            at_least_mana_used = total_mana_used
        return True

    if total_mana_used >= at_least_mana_used:
        return False

    if player_turn:
        for i in range(len(spells)):
            spell = spells[i]
            is_spell_activated = False
            for j in range(len(new_active_spells)):
                if new_active_spells[j]['name'] == spell['name']:
                    is_spell_activated = True
                    break
            spell_cost = spell['cost']
            if spell_cost <= player_mana and not is_spell_activated:
                a = deepcopy(new_active_spells)
                a.append(spell)
                simulate_fight(boss_hp, boss_damage, player_hp, player_mana - spell_cost, a, False,
                               total_mana_used + spell_cost)
    else:
        player_hp -= (boss_damage - player_armor) if (boss_damage - player_armor) > 0 else 1
        if player_hp > 0:
            simulate_fight(boss_hp, boss_damage, player_hp, player_mana, new_active_spells, True, total_mana_used)


def main():
    boss_hp, boss_damage = read_input_file()
    global at_least_mana_used
    simulate_fight(boss_hp, boss_damage, 50, 500, [], True, 0)
    print('Day 22 Part 1:', at_least_mana_used)
    global part_2
    part_2 = True
    at_least_mana_used = maxsize
    simulate_fight(boss_hp, boss_damage, 50, 500, [], True, 0)
    print('Day 22 Part 2:', at_least_mana_used)


if __name__ == '__main__':
    main()
