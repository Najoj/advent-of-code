input_file = 'data.txt'
# input_file = 'testdata.txt'
with open(input_file, 'r') as f:
    data = f.readlines()

all_sums = []

calorie_sum = 0
n = 0
save = n
for line in data:
    # Remove newline
    line = line.strip()
    if line:
        calorie_sum += int(line)
    else:
        all_sums.append(calorie_sum)
        calorie_sum = 0

all_sums.append(calorie_sum)

print('Part one:', max(all_sums))
print('Part two:', sum(sorted(all_sums, reverse=True)[0:3]))
