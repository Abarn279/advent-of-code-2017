from file_importer import FileImporter

inp = FileImporter.get_input("/../input/1.txt")

steps = len(inp) // 2
print(sum([int(inp[i]) for i in range(len(inp)) if inp[i] == inp[(i + steps) % len(inp)]]))