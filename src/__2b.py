from file_importer import FileImporter

inp = [list(map(int, i.split("\t"))) for i in FileImporter.get_input("/../input/2.txt").split('\n')]

sum = 0
for row in inp: 
    for num in row:
        divs = list(row)
        divs.remove(num)
        for otherNum in divs:
            if (num % otherNum == 0):
                sum += num // otherNum
print(sum)