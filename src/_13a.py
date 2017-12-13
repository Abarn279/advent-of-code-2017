from file_importer import FileImporter
from enum import Enum

inp = [list(map(int, i.split(": "))) for i in FileImporter.get_input("/../input/13.txt").split('\n')]

class Scanner:
    def __init__(self, rang):
        self.rang = rang

    def get_pos(self, ps):
        indRang = self.rang - 1
        return abs(indRang - ((ps + indRang) % (indRang*2)))

delay = 0
scanners = [None for x in range(inp[-1][0] + 1)] 
for i in inp:
    scanners[i[0]] = Scanner(i[1])                                        

severity = 0
found = False
for i in range(len(scanners)):
    if scanners[i] is None:
        continue

    pos = scanners[i].get_pos(i)
    if pos == 0:
        severity += i * scanners[i].rang

print(severity)