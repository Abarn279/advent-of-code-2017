from file_importer import FileImporter

class Gen:
    def __init__(self, prevVal: int, factor, divis):
        self.prevVal = prevVal
        self.factor = factor
        self.divis = divis
    def next(self): 
        self.prevVal = (self.prevVal * self.factor) % self.divis
        return self.prevVal

inp = FileImporter.get_input("/../input/15.txt").split("\n")
FACTOR_A, FACTOR_B, DIVISOR = 16807, 48271, 2147483647

gen_a = Gen(int(inp[0].split(" ")[-1]), FACTOR_A, DIVISOR)
gen_b = Gen(int(inp[1].split(" ")[-1]), FACTOR_B, DIVISOR)

print(sum(gen_a.next() & 0xffff == gen_b.next() & 0xffff for i in range(40000000)))