import sys
sys.path.append('..')

from d10.d10 import createKnotHashWithInput
from scipy.ndimage.measurements import label


input_data = 'hxtvlmkl'
test_data = 'flqrgnkx'
matrix = []


def createGrid(input_data_p):
    global matrix
    matrix = []
    grid = []
    for i in range(128):
        temp_string = input_data_p + '-' + str(i)
        knot_hash_string = createKnotHashWithInput(temp_string)
        bin_knot_hash_string = bin(int(knot_hash_string, 16))[2:].zfill(128)
        grid.append(str(bin_knot_hash_string))
        matrix.append(list(map(int, bin_knot_hash_string)))
    return grid


def countSquares(grid):
    squares = 0
    for item in grid:
        squares += str(item).count('1')
    return squares


# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.ndimage.measurements.label.html#scipy.ndimage.measurements.label -> awesome
def countRegions():
    regions = label(matrix)[1]
    return regions


def test():
    grid = createGrid(test_data)
    assert countSquares(grid) == 8108
    assert countRegions() == 1242


def main():
    test()
    grid = createGrid(input_data)
    print('Day 14 Part 1:', countSquares(grid))
    print('Day 14 Part 2:', countRegions())


if __name__ == '__main__':
    main()