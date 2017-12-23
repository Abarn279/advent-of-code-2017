from file_importer import FileImporter
from collections import defaultdict
import re

def get_value(arg2): 
    return int(arg2) if re.match("[+-]?\d", arg2) is not None else int(registers[arg2])

inp = [i.split() for i in FileImporter.get_input("/../input/23.txt").split('\n')]
registers = defaultdict(lambda: 0)
instIndex = 0
mul_t = 0
while instIndex < len(inp):
    curr = inp[instIndex]
    if curr[0] == 'set':
        registers[curr[1]] = get_value(curr[2])
    elif curr[0] == 'sub':
        registers[curr[1]] -= get_value(curr[2])
    elif curr[0] == 'mul':
        registers[curr[1]] *= get_value(curr[2])
        mul_t += 1
    elif curr[0] == 'jnz':
        if get_value(curr[1]) != 0:
            instIndex += get_value(curr[2])
            continue

    instIndex += 1

print(mul_t)