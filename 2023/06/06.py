import math
import re

input_file = 'my_input.txt'
#input_file = 'test_input.txt'
with open(input_file, 'r') as f:
    data = f.readlines()

times = [int(x) for x in re.findall(r'\d+', data[0])]
distances = [int(x) for x in re.findall(r'\d+', data[1])]
assert len(times) == len(distances)


def product(factors: list) -> int:
    prod = 1
    for x in factors:
        prod *= x
    return prod


mul = []
for time, distance in zip(times, distances):
    records = []
    for hold in range(1, time - 1):
        if distance < hold * (time - hold):
            records.append(hold)
    mul.append(len(records))

print('Part 1:', product(mul))

time = ''.join([str(x) for x in re.findall(r'\d+', data[0])])
time = int(time)
distance = ''.join([str(x) for x in re.findall(r'\d+', data[1])])
distance = int(distance)

# 0 = hold * hold - hold * time + distance
start_hold_max = time / 2 + math.sqrt(math.pow(time / 2, 2) - distance)
start_hold_min = time / 2 - math.sqrt(math.pow(time / 2, 2) - distance)
start_hold_max = int(start_hold_max) if start_hold_max > start_hold_min else int(start_hold_min)
start_hold_min = int(start_hold_max) if start_hold_max < start_hold_min else int(start_hold_min)
diff = start_hold_max - start_hold_min
print('Part 2:', diff)
