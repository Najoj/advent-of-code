import copy
import re

input_file = 'my_input.txt'
#input_file = 'test_input2.txt'
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

    def walk(self, left_right):
        assert left_right in DIRECTIONS
        self.current_node = self.nodes[self.current_node][left_right]
        return self.current_node == 'ZZZ'

    def __repr__(self):
        return self.current_node


walk = data[0].strip()
map = Map()
for node in data[2:]:
    n, d = node.split('=')
    d = tuple(x.strip() for x in re.findall(r'(\w+)', d))
    map.insert_node(n, d)

steps_until_zzz = 0
reached_zzz = False
walk = list(reversed(walk))
new_walk = copy.copy(walk)
while not reached_zzz:
    w = new_walk.pop()
    if w == 'L':
        reached_zzz = map.walk(LEFT)
    elif w == 'R':
        reached_zzz = map.walk(RIGHT)
    else:
        assert False

    if not new_walk:
        new_walk += walk

    steps_until_zzz += 1

print('Part 1:', steps_until_zzz)


walk = data[0].strip()
queue = []
map = Map()
for node in data[2:]:
    n, d = node.split('=')
    d = tuple(x.strip() for x in re.findall(r'(\w+)', d))
    map.insert_node(n, d)