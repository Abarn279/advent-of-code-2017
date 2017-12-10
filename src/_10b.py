from file_importer import FileImporter

def reverse_length(_list, currentPos, length): 
    reverse = list(reversed([_list[i % len(_list)] for i in range(currentPos, currentPos + length)]))
    for i in reverse: 
        _list[currentPos % len(_list)] = i
        currentPos += 1
    return _list

lengths = list(map(int, FileImporter.get_input("/../input/10.txt").split(',')))
nums = list(range(256))
currentPos = skipSize = 0

for length in lengths:
    nums = reverse_length(nums, currentPos, length)
    currentPos += length + skipSize; currentPos %= 256
    skipSize += 1

print(nums[0] * nums[1])