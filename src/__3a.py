from file_importer import FileImporter
import math

def expandGrid(grid):
    '''Expands a grid in 1 direction on each side with temp 0 vals'''
    for rowInd in range(len(grid)):
        grid[rowInd] = [0] + grid[rowInd] + [0]

    newRow = [0 for i in range(len(grid) + 2)]
    grid = [newRow] + grid + [newRow[:]]
    return grid

def getFinal(grid, row, col):
    '''Takes in a grid, and a row and col of final answer, return steps'''
    center = math.floor(len(grid) / 2)
    return int(math.fabs(row - center) + math.fabs(col - center))

def day3(grid, final):
    '''Full calculation'''

    # Each loop is going to expand the square by one
    while True:
        currentNum = grid[-2][-2]
        
        # Spiral up. Column is constant
        for i in reversed(range(len(grid) - 1)):
            currentNum += 1
            grid[i][len(grid) - 1] = currentNum
            if currentNum == final:
                return getFinal(grid, i, len(grid) - 1)

        # Spiral left. Row is constant.
        for i in reversed(range(len(grid) - 1)):
            currentNum += 1
            grid[0][i] = currentNum
            if currentNum == final:
                return getFinal(grid, 0, i)

        # Spiral down. Column is constant
        for i in range(1, len(grid)):
            currentNum += 1
            grid[i][0] = currentNum
            if currentNum == final:
                return getFinal(grid, i, 0)

        # Spiral right. Row is constant.
        for i in range(1, len(grid)):
            currentNum += 1
            grid[len(grid) - 1][i] = currentNum
            if currentNum == final:
                return getFinal(grid, len(grid) - 1, i)
        
        grid = expandGrid(grid)

inp = FileImporter.get_input("/../input/3.txt")

grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] # Index by row, col

print(day3(grid, int(inp)))