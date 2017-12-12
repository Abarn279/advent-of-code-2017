from file_importer import FileImporter
from queue import Queue

# Dictionary of program ID to list of connecting program IDs
inp = {int(i.split(" <-> ")[0]): list(map(int, i.split(" <-> ")[1].split(', '))) for i in FileImporter.get_input("/../input/12.txt").split('\n')}

q = Queue()
contained = set([0]) # Start with 0
q.put(inp[0])

while not q.empty():
    for program in q.get():
        if not program in contained: 
            contained.add(program)
            q.put(inp[program])

print(len(contained))
