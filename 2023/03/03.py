import re

input_file = 'my_input.txt'
# input_file = 'test_input.txt'
with open(input_file, 'r') as f:
    data = f.readlines()


def is_digit(c) -> bool:
    return c in '1234567890'


def get_gear(junk):
    all_gears = []
    for symbol in junk:
        if symbol[2] == '*':
            all_gears.append((symbol[0], symbol[1]))
    all_gears = list(set(all_gears))
    return all_gears


def has_symbol(test_):
    evaluation = any(not is_digit(t[2]) and t[2] != '.' and t[2] != '\n' for t in test_)
    return evaluation


line_no = 0
part_no = []
current = ''
test = []
gear_parts = []
gear_positions = []


def limits(n=4):
    char_from_ = char_num - n
    char_to_ = char_from_ + 2 * n
    if char_from_ < 0:
        char_from_ = 0
    if char_to_ > len(line):
        char_to_ = len(line)
    return re.findall(r'\d+', data[line_no + 1][char_from_:char_to_])


gears = {}
for line in data:
    char_num = 0
    for char in line:
        if is_digit(char):
            current += char
            if 0 <= line_no - 1 < len(data) and 0 <= char_num - 1 < len(data[line_no]):
                test.append((line_no - 1, char_num - 1, data[line_no - 1][char_num - 1]))
            if 0 <= line_no - 1 < len(data) and 0 <= char_num < len(data[line_no]):
                test.append((line_no - 1, char_num, data[line_no - 1][char_num]))
            if 0 <= line_no - 1 < len(data) and 0 <= char_num + 1 < len(data[line_no]):
                test.append((line_no - 1, char_num + 1, data[line_no - 1][char_num + 1]))

            if 0 <= line_no < len(data) and 0 <= char_num - 1 < len(data[line_no]):
                test.append((line_no, char_num - 1, data[line_no][char_num - 1]))
            if 0 <= line_no < len(data) and 0 <= char_num + 1 < len(data[line_no]):
                test.append((line_no, char_num + 1, data[line_no][char_num + 1]))

            if 0 <= line_no + 1 < len(data) and 0 <= char_num - 1 < len(data[line_no]):
                test.append((line_no + 1, char_num - 1, data[line_no + 1][char_num - 1]))
            if 0 <= line_no + 1 < len(data) and 0 <= char_num < len(data[line_no]):
                test.append((line_no + 1, char_num, data[line_no + 1][char_num]))
            if 0 <= line_no + 1 < len(data) and 0 <= char_num + 1 < len(data[line_no]):
                test.append((line_no + 1, char_num + 1, data[line_no + 1][char_num + 1]))

        else:
            if current and has_symbol(test):
                part_no.append(int(current))

                found_gears = get_gear(test)
                if len(found_gears) == 1:
                    h = hash(found_gears[0])
                    if h in gears.keys():
                        gears[h].append(int(current))
                    else:
                        gears[h] = [int(current)]
                elif len(found_gears) == 0:
                    pass
                else:
                    assert False
            current = ''
            test = []

        char_num += 1
    line_no += 1

print('Part 1:', sum(part_no))

s = 0
for gear in gears:
    if len(gears[gear]) == 2:
        p = gears[gear][0] * gears[gear][1]
        s += p
print('Part 2:', s)
