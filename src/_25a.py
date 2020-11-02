from file_importer import FileImporter
from collections import defaultdict

class Rule:
    def __init__(self, new_val, new_dir, new_state):
        self.new_val = new_val
        self.new_dir = new_dir
        self.new_state = new_state

class State:
    def __init__(self, tape: defaultdict, rule1: Rule, rule2: Rule):
        self.tape = tape
        self.rule1 = rule1
        self.rule2 = rule2
    def act(self):
        global state
        global cursor

        # 0 is always rule 1 and 1 is always rule 2
        rule = self.rule1 if tape[cursor] == 0 else self.rule2

        # step 1 - write new val
        tape[cursor] = rule.new_val
        
        # step 2 - move cursor
        cursor += rule.new_dir

        # step 3 - update state
        state = rule.new_state


inp = FileImporter.get_input("/../input/25.txt").split('\n')
tape = defaultdict(lambda: 0)
state = 'A'
cursor = 0

states = {
    'A': State(tape, Rule(1, 1, 'B'), Rule(0, -1, 'F')),
    'B': State(tape, Rule(0, 1, 'C'), Rule(0, 1, 'D')),
    'C': State(tape, Rule(1, -1, 'D'), Rule(1, 1, 'E')),
    'D': State(tape, Rule(0, -1, 'E'), Rule(0, -1, 'D')),
    'E': State(tape, Rule(0, 1, 'A'), Rule(1, 1, 'C')),
    'F': State(tape, Rule(1, -1, 'A'), Rule(1, 1, 'A'))
}

for i in range(12794428):
    c_state = states[state]
    c_state.act()

print(sum(1 for i in tape.values() if i == 1))