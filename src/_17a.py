from file_importer import FileImporter

steps = int(FileImporter.get_input("/../input/17.txt"))
currentPos = 0
buffer = [0]
newVal = 1

for i in range(2017):
    currentPos = ((currentPos + steps) % len(buffer)) + 1
    buffer.insert(currentPos, newVal)
    newVal += 1

print(buffer[currentPos + 1])