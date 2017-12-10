from file_importer import FileImporter
from operator import xor
from functools import reduce

def reverse_length(_list, currentPos, length): 
    reverse = list(reversed([_list[i % len(_list)] for i in range(currentPos, currentPos + length)]))
    for i in reverse: 
        _list[currentPos % len(_list)] = i
        currentPos += 1
    return _list

lengths = [ord(i) for i in FileImporter.get_input("/../input/10.txt")] + [17, 31, 73, 47, 23] # Get ascii for each char, add 
nums = list(range(256))                                                                       # the problem-defined sequence
currentPos = skipSize = 0

# Run 64 rounds
for i in range(64):
    for length in lengths:
        nums = reverse_length(nums, currentPos, length)
        currentPos += length + skipSize; currentPos %= 256
        skipSize += 1

# Calculate dense hash - 16 blocks
denseHash = []
for i in range(16):
    hashVal = reduce(xor, [i for i in nums[i * 16:i * 16 + 16]])
    denseHash.append(hashVal)

# Function to add leading 0 if necessary
ensurelen = lambda x: '0' + x if len(x) == 1 else x

# Get output hash
print("".join(ensurelen(hex(i)[2:]) for i in denseHash))
