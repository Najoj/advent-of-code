import textwrap

INPUT = 'example.in'
INPUT = 'my.in'


def split(s, n):
    return textwrap.wrap(s, n)

def get_valid(from_, to_):
    for x in range(from_, to_ + 1):
        x_str = str(x)
        l = int(len(x_str) / 2)
        for n in range(1, l + 2):
            splits = split(str(x), n)
            if len(splits) > 1 and all(splits[0] == y for y in splits[1:]):
                yield x
                break


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
    assert total_sum == 4174379265, f'Wrong in example. Got {total_sum}'

print(total_sum)
