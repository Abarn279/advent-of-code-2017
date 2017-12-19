from file_importer import FileImporter

def add_tup(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def negate_touple(t1):
    return (-t1[0], -t1[1])

# Row, Column Deltas
UP, DOWN, RIGHT, LEFT = (-1, 0), (1, 0), (0, 1), (0, -1)

inp = [i for i in FileImporter.get_input("/../input/19.txt").split('\n')]

current = (0, inp[0].index('|'))
direction = DOWN
letters = []

while True:
    nxt = add_tup(current, direction)
    char = inp[nxt[0]][nxt[1]]
    if char == '+':
        for i in (set([UP, DOWN, RIGHT, LEFT]) - set([direction, negate_touple(direction)])):
            turned_coord = add_tup(nxt, i)
            if inp[turned_coord[0]][turned_coord[1]] in '|-':
                direction = i
                break
    elif char.isalpha():
        letters.append(char)
    elif char == " ":
        break

    current = nxt

print("".join(letters))    