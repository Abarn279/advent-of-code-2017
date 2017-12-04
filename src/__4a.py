from file_importer import FileImporter

inp = [i.split(" ") for i in FileImporter.get_input("/../input/4.txt").split("\n")]

count = 0
for line in inp:
    lset = set()
    allUnique = True
    for word in line:
        if word in lset:
            allUnique = False
            break
        lset.add(word)
    if allUnique:
        count += 1
print(count)    

