from file_importer import FileImporter

inp = [j for j in [i.split(' -> ') for i in FileImporter.get_input("/../input/7.txt").split("\n")] if len(j) > 1]

left, right = set(), set()
for i in inp:
    left.add(i[0].split()[0].strip())
    for j in i[1].split(', '):
        right.add(j.strip())

print(list((left - right))[0])