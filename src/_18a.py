from file_importer import FileImporter
from collections import defaultdict
import re

inp = [i.split() for i in FileImporter.get_input("/../input/18.txt").split('\n')]
registers = defaultdict(lambda: 0)
lastPlayed = None
instIndex = 0

def get_value(arg2): 
    return int(arg2) if re.match("[+-]?\d", arg2) is not None else int(registers[arg2])

while instIndex < len(inp):
    curr = inp[instIndex]
    if curr[0] == 'snd':
        lastPlayed = registers[curr[1]]
    elif curr[0] == 'set':
        registers[curr[1]] = get_value(curr[2])
    elif curr[0] == 'add':
        registers[curr[1]] += get_value(curr[2])
    elif curr[0] == 'mul':
        registers[curr[1]] *= get_value(curr[2])
    elif curr[0] == 'mod':
        registers[curr[1]] %= get_value(curr[2])
    elif curr[0] == 'rcv':
        if registers[curr[1]] != 0:
            print("recovered val: " + str(lastPlayed))
            break
    elif curr[0] == 'jgz':
        if get_value(curr[1]) > 0:
            instIndex += get_value(curr[2])
            continue

    instIndex += 1
