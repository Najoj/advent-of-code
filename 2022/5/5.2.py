import re


class Stack:
    def __init__(self):
        self._stack = []
        self._height = 0

    def push(self, item, bottom=False):
        if item and item.strip():
            self._height += 1
            if bottom:
                self._stack = [item] + self._stack
            else:
                self._stack = self._stack + [item]

    def pop(self):
        if not self._stack:
            return None
        self._height -= 1
        item = self._stack[-1]
        self._stack = self._stack[:-1]
        return item

    def reverse(self):
        reversed(self._stack)

    def __len__(self):
        return self._height

    def __str__(self):
        string = ' '.join(string for string in self._stack[key])
        return string


NOTHING = '    '

input_file, no_stacks = 'data.txt', 9
# input_file, no_stacks = 'testdata.txt', 3
with open(input_file, 'r') as f:
    data = f.readlines()

stacks = {}
for stack_number in range(no_stacks):
    stacks[stack_number] = Stack()

read_moves = False  # read stacks.
match_stacks = True
height = 0
for line in data:
    if match_stacks and line and '1' not in line:
        stack_number = 0
        for n in range(0, no_stacks * 4, 4):
            box = line[n:n + 3]
            stacks[stack_number].push(box, True)
            stack_number += 1
            stack_number %= no_stacks
    elif match_stacks and '1' in line:
        match_stacks = False

    elif line.strip():
        re_move = re.compile(r'move (\d+) from (\d+) to (\d+)')
        _, no, from_, to, _ = re.split(re_move, line)
        no, from_, to = int(no), int(from_) - 1, int(to) - 1

        save = []
        for _ in range(no):
            item = stacks[from_].pop()
            save.append(item)
        for item in reversed(save):
            stacks[to].push(item)

for key in stacks.keys():
    print(stacks[key].pop()[1], end='')
print()
