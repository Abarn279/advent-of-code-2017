from file_importer import FileImporter

inp = list(map(int, [i for i in FileImporter.get_input("/../input/5.txt").split('\n')]))

ind, steps = 0, 0
while True:
    indToAdd = ind
    try:
        ind += inp[ind]
        if inp[indToAdd] >= 3: inp[indToAdd] -= 1
        else: inp[indToAdd] += 1
        steps += 1
    except:
        break
print(steps)
