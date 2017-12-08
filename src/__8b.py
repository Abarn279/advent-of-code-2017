from file_importer import FileImporter
from collections import defaultdict
import operator
ops = { '+': operator.add, '>': operator.gt, '<': operator.lt, '>=': operator.ge, '<=': operator.le, '==': operator.eq, '!=': operator.ne, 'inc': operator.add, 'dec': operator.sub }

inp = [i.split() for i in FileImporter.get_input("/../input/8.txt").split("\n")]
registers = defaultdict(lambda: 0)

maxVal = 0
for i in inp:
    reg, op, val, condReg, condOp, condVal = i[:3] + i[4:]  # Unpack input, ignore 'if'
    if not ops[condOp](registers[condReg], int(condVal)): continue
    registers[reg] = ops[op](registers[reg], int(val))
    if registers[reg] > maxVal: maxVal = registers[reg]
print(maxVal)
