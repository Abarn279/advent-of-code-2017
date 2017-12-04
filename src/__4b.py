from file_importer import FileImporter

inp = [i.split(" ") for i in FileImporter.get_input("/../input/4.txt").split("\n")]

print(len([l for l in inp if len(set(["".join(sorted(i)) for i in l])) == len(["".join(sorted(i)) for i in l])]))