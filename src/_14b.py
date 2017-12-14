from file_importer import FileImporter
from aocutils import knot_hash

inp = FileImporter.get_input("/../input/14.txt")

def mark_group(grid, row, col, groupNum):
    grid[row][col] = str(groupNum)
    neighbors = []
    if row != 0:
        neighbors.append((row - 1, col))
    if row != len(grid) - 1:
        neighbors.append((row + 1, col))
    if col != 0:
        neighbors.append((row, col - 1))
    if col != len(grid) - 1:
        neighbors.append((row, col + 1))
    for neighbor in neighbors:
        if grid[neighbor[0]][neighbor[1]] == '#':
            mark_group(grid, neighbor[0], neighbor[1], groupNum)

grid = []
for i in range(128):
    khash = knot_hash(inp + '-' + str(i))                          # Get knot hash
    binary = bin(int(khash, 16))[2:].zfill(128)                    # Get binary rep of knot hash, get rid of 0b in front, fill to 128 chars
    grid.append(['#' if i == '1' else '.' for i in binary])       

groupNum = 1
for rowInd in range(len(grid)):
    for colInd in range(len(grid)):
        if grid[rowInd][colInd] == '#':
            mark_group(grid, rowInd, colInd, groupNum)             # Call recursive function to go search and mark all members of this group
            groupNum += 1

print(groupNum - 1)
