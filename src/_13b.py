from file_importer import FileImporter
from enum import Enum

inp = [list(map(int, i.split(": "))) for i in FileImporter.get_input("/../input/13.txt").split('\n')]

class Scanner:
    def __init__(self, rang):
        self.rang = rang

    def get_pos(self, ps):
        indRang = self.rang - 1
        return abs(indRang - ((ps + indRang) % (indRang*2)))

def part2(inp):
    delay = 0
    while True:
        scanners = [None for x in range(inp[-1][0] + 1)]                  
        for i in inp:
            scanners[i[0]] = Scanner(i[1])                                     

        step = 0
        found = False
        for i in scanners:
            if i is None:
                step += 1 
                continue

            pos = i.get_pos(step + delay)
            if pos == 0:
                found = True
                break
            step += 1

        if not found:
            return delay

        delay += 1

print(part2(inp))