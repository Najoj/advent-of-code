INPUT = 'example.in'
INPUT = 'my.in'

with open(INPUT) as f:
    rolls_matrix = f.readlines()

n_lines = len(rolls_matrix)
n_columns = len(rolls_matrix[0].strip())

def check(l, c):
    if rolls_matrix[l][c] != '@':
        return 0
    n = 0
    for x, y in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1), (1,-1),(1,0),(1,1)]:
        if x == 0 and y == 0:
            continue
        if 0 <= l + x < n_lines and 0 <= c + y < n_columns:
            n += 1 if rolls_matrix[l + x][c + y] == '@' else 0

    if n < 4:
        return 1
    return 0



num = 0
for l in range(n_lines):
    for c in range(n_columns):
        num += check(l, c)

if 'example' in INPUT:
    assert num == 13

print('Rolls:', num)