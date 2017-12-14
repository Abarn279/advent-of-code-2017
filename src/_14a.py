from file_importer import FileImporter
from aocutils import knot_hash

inp = FileImporter.get_input("/../input/14.txt")

print(sum(bin(int(knot_hash(inp + '-' + str(i)), 16))[2:].count('1') for i in range(128)))