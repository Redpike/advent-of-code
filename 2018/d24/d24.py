import re
import math


class Group:
    def __init__(self, n, hp_each, weaknesses, immunities, atk_dmg, atk_type, initiative, team):
        self.n = n
        self.hp_each = hp_each
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.atk_dmg = atk_dmg
        self.atk_type = atk_type
        self.initiative = initiative
        self.team = team

    def __repr__(self):
        return 'group({!r})'.format(self.__dict__)

    @property
    def eff_power(self):
        return self.n * self.atk_dmg

    def dmg_to(self, other):
        return self.eff_power * (
            0 if self.atk_type in other.immunities else 2 if self.atk_type in other.weaknesses else 1)


def read_input():
    return open('input', 'r').read().splitlines()


def parse(input_data, team, boost=0):
    res = []
    for i in input_data:
        g = re.match(
            r'(\d+) units each with (\d+) hit points (?:\((.*?)\) )?with an attack that does (\d+) (\S+) damage at initiative (\d+)',
            i)
        n = int(g.group(1))
        hp = int(g.group(2))
        weaknesses = set()
        immunities = set()
        wi = g.group(3)
        if wi is not None:
            for cmp in wi.split('; '):
                if cmp.startswith('immune to '):
                    immunities |= set(cmp[len('immune to '):].split(', '))
                elif cmp.startswith('weak to '):
                    weaknesses |= set(cmp[len('weak to '):].split(', '))
        dmg = int(g.group(4))
        typ = g.group(5)
        initiative = int(g.group(6))
        res.append(Group(n, hp, weaknesses, immunities, dmg + boost, typ, initiative, team))
    return res


def get_team(s):
    if s is None:
        return 'stalemate'
    for i in s:
        return i.team


def run_combat(imm_inp, inf_inp, boost=0):
    immune_system = set(parse(imm_inp, 'immune', boost))
    infection = set(parse(inf_inp, 'infection'))
    while immune_system and infection:
        potential_combatants = immune_system | infection
        attacking = {}
        for combatant in sorted(immune_system | infection, key=lambda x: (x.eff_power, x.initiative), reverse=True):
            try:
                s = max((x for x in potential_combatants if x.team != combatant.team and combatant.dmg_to(x) != 0),
                        key=lambda x: (combatant.dmg_to(x), x.eff_power, x.initiative))
            except ValueError:
                attacking[combatant] = None
                continue
            potential_combatants.remove(s)
            attacking[combatant] = s
        did_damage = False
        for combatant in sorted(immune_system | infection, key=lambda x: x.initiative, reverse=True):
            if combatant.n <= 0:
                continue
            atk = attacking[combatant]
            if atk is None:
                continue
            dmg = combatant.dmg_to(atk)
            n_dead = dmg // atk.hp_each
            if n_dead > 0:
                did_damage = True
            atk.n -= n_dead
            if atk.n <= 0:
                immune_system -= {atk}
                infection -= {atk}

        if not did_damage:
            return None
    winner = max(immune_system, infection, key=len)
    return winner


def read_sections(input_data):
    return input_data[1:11], input_data[13:23]


def solve(input_data, part):
    inp_imm, inp_infection = read_sections(input_data)
    winner = run_combat(inp_imm, inp_infection)
    if part == 1:
        return sum(x.n for x in winner)
    else:
        boost_min = 0
        boost_max = 1
        while get_team(run_combat(inp_imm, inp_infection, boost_max)) != 'immune':
            boost_max *= 2

        while boost_min != boost_max:
            pow = (boost_min + boost_max) // 2
            cr = run_combat(inp_imm, inp_infection, pow)
            res = get_team(cr)
            if res != 'immune':
                boost_min = math.ceil((boost_min + boost_max) / 2)
            else:
                boost_max = pow

        return sum(x.n for x in run_combat(inp_imm, inp_infection, boost_max))


def main():
    input_data = read_input()
    print('Day 24 Part 1:', solve(input_data, part=1))
    print('Day 24 Part 2:', solve(input_data, part=2))


if __name__ == '__main__':
    main()
