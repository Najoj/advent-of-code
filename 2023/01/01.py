import re
input_file = 'my_input.txt'
# input_file = 'test_input.txt'
with open(input_file, 'r') as f:
    data = f.readlines()

to_sum = []
for line in data:
    digits = re.sub(r'[a-z\n]', '', line)
    a = int(digits[0])
    b = int(digits[-1])
    c = a * 10 + b
    to_sum.append(c)

total_sum = sum(to_sum)

print('Part one:', total_sum)

input_file = 'my_input.txt'
#input_file = 'test_input_2.txt'
with open(input_file, 'r') as f:
    data = f.readlines()

table = {'one': 1, '1': 1,
         'two': 2, '2': 2,
         'three': 3, '3': 3,
         'four': 4, '4': 4,
         'five': 5, '5': 5,
         'six': 6, '6': 6,
         'seven': 7, '7': 7,
         'eight': 8, '8': 8,
         'nine': 9, '9': 9}
re_find = re.compile(r'one|two|three|four|five|six|seven|eight|nine|[1-9]')
re_find_rev = re.compile(r'enin|thgie|neves|xis|evif|ruof|eerht|owt|eno|[1-9]')
to_sum = []
for line in data:
    line_rev = line[::-1]

    digits = re.findall(re_find, line)
    digits_rev = re.findall(re_find_rev, line_rev)

    a = digits[0]
    b = digits_rev[0]
    b = b[::-1]

    a = int(table[a])
    b = int(table[b])

    c = 10*a + b
    to_sum.append(c)
total_sum = sum(to_sum)
print('Part two:', total_sum)
