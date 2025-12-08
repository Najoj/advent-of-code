INPUT = 'example.in'
INPUT = 'my.in'

with open(INPUT) as file:
    lines = file.readlines()


# operators and length of digits
operators = []
first = True
length = -1
for c in lines[-1]:
    length += 1
    if c in ['+', '*']:
        if first:
            first = False
            operators.append((c, -1))
        else:
            operators[-1] = (operators[-1][0], length-1)
            operators.append((c, 1))
            length = 0
operators[-1] = (operators[-1][0], length+1)
print(operators)

_sum = 0 # result
numbers = []
n = 0
start_l = 0
for op, l in operators:
    first = True
    for line in lines[:-1]:
        num = line[start_l:start_l+l].replace(' ', '0')
        if first:
            first = False
            numbers.append([num])
        else:
            numbers[n].append(num)
            
    new_number = ['']*l
    for num in numbers[n]:
        for i in range(len(num)):
            new_number[i] += num[i]
        print(new_number)
    
    if op == '*':
        _res = 1
    else:
        _res = 0
    for num in new_number:
        nnum = num.rstrip('0').lstrip('0')
        expression = f'{_res} {op} {nnum}'
        _res = eval(expression)
    _sum += _res
    
    start_l += l+1
    n += 1

if 'example' in INPUT:
    assert 3263827 == _sum, 'Got sum ' + str(_sum)
print(_sum)