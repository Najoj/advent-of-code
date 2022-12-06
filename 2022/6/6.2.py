input_file = 'data.txt'
# input_file = 'testdata2.txt'
with open(input_file, 'r') as f:
    data = f.readlines()

# Only testdata will contain more than one line
done = False
LENGTH = 14
for line in data:
    # Line will contain '\n'
    for i in range(len(line) - LENGTH):
        line_set = set(line[i:i + LENGTH])
        if len(line_set) == LENGTH:
            print(i + LENGTH)
            break
