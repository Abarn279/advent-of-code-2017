from file_importer import FileImporter

inp = FileImporter.get_input("/../input/9.txt")
# inp = "<{!>}>"
i = score = scoreToAdd = 0
garbage = False
garbageChars = 0
while i < len(inp):
    if inp[i] == '!':
        i += 2
        continue

    if inp[i] == '<' and not garbage:
        garbage = True
        i += 1; continue
    elif inp[i] == '>' and garbage:
        garbage = False
        i += 1; continue
        
    if garbage:
        i += 1; garbageChars += 1; continue
    
    elif inp[i] == '{':
        scoreToAdd += 1
    elif inp[i] == '}':
        score += scoreToAdd
        scoreToAdd -= 1

    i += 1

print(garbageChars)
