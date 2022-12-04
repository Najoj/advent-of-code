input_file = 'data.txt'
# input_file = 'testdata.txt'
with open(input_file, 'r') as f:
    data = f.readlines()


pairs = 0

for line in data:
    range_a, range_b = line.strip().split(',', maxsplit=1)

    min_a, max_a = range_a.split('-', maxsplit=1)
    min_a, max_a = int(min_a), int(max_a)
    assert min_a <= max_a

    min_b, max_b = range_b.split('-', maxsplit=1)
    min_b, max_b = int(min_b), int(max_b)
    assert min_b <= max_b

    if min_b <= min_a <= max_b or min_a <= min_b <= max_a:
        pairs += 1

print(pairs)
