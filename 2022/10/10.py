input_file = 'testdata.txt'
input_file = 'data.txt'
# input_file = 'my_testdata.txt'
with open(input_file) as f:
    data = f.readlines()

register_X = 1
queue_V = [register_X]
for line in data:
    line = line.strip()

    queue_V.append(register_X)
    # skip noop
    if line == 'noop':
        pass
    else:
        instruction, number = line.split(' ')
        number = int(number)
        queue_V.append(register_X)
        register_X += number

print(sum([i * queue_V[i] for i in range(20, 221, 40)]))

for line in range(1, 241, 40):
    row = ''
    for clock in range(line, line + 40):
        if clock - line in [queue_V[clock] - 1, queue_V[clock], queue_V[clock] + 1]:
            row += '#'
        else:
            row += '.'
    print(row)
