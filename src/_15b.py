from file_importer import FileImporter

class Gen:
    def __init__(self, prevVal: int, factor, divis, mod):
        self.prevVal = prevVal
        self.factor = factor
        self.divis = divis
        self.mod = mod
    def next(self): 
        self.prevVal = (self.prevVal * self.factor) % self.divis
        if not self.prevVal % self.mod == 0: return self.next()
        return self.prevVal

inp = FileImporter.get_input("/../input/15.txt").split("\n")
FACTOR_A, FACTOR_B, DIVISOR = 16807, 48271, 2147483647

gen_a = Gen(int(inp[0].split(" ")[-1]), FACTOR_A, DIVISOR, 4)
gen_b = Gen(int(inp[1].split(" ")[-1]), FACTOR_B, DIVISOR, 8)

print(sum(gen_a.next() & 0xffff == gen_b.next() & 0xffff for i in range(5000000)))