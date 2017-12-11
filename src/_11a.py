from file_importer import FileImporter
from collections import defaultdict
from math import fabs

inp = FileImporter.get_input("/../input/11.txt").split(',')
dic = defaultdict(lambda: 0)

for i in inp:
    dic[i] += 1

xabs = fabs((dic["ne"] + dic["se"]) - (dic["nw"] + dic["sw"]))
yabs = fabs((dic["n"] + dic["nw"]) - (dic["s"] + dic["se"]))
zabs = fabs((dic["s"] + dic["sw"]) - (dic["n"] + dic["ne"]))

print(int((xabs + zabs + yabs) / 2))