INPUT = 'example.in'
INPUT = 'my.in'

with open(INPUT) as file:
    lines = file.readlines()


data_lines = []
i,j = 0,0
for line in lines:
    data = []
    for n in line.split(' '):
        if n.strip():
            data.append(int(n) if n[0] in '0123456789' else n)
    data_lines.append(data)

total = []
for i in range(len(data_lines) - 1):
    for j in range(len(data_lines[i])):
        operator = data_lines[-1][j]
        num = data_lines[i][j]

        if len(total) <= j:
            if operator == '+':
                total.append(0)
            else:
                total.append(1)

        total[j] = eval(str(total[j]) + operator + str(num))

print(total)
print(sum(total))