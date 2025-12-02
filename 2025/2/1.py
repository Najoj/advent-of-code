import math as maths  # Oi, British

INPUT = 'example.in'
INPUT = 'my.in'

def get_valid(from_, to_):
    for x in range(from_, to_ + 1):
        l = int(len(str(x)) / 2)
        x = str(x)
        if x[:l] == x[l:]:
            yield x



def sum_of_ids(from_, to_):
    sum_ = 0
    for x in get_valid(from_, to_):
        if from_ <= int(x) <= to_:
            sum_ += int(x)
    return sum_

with open(INPUT) as f:
    # All in one line
    ranges = f.readlines()

ranges = ''.join(ranges)
ranges = ranges.split(',')

total_sum = 0
for r_ in ranges:
    from_, to_ = r_.split('-')
    from_, to_ = int(from_), int(to_)
    total_sum += sum_of_ids(from_, to_)
if INPUT == 'example.in':
    assert total_sum == 1227775554, f'Wrong in example. Got {total_sum}'

print(total_sum)