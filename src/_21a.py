from file_importer import FileImporter
import numpy

def check_rule(grid, rule):
    srule = rule.split("/")
    if len(srule) != len(grid): 
        return False
    for rowi in range(len(grid)):
        if "".join(grid[rowi]) != srule[rowi]:
            return False
    return True

def get_grid_from_str(string):
    return [list(j) for j in [i for i in string.split("/")]]

class Subgrid:
    def __init__(self, grid):
        self.grid = grid
    def update(self, rules):
        for rule in rules:
            for i in range(4):
                state = numpy.rot90(self.grid, i)
                for st in [state, numpy.flipud(state), numpy.fliplr(state)]:
                    if check_rule(st, rule[0]): # Rotate all, get new grid from rule
                        self.grid = get_grid_from_str(rule[1])
                        return
    def get_active_count(self):
        return sum(1 if self.grid[i][j] == "#" else 0 for i in range(len(self.grid)) for j in range(len(self.grid)))
    def get_split_instances(self):
        if len(self.grid) <= 3: return [self]

        s_subgrid = 3 if len(self.grid) % 3 == 0 else 2

        instances = []
        for i in range(0, len(self.grid), s_subgrid):
            for j in range(0, len(self.grid), s_subgrid):
                newgrid = []
                newgrid.append(self.grid[i][j:j+s_subgrid])
                newgrid.append(self.grid[i+1][j:j+s_subgrid])
                if s_subgrid == 3:
                    newgrid.append(self.grid[i+2][j:j+s_subgrid])
                instances.append(Subgrid(newgrid[:]))
        return instances


inp = [i.split(" => ") for i in FileImporter.get_input("/../input/21.txt").split("\n")]

grid = Subgrid([['.', '#', '.'],
                ['.', '.', '#'],
                ['#', '#', '#']])

grids = [grid]

for i in range(5):
    new_list = []
    for grid in grids:
        new_list = new_list + grid.get_split_instances()
    grids = new_list[:]
    
    for grid in grids:
        grid.update(inp)

print(sum(grid.get_active_count() for grid in grids))