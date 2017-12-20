from file_importer import FileImporter
import re

class Particle:
    def __init__(self, ipos, ivel, iacc, id):
        self.pos = ipos; self.vel = ivel; self.acc = iacc;self.id = id
    def update(self):
        for i in range(3):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]
    def mandis(self):
        return sum(abs(self.pos[i]) for i in range(3))

inp = [i for i in FileImporter.get_input("/../input/20.txt").split('\n')]
particles = [Particle(*[list(map(int, j.split(","))) for j in re.findall("<(.*?)>", inp[i])] + [i]) for i in range(len(inp))] # Lol

for i in range(1000000):
    minval = 100000000000; minId = -1
    for pi in range(len(particles)):
        particles[pi].update()
        mandis = particles[pi].mandis()
        if abs(mandis) < minval:
            minval = abs(mandis); minId = pi
    print("max ID: " + str(minId)) # Run this for a while until you get the answer... :)