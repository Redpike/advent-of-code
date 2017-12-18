from collections import defaultdict

test_input = [
    'set a 1',
    'add a 2',
    'mul a a',
    'mod a 5',
    'snd a',
    'set a 0',
    'rcv a',
    'jgz a -1',
    'set a 1',
    'jgz a -2'
]

test_input2 = [
    'snd 1',
    'snd 2',
    'snd p',
    'rcv a',
    'rcv b',
    'rcv c',
    'rcv d'
]


class State(object):
    def __init__(self, num, instruction):
        self.id_ = num
        self.index = 0
        self.instruction = instruction
        self.registers = defaultdict(int)
        self.registers['p'] = num
        self.sends = []
        self.send_count = 0
        self.other = None
        self.terminated = False

    def canRun(self):
        if self.terminated:
            return False
        try:
            rcv = self.instruction[self.index].split()[0] == 'rcv'
            if rcv:
                return len(self.other.sends) > 0
        except IndexError:
            return False
        return True

    def doNextInstruction(self):
        if not self.canRun():
            return

        if self.terminated:
            return
        try:
            instruction = self.instruction[self.index]
        except IndexError:
            self.terminated = True
            return
        command, *arguments = instruction.split()
        if command == 'snd':
            self.sends.append(getValue(self.registers, arguments[0]))
            self.send_count += 1
            self.index += 1
        elif command == 'set':
            self.registers[arguments[0]] = getValue(self.registers, arguments[1])
            self.index += 1
        elif command == 'add':
            self.registers[arguments[0]] += getValue(self.registers, arguments[1])
            self.index += 1
        elif command == 'mul':
            self.registers[arguments[0]] *= getValue(self.registers, arguments[1])
            self.index += 1
        elif command == 'mod':
            self.registers[arguments[0]] %= getValue(self.registers, arguments[1])
            self.index += 1
        elif command == 'rcv':
            self.registers[arguments[0]] = self.other.sends.pop(0)
            self.index += 1
        elif command == 'jgz':
            if getValue(self.registers, arguments[0]) > 0:
                self.index += getValue(self.registers, arguments[1])
            else:
                self.index += 1


def readInputFile():
    input_file = open('input', 'r')
    input_data = []
    for line in input_file:
        line = line.strip('\n')
        input_data.append(line)
    return input_data


def getValue(registers, value):
    try:
        return int(value)
    except ValueError:
        return registers[value]


def getRecoveredFrequency(input_data):
    registers = defaultdict(int)
    index = 0
    last_played = None

    while True:
        instruction = input_data[index]
        command, *arguments = instruction.split()
        if command == 'snd':
            last_played = getValue(registers, arguments[0])
            index += 1
        elif command == 'set':
            registers[arguments[0]] = getValue(registers, arguments[1])
            index += 1
        elif command == 'add':
            registers[arguments[0]] += getValue(registers, arguments[1])
            index += 1
        elif command == 'mul':
            registers[arguments[0]] *= getValue(registers, arguments[1])
            index += 1
        elif command == 'mod':
            registers[arguments[0]] %= getValue(registers, arguments[1])
            index += 1
        elif command == 'rcv':
            if getValue(registers, arguments[0]) != 0:
                return last_played
            index += 1
        elif command == 'jgz':
            if getValue(registers, arguments[0]) > 0:
                index += getValue(registers, arguments[1])
            else:
                index += 1


def sendValue(input_data):
    p0 = State(0, input_data)
    p1 = State(1, input_data)
    p0.other = p1
    p1.other = p0
    while True:
        p0.doNextInstruction()
        p1.doNextInstruction()
        if not p0.canRun() and not p1.canRun():
            break
    return p1.send_count


def test():
    assert getRecoveredFrequency(test_input) == 4
    assert sendValue(test_input2) == 3


def main():
    test()
    input_data = readInputFile()
    print('Day 18 Part 1:', getRecoveredFrequency(input_data))
    print('Day 18 Part 2:', sendValue(input_data))


if __name__ == '__main__':
    main()
