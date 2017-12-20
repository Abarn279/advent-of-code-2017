from file_importer import FileImporter
import re
from collections import defaultdict

def get_hash(lis):
    return ",".join(str(i) for i in lis)

def get_colliding_dic(lparticles):
    posDic = defaultdict(lambda: 0)
    for p in lparticles:
        posDic[get_hash(p.pos)] += 1
    return posDic

class Particle:
    def __init__(self, ipos, ivel, iacc, id):
        self.pos = ipos; self.vel = ivel; self.acc = iacc;self.id = id
        self.colliding = True
    def update(self):
        self.colliding = False
        for i in range(3):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]

inp = [i for i in FileImporter.get_input("/../input/20.txt").split('\n')]
particles = [Particle(*[list(map(int, j.split(","))) for j in re.findall("<(.*?)>", inp[i])] + [i]) for i in range(len(inp))] # Lol

for i in range(1000000):
    j = 0
    for p in particles:
        p.update()
    dic = get_colliding_dic(particles)
    while j < len(particles):
        if (dic[get_hash(particles[j].pos)] > 1):
            particles.pop(j)
            continue
        j += 1
    print("particles left: " + str(len(particles))) # Run for a while, receive answer :)