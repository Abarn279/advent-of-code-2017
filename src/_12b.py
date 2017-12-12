from file_importer import FileImporter
from queue import Queue

# Dictionary of program ID to list of connecting program IDs
inp = {int(i.split(" <-> ")[0]): list(map(int, i.split(" <-> ")[1].split(', '))) for i in FileImporter.get_input("/../input/12.txt").split('\n')}

allIds = set(i for i in inp.keys())
groups = 0

while len(allIds) > 0:
    q = Queue()
    contained = set([0]) # Start with 0
    q.put(inp[min(allIds)])

    while not q.empty():
        for program in q.get():
            if not program in contained: 
                contained.add(program)
                q.put(inp[program])
    
    allIds = allIds - contained # Get the set of allIds minus the group that was just found
    groups += 1

print(groups)