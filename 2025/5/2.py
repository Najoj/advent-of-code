import copy

INPUT = 'example.in'
INPUT = 'my.in'
#INPUT = 'test.in'

with open(INPUT) as file:
    lines = file.readlines()

ranges = []
fresh = 0
min_max = [0, 0]
mm_set = False
for line in lines:
    line = line.strip()
    if not line:
        # empty line
        continue
    elif '-' in line:
        # a range
        f, t = line.split('-')
        f = int(f)
        t = int(t)
        ranges.append((f, t+1))

    else:
        # an ingredient, dnc
        continue
    # end if
# end for


def check_range(outer, inner):
    updated = True
    new_ranges = inner
    if outer == inner or outer[1] < inner[0] or inner[1] < outer[0]:
        # no overlap
        updated = False
    elif inner[0] <= outer[0] <= outer[1] <= inner[1]:
        # inner [        ]
        # outer   [   ]
        new_ranges = (inner[0], inner[1])

    elif outer[0] <= inner[0] <= outer[1] <= inner[1]:
        # inner     [   ]
        # outer   [   ]
        new_ranges = (outer[0], inner[1])

    elif inner[0] <= outer[0] <= inner[1] <= outer[1]:
        # inner [    ]
        # outer   [     ]
        new_ranges = (inner[0], outer[1])

    elif outer[0] <= inner[0] <= inner[1] <= outer[1]:
        # inner   [   ]
        # outer [        ]
        new_ranges = (outer[0], outer[1])

    else:
        print(inner)
        print(outer)

    return new_ranges, updated

def update_ranges(ranges):
    """
    >>> update_ranges([(1,2)])
    [(1,2)]
    """
    new_ranges = copy.copy(ranges)
    for outer in ranges:
        for inner in ranges:
            new_range, updated = check_range(outer, inner)
            if updated:
                new_ranges.remove(outer)
                new_ranges.remove(inner)
                new_ranges.append(new_range)
                return new_ranges
    return new_ranges

while True:
    new_ranges = update_ranges(ranges)
    if ranges == new_ranges:
        break
    ranges = new_ranges
    print(len(ranges))

no_fresh = 0
for f, t in ranges:
    no_fresh += t-f

if 'example.in' in INPUT:
    assert no_fresh == 14, f'Got {no_fresh} != 14'
print(no_fresh)