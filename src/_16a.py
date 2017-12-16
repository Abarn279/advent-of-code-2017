from file_importer import FileImporter

def spin(ary, ind): 
    ind = len(ary) - ind
    return ary[ind:] + ary[:ind]

def exchange(ary, pos1, pos2):
    tmp = ary[pos1]
    ary[pos1] = ary[pos2]
    ary[pos2] = tmp
    return ary

def partner(ary, char1, char2):
    pos1, pos2 = ary.index(char1), ary.index(char2)
    return exchange(ary, pos1, pos2)

progs = [chr(i) for i in range(97, 113)]

inp = FileImporter.get_input("/../input/16.txt").split(",")

for i in inp:
    x = i.split("/")
    if len(x) == 1:
        progs = spin(progs, int(x[0][1:]))
    elif x[0][0] == "x":
        progs = exchange(progs, int(x[0][1:]), int(x[1]))
    elif x[0][0] == "p":
        progs = partner(progs, x[0][1], x[1])

print("".join(progs))