from file_importer import FileImporter
from collections import defaultdict
from queue import Queue
import re

inp = [i.split() for i in FileImporter.get_input("/../input/18.txt").split('\n')]

class Prog:
    def __init__(self, inp, inpId):
        self.q = Queue()
        self.registers = defaultdict(lambda: 0)
        self.registers['p'] = inpId
        self.instIndex = 0
        self.inp = inp
        self.waiting = False
        self.terminated = False
        self.sentValues = 0

    def get_value(self, arg2): 
        return int(arg2) if re.match("[+-]?\d", arg2) is not None else int(self.registers[arg2])

    def set_partner(self, other):
        self.partner = other

    def execute(self):
        if (self.instIndex >= len(self.inp)):
            self.terminated = True
            return

        curr = self.inp[self.instIndex]
        if curr[0] == 'snd':
            self.partner.q.put(self.get_value(curr[1]))
            self.sentValues += 1

        elif curr[0] == 'set':
            self.registers[curr[1]] = self.get_value(curr[2])
        elif curr[0] == 'add':
            self.registers[curr[1]] += self.get_value(curr[2])
        elif curr[0] == 'mul':
            self.registers[curr[1]] *= self.get_value(curr[2])
        elif curr[0] == 'mod':
            self.registers[curr[1]] %= self.get_value(curr[2])
        elif curr[0] == 'rcv':
            if self.q.empty():
                self.waiting = True

                if self.waiting and self.partner.waiting:
                    self.terminated = self.partner.terminated = True
                
                return

            else:
                self.waiting = False
                self.registers[curr[1]] = self.q.get()

        elif curr[0] == 'jgz':
            if self.get_value(curr[1]) > 0:
                self.instIndex += self.get_value(curr[2])
                return

        self.instIndex += 1


prog0 = Prog(inp, 0)
prog1 = Prog(inp, 1)
prog0.set_partner(prog1)
prog1.set_partner(prog0)

while not (prog0.terminated and prog1.terminated):
    if not prog0.terminated:
        prog0.execute()
    if not prog1.terminated:
        prog1.execute()

print(prog1.sentValues)
