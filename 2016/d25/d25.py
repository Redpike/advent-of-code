def read_input_file():
    return open('input', 'r').read().splitlines()


def value(key, dic):
    return dic[key] if key in dic else int(key)


def execute_assembunny_code(instructions: list):
    for ans in range(10_000_000):
        registers = {'a': ans, 'b': 0, 'c': 1, 'd': 0}

        ind = 0
        output = []
        while ind != len(instructions):
            splitted_line = instructions[ind].split(' ')

            if splitted_line[0] == 'inc':
                registers[splitted_line[1]] += 1
            elif splitted_line[0] == 'dec':
                registers[splitted_line[1]] -= 1
            elif splitted_line[0] == 'cpy':
                registers[splitted_line[2]] = value(splitted_line[1], registers)
            elif splitted_line[0] == 'jnz' and value(splitted_line[1], registers) != 0:
                ind += int(splitted_line[2])
                continue
            elif splitted_line[0] == 'out':
                if len(output) == 0 and registers[splitted_line[1]] == 0:
                    output.append(registers[splitted_line[1]])
                elif len(output) == 0 and registers[splitted_line[1]] != 0:
                    break
                elif output[-1] == 0 and registers[splitted_line[1]] == 1:
                    output.append(registers[splitted_line[1]])
                elif (output[-1]) == 1 and registers[splitted_line[1]] == 0:
                    output.append(registers[splitted_line[1]])
                else:
                    break

            if len(output) >= 100:
                return ans
            ind += 1


def main():
    input_data = read_input_file()
    print('Day 25 Part 1:', execute_assembunny_code(input_data))


if __name__ == '__main__':
    main()
