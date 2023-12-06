import re

input_file = 'my_input.txt'
# input_file = 'test_input.txt'
with open(input_file, 'r') as f:
    data = f.readlines()

seeds = re.findall(r'(\d+)', data[0])
seeds = [int(s) for s in seeds]
assert not data[1].strip()

TO = 'to'
RANGES = 'ranges'

maps = {}
name = None
category = None
for line in data[2:]:
    line = line.strip()
    done = False
    if line:
        if name is None:
            name = re.findall(r'([^-]+)-to-([^ ]+) map:', line)
            name = name[0]
        category = re.findall(r'(\d+)', line)

        if name and not category:
            to = name[1]
            name = name[0]

            maps[name] = {TO: to, RANGES: []}
        elif name and category:
            # destination range start, the source range start, and the range length
            maps[name][RANGES].append((int(category[0]), int(category[1]), int(category[2])))
        else:
            pass
    else:
        name, category = None, None

seed_mapping = {}


def get_location(seed_number, seed_='seed') -> int:
    if seed_ == 'location':
        return seed_number
    if seed_ not in seed_mapping.keys():
        seed_mapping[seed_] = {}
    if seed_number in seed_mapping[seed_].keys():
        return seed_mapping[seed_][seed_number]

    mmap = maps[seed_]
    soil_number = None
    for rrange in mmap[RANGES]:
        dest = rrange[0]
        start = rrange[1]
        length = rrange[2]
        if start <= seed_number < start + length:
            soil_number = seed_number - start + dest
            break
    if soil_number is None:
        value = get_location(seed_number, mmap[TO])
    else:
        value = get_location(soil_number, mmap[TO])

    seed_mapping[seed_][seed_number] = value
    return value



seeds_set = []
from_ = None  # for part ii
smallest_location = None
for s in seeds:
    location = get_location(s)
    if smallest_location is None or location < smallest_location:
        smallest_location = location
    if from_ is None:
        from_ = s
    else:
        to_ = from_ + s
        seeds_set += [(from_, from_ + s)]
        from_ = None

print('Part 1:', smallest_location)

# seeds_set = optimize(seeds_set)

smallest_location = None
for ss in seeds_set:
    for s in range(ss[0], ss[1]):
        location = get_location(s)
        if smallest_location is None or location < smallest_location:
            smallest_location = location
print('Part 2:', smallest_location)
