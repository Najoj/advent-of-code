input_file = 'testdata.txt'
input_file = 'data.txt'
# input_file = 'my_testdata.txt'

RIGHT_ORDER = -1
CONTINUE = 0
WRONG_ORDER = 1


def compare(left, right):
    if isinstance(left, int) and isinstance(right, list):
        left = [left]
    if isinstance(left, list) and isinstance(right, int):
        right = [right]

    if isinstance(left, list) and isinstance(right, list):
        for left_element, right_element in zip(left, right):
            in_right_order = compare(left_element, right_element)
            if in_right_order != CONTINUE:
                return in_right_order

        if len(left) == len(right):
            return CONTINUE
        elif len(left) < len(right):
            return RIGHT_ORDER
        else:
            return WRONG_ORDER

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return RIGHT_ORDER
        elif left > right:
            return WRONG_ORDER
        return CONTINUE


with open(input_file) as f:
    data = f.readlines()

count = 0
index = 0
for x in range(0, len(data), 3):
    index += 1
    array1 = eval(data[x + 0])
    array2 = eval(data[x + 1])

    # part 1
    if compare(array1, array2) != WRONG_ORDER:
        # print(index)
        count += index

print('Answer:', count)
