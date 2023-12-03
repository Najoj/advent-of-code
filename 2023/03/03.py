input_file = 'my_input.txt'
# input_file = 'test_input.txt'
with open(input_file, 'r') as f:
    data = f.readlines()


def is_digit(c) -> bool:
    return c in '1234567890'


def has_symbol(test_):
    evaluation = any(not is_digit(t) and t != '.' and t != '\n' for t in test_)
    return evaluation


line_no = 0
part_no = []
current = ''
test = []
for line in data:
    char_no = 0
    for char in line:
        if is_digit(char):
            current += char

            if 0 <= line_no - 1 < len(data) and 0 <= char_no - 1 < len(data[line_no]):
                test.append(data[line_no - 1][char_no - 1])
            if 0 <= line_no - 1 < len(data) and 0 <= char_no < len(data[line_no]):
                test.append(data[line_no - 1][char_no])
            if 0 <= line_no - 1 < len(data) and 0 <= char_no + 1 < len(data[line_no]):
                test.append(data[line_no - 1][char_no + 1])

            if 0 <= line_no < len(data) and 0 <= char_no - 1 < len(data[line_no]):
                test.append(data[line_no][char_no - 1])
            if 0 <= line_no < len(data) and 0 <= char_no + 1 < len(data[line_no]):
                test.append(data[line_no][char_no + 1])

            if 0 <= line_no + 1 < len(data) and 0 <= char_no - 1 < len(data[line_no]):
                test.append(data[line_no + 1][char_no - 1])
            if 0 <= line_no + 1 < len(data) and 0 <= char_no < len(data[line_no]):
                test.append(data[line_no + 1][char_no])
            if 0 <= line_no + 1 < len(data) and 0 <= char_no + 1 < len(data[line_no]):
                test.append(data[line_no + 1][char_no + 1])

        else:
            if current and has_symbol(test):
                part_no.append(int(current))
            current = ''
            test = []

        char_no += 1
    line_no += 1

print('\n'.join(str(p) for p in part_no))
print('Part 1:', sum(part_no))
