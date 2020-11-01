from file_importer import FileImporter
from numpy import rot90, flip, array

rules = {i.split(" => ")[0]: i.split(" => ")[1] for i in FileImporter.get_input("/../input/21.txt").split("\n")}

def to_rule_string(grid):
    s = ""
    for y in grid:
        for x in y:
            s += x
        s += '/'
    return s[:-1]

def to_grid(string):
    return [list(j) for j in [i for i in string.split('/')]]

def get_permutations(grid):
    permutations = []

    rotated = grid[:]
    for i in range(4):
        rotated = rot90(rotated)
        flipped = flip(rotated, 1)
        permutations.append(rotated)
        permutations.append(flipped)
    
    return [i.tolist() for i in permutations]

def get_subgrid(grid, x, y, size):
    g = []

    ny = 0
    for zy in range(y, y + size):
        g.append([])

        for zx in range(x, x + size):
            g[ny].append(grid[zy][zx])

        ny += 1
    return g

grid = array([
    ['.', '#', '.'], 
    ['.', '.', '#'], 
    ['#', '#', '#']
])

rule_translations = {}

for iteration in range(18):
    print(iteration)

    new_grid = []

    size = 2 if len(grid) % 2 == 0 else 3

    for y in range(0, len(grid), size):

        for x in range(0, len(grid), size):
            subgrid = get_subgrid(grid, x, y, size)

            found_rs = None
            base_rs = to_rule_string(subgrid)
            if base_rs in rule_translations:
                found_rs = rule_translations[base_rs]
            else:
                perms = get_permutations(subgrid)
            
                for perm in perms: 
                    rule_string = to_rule_string(perm)
                    if rule_string in rules:
                        found_rs = rule_string
                        rule_translations[base_rs] = found_rs
                        break

            if found_rs == None:
                raise Exception("!")

            new_subgrid = to_grid(rules[found_rs])
            
            ny_i = (y // size) * (size + 1) # what y to start at for expanded grid
            for ny in new_subgrid:

                if len(new_grid) < ny_i + 1:
                    new_grid.append([])

                for nx in ny:
                    new_grid[ny_i].append(nx)
                
                ny_i += 1

    grid = new_grid

print(sum(1 for i in array(grid).flatten() if i == '#')) 