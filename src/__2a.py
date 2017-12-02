from file_importer import FileImporter

inp = [list(map(int, i.split("\t"))) for i in FileImporter.get_input("/../input/2.txt").split('\n')]

print(sum(max(i)-min(i) for i in inp))