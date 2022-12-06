import re
from Stack import Stack

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
re_move = re.compile(r'move (\d+) from (\d+) to (\d+)')

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
        _, no, from_, to, _ = re.split(re_move, line)
        no, from_, to = int(no), int(from_) - 1, int(to) - 1

        for _ in range(no):
            stacks[to].push(stacks[from_].pop())

for key in stacks.keys():
    print(stacks[key].pop()[1], end='')
print()
