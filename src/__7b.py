from file_importer import FileImporter

class Node:
    def __init__(self, name, weight):
        self.name = str(name); self.weight = int(weight); self.children = []

def get_node(nodeList, nameToAdd):
    line = [i for i in nodeList if i.startswith(nameToAdd)][0]
    childNames = []
    splitLine = line.split(" -> ")

    nodeInfo = splitLine[0]
    if len(splitLine) > 1:
        childNames = splitLine[1].split(", ")

    splitInfo = nodeInfo.split(" ")
    name, weight = splitInfo[0], splitInfo[1][1:-1]

    node = Node(name, weight)
    
    for childName in childNames:
        node.children.append(get_node(nodeList, childName))

    return node

def get_tree_sum(node):
    sum = node.weight
    for child in node.children:
        sum += get_tree_sum(child)
    return sum

def find_unbalanced_weight_dif(node):
    if len(node.children) == 0:                                     # Skip leaves
        return

    for child in node.children:                                     # Post-order traversal
        weight = find_unbalanced_weight_dif(child)
        if weight != None:
            return weight

    sums = []                                                       # Get sums of all children
    for child in node.children:
        sums.append(get_tree_sum(child))
    
    if len(set(sums)) == 1:                                         # If all sums are the same, its balanced
        return None
    
    counts = { i:sums.count(i) for i in sums }                      # Dictionary of child summation value to how many times it shows up
    dif = max(counts, key=counts.get) - min(counts, key=counts.get) # Difference between other vals and the uneven val
    childInd = sums.index(min(counts, key=counts.get))              # Index back to the node in question

    return node.children[childInd].weight + dif                     # Get the node weight and add its needed difference

root = "aapssr" # Output from 7A
inp = FileImporter.get_input("/../input/7.txt").split("\n")
node = get_node(inp, root) # Build tree

print(find_unbalanced_weight_dif(node))