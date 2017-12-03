from file_importer import FileImporter
import math

def expandGrid(grid):
    '''Expands a grid in 1 direction on each side with temp 0 vals'''
    for rowInd in range(len(grid)):
        grid[rowInd] = [0] + grid[rowInd] + [0]

    newRow = [0 for i in range(len(grid) + 2)]
    grid = [newRow] + grid + [newRow[:]]
    return grid

def getSumOfNeighbors(grid, row, col):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if row + i < 0 or row + i == len(grid) or col + j < 0 or col + j == len(grid):
                continue
            sum += grid[row + i][col + j]
    return sum

def day3(grid, final):
    '''Full calculation'''

    # Each loop is going to expand the square by one
    while True:
        # Spiral up. Column is constant
        for i in reversed(range(len(grid) - 1)):
            newValue = getSumOfNeighbors(grid, i, len(grid) - 1)
            grid[i][len(grid) - 1] = newValue
            if newValue > final:
                return newValue

        # Spiral left. Row is constant.
        for i in reversed(range(len(grid) - 1)):
            newValue = getSumOfNeighbors(grid, 0, i)
            grid[0][i] = newValue
            if newValue > final:
                return newValue

        # Spiral down. Column is constant
        for i in range(1, len(grid)):
            newValue = getSumOfNeighbors(grid, i, 0)
            grid[i][0] = newValue
            if newValue > final:
                return newValue

        # Spiral right. Row is constant.
        for i in range(1, len(grid)):
            newValue = getSumOfNeighbors(grid, len(grid) - 1, i)
            grid[len(grid) - 1][i] = newValue
            if newValue > final:
                return newValue
        
        grid = expandGrid(grid)

inp = FileImporter.get_input("/../input/3.txt")

grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] # Index by row, col

print(day3(grid, int(inp)))