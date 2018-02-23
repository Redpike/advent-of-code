from sys import maxsize
from copy import deepcopy

# name, mana cost, damage, heal, armor, mana charge, turns
missile = ('Magic Missile', 53, 4, 0, 0, 0, 0)
drain = ('Drain', 73, 2, 2, 0, 0, 0)
shield = ('Shield', 113, 0, 0, 7, 0, 6)
poison = ('Poison', 173, 3, 0, 0, 0, 6)
recharge = ('Recharge', 229, 0, 0, 0, 101, 5)
spells = [missile, drain, shield, poison, recharge]

at_least_mana_used = maxsize
part_2 = False


def simulate_fight(boss_hp, player_hp, player_mana, active_spells, player_turn, total_mana_used):
    boss_dmg = 10
    player_armor = 0

    if part_2 and player_turn:
        player_hp -= 1
        if player_hp <= 0:
            return False

    new_active_spells = []
    for active_spell in active_spells:
        if active_spell[6] >= 0:
            boss_hp -= active_spell[2]
            player_hp += active_spell[3]
            player_armor += active_spell[4]
            player_mana += active_spell[5]
        new_active_spell = (
            active_spell[0], active_spell[1], active_spell[2], active_spell[3], active_spell[4], active_spell[5],
            active_spell[6] - 1)
        if new_active_spell[6] > 0:
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
                if new_active_spells[j][0] == spell[0]:
                    is_spell_activated = True
                    break
            spell_cost = spell[1]
            if spell_cost <= player_mana and not is_spell_activated:
                a = deepcopy(new_active_spells)
                a.append(spell)
                simulate_fight(boss_hp, player_hp, player_mana - spell_cost, a, False,
                               total_mana_used + spell_cost)
    else:
        player_hp -= (boss_dmg - player_armor) if (boss_dmg - player_armor) > 0 else 1
        if player_hp > 0:
            simulate_fight(boss_hp, player_hp, player_mana, new_active_spells, True, total_mana_used)


def main():
    global at_least_mana_used
    print('Day 22 Part 1:', simulate_fight(71, 50, 500, [], True, 0), at_least_mana_used)
    global part_2
    part_2 = True
    at_least_mana_used = maxsize
    print('Day 22 Part 1:', simulate_fight(71, 50, 500, [], True, 0), at_least_mana_used)


if __name__ == '__main__':
    main()
