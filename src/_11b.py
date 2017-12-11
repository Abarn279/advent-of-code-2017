from file_importer import FileImporter
from collections import defaultdict

inp = FileImporter.get_input("/../input/11.txt").split(',')
dic = defaultdict(lambda: 0)

max = 0
for i in inp:
    dic[i] += 1
    xabs = abs((dic["ne"] + dic["se"]) - (dic["nw"] + dic["sw"]))
    yabs = abs((dic["n"] + dic["nw"]) - (dic["s"] + dic["se"]))
    zabs = abs((dic["s"] + dic["sw"]) - (dic["n"] + dic["ne"]))
    dist = int((xabs + zabs + yabs) / 2)
    if dist > max:
        max = dist
print(max)