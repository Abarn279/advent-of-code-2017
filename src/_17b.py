from file_importer import FileImporter

steps = int(FileImporter.get_input("/../input/17.txt"))
currentPos = 0
secondVal = -1
bufLen = 1
newVal = 1

for i in range(50000000):
    currentPos = ((currentPos + steps) % bufLen) + 1
    if currentPos == 1:
        secondVal = newVal
    bufLen += 1
    newVal += 1

print(secondVal)