import numpy
import re

turn_on_inst = 'turn on'
turn_off_inst = 'turn off'
toggle_inst = 'toggle'
regex_pattern = '.* (\d+),(\d+) through (\d+),(\d+)'


def turnOn(matrix, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            matrix[x][y] = 1


def turnOff(matrix, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            matrix[x][y] = 0


def toggle(matrix, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            matrix[x][y] = 1 - matrix[x][y]


def turnOn2(matrix, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            matrix[x][y] += 1


def turnOff2(matrix, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if matrix[x][y]:
                matrix[x][y] -= 1


def toggle2(matrix, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            matrix[x][y] += 2


def readInputFile():
    input_file = open('input', 'r').read()
    input_data = []
    for line in input_file.splitlines():
        input_data.append(line)
    return input_data


def countLitLights(input_data):
    matrix = numpy.zeros((1000, 1000), numpy.int16)
    for instuction in input_data:
        compiled_regex = re.compile(regex_pattern)
        x1, y1, x2, y2 = tuple([int(cord) for cord in compiled_regex.match(instuction).groups()])
        if turn_on_inst in instuction:
            turnOn(matrix, x1, y1, x2, y2)
        elif turn_off_inst in instuction:
            turnOff(matrix, x1, y1, x2, y2)
        elif toggle_inst in instuction:
            toggle(matrix, x1, y1, x2, y2)
        else:
            raise NotImplementedError('No instruction was found')
    lit_lights = numpy.count_nonzero(matrix)
    return lit_lights


def computeTotalBrighntess(input_data):
    matrix = numpy.zeros((1000, 1000), numpy.int16)
    for instuction in input_data:
        compiled_regex = re.compile(regex_pattern)
        x1, y1, x2, y2 = tuple([int(cord) for cord in compiled_regex.match(instuction).groups()])
        if turn_on_inst in instuction:
            turnOn2(matrix, x1, y1, x2, y2)
        elif turn_off_inst in instuction:
            turnOff2(matrix, x1, y1, x2, y2)
        elif toggle_inst in instuction:
            toggle2(matrix, x1, y1, x2, y2)
        else:
            raise NotImplementedError('No instruction was found')
    total_brightness = numpy.sum(matrix)
    return total_brightness


def main():
    input_data = readInputFile()
    print('Day 06 Part 1:', countLitLights(input_data))
    print('Day 06 Part 2:', computeTotalBrighntess(input_data))


if __name__ == '__main__':
    main()
