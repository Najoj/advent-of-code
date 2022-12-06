#input_file = 'data.txt'
input_file = 'testdata1.txt'
with open(input_file, 'r') as f:
    data = f.readlines()

# Only testdata will contain more than one line
done = False
for line in data:
    # Line will contain '\n'
    for i in range(len(line)-4):
        line_set = set(line[i:i+4])
        if len(line_set) == 4:
            print(i+4)
            break
