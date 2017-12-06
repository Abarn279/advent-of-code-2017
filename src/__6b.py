from file_importer import FileImporter

inp = list(map(int, FileImporter.get_input("/../input/6.txt").split()))

def max_bank_ind(banks):
    max = 0
    for i in range(len(banks)):
        if banks[i] > banks[max]:
            max = i
    return max

def realloc(banks, bankInd):
    blocks, banks[bankInd] = banks[bankInd], 0
    while blocks > 0:
        bankInd += 1
        banks[bankInd % len(banks)] += 1
        blocks -= 1

states, count = [], 0
while True:
    if inp in states:
        break

    states.append(inp[:])
    maxInd = max_bank_ind(inp)
    realloc(inp, maxInd)
    count += 1

print(count - states.index(inp))