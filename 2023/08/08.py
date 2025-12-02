import copy
import re
import sys

input_file = 'my_input.txt'
# input_file = 'test_input2.txt'
with open(input_file, 'r') as f:
    data = f.readlines()

LEFT = 0
RIGHT = 1
DIRECTIONS = [LEFT, RIGHT]


class Map:
    def __init__(self, default_node='AAA'):
        self.nodes = {}
        self.current_node = default_node

    def insert_node(self, name: str, left_right):
        name = name.strip()
        assert name not in self.nodes
        self.nodes[name] = left_right

    def walk(self, left_right, part2=False):
        assert left_right in DIRECTIONS
        self.current_node = self.nodes[self.current_node][left_right]
        return self.current_node[-1] == 'Z' if part2 else self.current_node == 'ZZZ'

    def __repr__(self):
        return self.current_node


walk = data[0].strip()
map_ = Map()
for node in data[2:]:
    n, d = node.split('=')
    d = tuple(x.strip() for x in re.findall(r'(\w+)', d))
    map_.insert_node(n, d)

steps_until_zzz = 0
reached_zzz = False
walk = list(reversed(walk))
new_walk = copy.copy(walk)
while not reached_zzz:
    w = new_walk.pop()
    if w == 'L':
        reached_zzz = map_.walk(LEFT)
    elif w == 'R':
        reached_zzz = map_.walk(RIGHT)
    else:
        assert False

    if not new_walk:
        new_walk += walk

    steps_until_zzz += 1

print('Part 1:', steps_until_zzz)

"""
input_file = 'test_input3.txt'
with open(input_file, 'r') as f:
    data = f.readlines()
"""

# Template map
map_ = Map()
for node in data[2:]:
    n, d = node.split('=')
    d = tuple(x.strip() for x in re.findall(r'(\w+)', d))
    map_.insert_node(n, d)

walk = data[0].strip()
starting_nodes = [node for node in map_.nodes if node[-1] == 'A']
queue = []
for i in range(len(starting_nodes)):
    n_map = copy.deepcopy(map_)
    n_map.current_node = starting_nodes[i]
    queue.append(n_map)

reached_zzz = [False] * len(queue)
all_reached = False
walk = list(reversed(walk))
new_walk = copy.copy(walk)
steps_until_zzz = 0
while not all(reached_zzz):
    w = new_walk.pop()

    i = 0

    for m in queue:
        if w == 'L':
            reached_zzz[i] = m.walk(LEFT, True)
        elif w == 'R':
            reached_zzz[i] = m.walk(RIGHT, True)
        else:
            assert False
        i += 1

    steps_until_zzz += 1

    if not new_walk:
        new_walk += walk
        sys.stdout.flush()

print('Part 2:', steps_until_zzz)

