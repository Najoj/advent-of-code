import math


def initialise_see_trees(forrest_):
    row_index = 0
    for trees_ in forrest_:
        seen_row = []
        col_index = 0
        for _ in trees_:
            if (row_index == 0 or
                    col_index == 0 or
                    row_index == max_row - 1 or
                    col_index == max_col - 1):
                seen_row.append(True)
            else:
                seen_row.append(False)
            col_index += 1
        trees_seen.append(seen_row)
        row_index += 1


def see_trees(forrest_):
    row_index = 0
    for trees_ in forrest_:
        col_index = 0
        first_tree = forrest_[row_index][0]
        max_tree = first_tree
        for tree_ in trees_:
            if tree_ > max_tree:
                trees_seen[row_index][col_index] = True
                max_tree = tree_
            col_index += 1
        row_index += 1


def turn_90(matrix):
    """
    >>> turn_90([[]])
    []
    >>> turn_90([[1, 2], [3, 4]])
    [[2, 4], [1, 3]]
    >>> turn_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]


def print_tree():
    global row
    for row in trees_seen:
        print(row)


def _view(ri, ci):
    consider = forrest[ri][ci]
    count = [1, 1, 1, 1]
    # going north
    for r in range(max_row):
        r = ri - r - 1
        if r < 0:
            count[0] -= 1
            break
        if forrest[r][ci] < consider:
            count[0] += 1
        else:
            break
    # going south
    for r in range(max_row):
        r = ri + r + 1
        if r > max_row - 1:
            count[1] -= 1
            break
        if forrest[r][ci] < consider:
            count[1] += 1
        else:
            break
    # going west
    for c in range(max_col):
        c = ci - c - 1
        if c < 0:
            count[2] -= 1
            break
        if forrest[ri][c] < consider:
            count[2] += 1
        else:
            break
    # going east
    for c in range(max_col):
        c = ci + c + 1
        if c > max_col - 1:
            count[3] -= 1
            break
        if forrest[ri][c] < consider:
            count[3] += 1
        else:
            break

    mul_ = int(math.prod(count))
    return mul_


if __name__ == '__main__':
    test_file = 'testdata.txt'
    input_file = test_file
    input_file = 'data.txt'

    with open(input_file) as f:
        data = f.readlines()

    forrest = []
    trees_seen = []
    max_row = len(data[0]) - 1
    max_col = len(data)

    for trees in data:
        trees = [int(x) for x in trees.strip()]
        seen = [False for x in trees]
        forrest.append(trees)

    for row in trees_seen:
        print(row)

    initialise_see_trees(forrest)

    see_trees(forrest)

    trees_seen = turn_90(trees_seen)
    forrest = turn_90(forrest)
    see_trees(forrest)

    trees_seen = turn_90(trees_seen)
    forrest = turn_90(forrest)
    see_trees(forrest)

    trees_seen = turn_90(trees_seen)
    forrest = turn_90(forrest)
    see_trees(forrest)

    # print(transposed_forrest)
    seen = 0
    for row in trees_seen:
        for tree in row:
            # print(str(tree), end='')
            # print('  ' if tree else ' ', end='')
            if tree:
                seen += 1
        # print('')

    assert seen == 21 if input_file == test_file else seen == 1785
    assert seen < 1915
    print(seen)

    # Turn back to original
    forrest = turn_90(forrest)
    scenic_view = 0
    for row_index in range(len(forrest[0]) - 2):
        row_index += 1
        for col_index in range(len(forrest) - 2):
            col_index += 1
            view = _view(row_index, col_index)
            scenic_view = scenic_view if scenic_view > view else view

    assert scenic_view == 8 if input_file == test_file else True
    print(scenic_view)

