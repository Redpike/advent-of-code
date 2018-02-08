import functools

operands = {
    None: lambda arg: arg(0),
    "NOT": lambda arg: ~arg(1),
    "AND": lambda arg: arg(0) & arg(2),
    "OR": lambda arg: arg(0) | arg(2),
    "LSHIFT": lambda arg: arg(0) << arg(2),
    "RSHIFT": lambda arg: arg(0) >> arg(2)
}


class AssemblySignal:
    def __init__(self, operators, commands):
        self._operators = operators
        self._commands = commands

    @functools.lru_cache()
    def get(self, key):
        try:
            value = int(key)
        except ValueError:
            cmd = self._commands[key].split(' ')
            operator = self._parse_operator(cmd)
            argument = functools.partial(self._get_argument, cmd)
            value = self._operators[operator](argument)

        return value

    def replace(self, update):
        return AssemblySignal(self._operators, {**self._commands, **update})

    def _parse_operator(self, cmd):
        return next((x for x in self._operators if x in cmd), None)

    def _get_argument(self, cmd, index):
        return self.get(cmd[index])


def readInputFile():
    return open('input', 'r').readlines()


def parseData(input_data):
    pairs = (x.strip().split(' -> ') for x in input_data)
    return {k: v for v, k in pairs}


def main():
    input_data = readInputFile()
    parsed_data = parseData(input_data)
    part1 = AssemblySignal(operands, parsed_data)
    part2 = part1.replace({'b': str(part1.get('a'))})
    print('Day 07 Part 1:', part1.get('a'))
    print('Day 07 Part 2:', part2.get('a'))


if __name__ == "__main__":
    main()
