def readInputFile():
    input_file = open('input', 'r')
    line = input_file.read().split()
    data = [int(x) for x in line]
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


def checkDistanceBeetwenTheSameStates(distributed_blocks, current_list):
    for position in distributed_blocks:
        if position[1] == current_list:
            return position[0]


def countCycles(input_data):
    cycle_counter = 0
    distributed_blocks = [[cycle_counter, input_data]]
    current_list = input_data
    while True:
        cycle_counter += 1
        max_position = findMaxPosition(list(current_list))
        current_list = distributeBlocks(list(current_list), max_position)

        if current_list not in list(zip(*distributed_blocks))[1]:
            distributed_blocks.append([cycle_counter, current_list])
        else:
            distance = checkDistanceBeetwenTheSameStates(distributed_blocks, current_list)
            return cycle_counter - distance


def test():
    assert findMaxPosition([1, 2, 8, 3, 4, 5]) == 2
    assert distributeBlocks([1, 2, 8, 3, 4, 5], 2) == [2, 3, 1, 5, 6, 6]
    assert countCycles([0, 2, 7, 0]) == 4


def main():
    test()
    input_data = readInputFile()
    print("Day 6 Part 2:", countCycles(input_data))


if __name__ == '__main__':
    main()
