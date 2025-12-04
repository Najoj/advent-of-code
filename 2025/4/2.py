import copy

#INPUT = 'example.in'
INPUT = 'my.in'

with open(INPUT) as f:
    rolls_matrix = f.readlines()

n_lines = len(rolls_matrix)
n_columns = len(rolls_matrix[0].strip())

def check(input_matrix):
    output_matrix = []
    updated = 0
    for l in range(0, n_lines):
        output_line = ['x']*n_columns
        for c in range(0, n_columns):
            output_line[c] = input_matrix[l][c]
            count = 0
            if input_matrix[l][c] != '@':
                continue
            n = 0
            for x, y in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1), (1,-1),(1,0),(1,1)]:
                if x == 0 and y == 0:
                    continue
                if 0 <= l + x < n_lines and 0 <= c + y < n_columns:
                    if input_matrix[l + x][c + y] == '@':
                        count += 1
            if count < 4:
                output_line[c] = '.'
                updated += 1
        # endfor l
        output_matrix.append(''.join(output_line))
    # endfor c
    return updated, output_matrix

num = 0
input_matrix = copy.deepcopy(rolls_matrix)
while True:
    m, updated_matrix = check(input_matrix)
    if input_matrix == updated_matrix:
        assert m == 0
        break
    else:
        input_matrix = copy.deepcopy(updated_matrix)
        num += m

if 'example' in INPUT:
    assert num == 43

print('Rolls:', num)