from file_importer import FileImporter
import math
from collections import defaultdict

def add_tuple(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def get_key(x, y):
    return str(x) + ',' + str(y)

inp = [list(i) for i in FileImporter.get_input("/../input/22.txt").split("\n")]

grid_dic = defaultdict(lambda: '.')

for i in range(len(inp)):
    for j in range(len(inp)):
        grid_dic[get_key(i, j)] =inp[i][j]

# Map of direction number to the vector you'll travel
directions = {  
    0: (0, 1),  # Right
    1: (-1, 0), # Up
    2: (0, -1), # Left
    3: (1, 0),  # Down
}

# Initial position is middle of grid, direction is up. Grid is a square
c_pos = (math.floor(len(inp) / 2), math.floor(len(inp) / 2))
c_dir = 1 

n_infections = 0
for burst_i in range(10000000):
    curr = grid_dic[get_key(c_pos[0], c_pos[1])]
    if curr == '#':    
        c_dir = (c_dir - 1) % 4
        grid_dic[get_key(c_pos[0], c_pos[1])] = 'F'
    elif curr == ".":
        c_dir = (c_dir + 1) % 4
        grid_dic[get_key(c_pos[0], c_pos[1])] = 'W'
    elif curr == "W":
        grid_dic[get_key(c_pos[0], c_pos[1])] = '#'
        n_infections += 1
    elif curr == "F":
        grid_dic[get_key(c_pos[0], c_pos[1])] = '.'
        c_dir = (c_dir + 2) % 4

    c_pos = add_tuple(c_pos, directions[c_dir])          # Move forward in dir

print(n_infections)