def readInputFile():
    input_file = open('input', 'r')
    data = []
    for line in input_file:
        line = line.strip('\n').split()
        data.append(list(map(int, line)))
    return data


def findMaxPosition(input_list):
    max_position = 0
    max_value = 0
    for i in range(len(input_list)):
        if input_list[i] > max_value:
            max_value = input_list[i]
            max_position = i
    return max_position


def distributeBlocks(input_list, max_position):
    current_dritributed_list = list(input_list)
    max_element = current_dritributed_list[max_position]
    current_dritributed_list[max_position] = 0
    current_index = max_position
    while max_element > 0:
        current_index = (current_index + 1) % len(current_dritributed_list)
        current_dritributed_list[current_index] += 1
        max_element -= 1
    return current_dritributed_list


def countCycles(input_data):
    distributed_banks = input_data
    cycle_counter = 0
    while True:
        current_list = list(input_data[cycle_counter])
        max_position = findMaxPosition(current_list)
        current_list = list(distributeBlocks(current_list, max_position))
        cycle_counter += 1
        if current_list not in distributed_banks:
            distributed_banks.append(current_list)
        else:
            return cycle_counter


def test():
    assert countCycles([[0, 2, 7, 0]]) == 5


def main():
    test()
    input_data = readInputFile()
    print("Day 6 Part 1:", countCycles(input_data))


if __name__ == '__main__':
    main()
