INPUT = 'example.in'
INPUT = 'my.in'

with open(INPUT) as file:
    lines = file.readlines()

ranges = []
fresh = 0
for line in lines:
    line = line.strip()
    if not line:
        # empty line
        continue
    elif '-' in line:
        # a range
        f, t = line.split('-')
        ranges.append(range(int(f), int(t) + 1))  # add to t to be inclusive
    else:
        # an ingredient
        line = int(line)
        for range in ranges:
            if line in range:
                fresh += 1
                break
            #end if
        # end for
    # end if
# end for

if 'example.in' in INPUT:
    assert fresh == 3, f'Got {fresh} != 3'
print(fresh)