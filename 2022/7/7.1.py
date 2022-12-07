import os

input_file = 'data.txt'
test_file = 'testdata1.txt'
# input_file = test_file
with open(input_file, 'r') as f:
    data = f.readlines()

position = []
read_content = False
file_hierarchy = {}
ROOT = '/'


def update_file(name, content):
    tmp = file_hierarchy
    for p_ in position:
        tmp = tmp[p_]
    tmp.update({name: content})


# create file structure
for line in data:
    line = line.strip()

    # command
    if '$' == line[0]:
        _dollar, command = line.split(' ', maxsplit=1)
        if 'cd' == command[0:2]:
            _, argument = command.split(' ', maxsplit=1)
            if '..' == argument:
                position = position[:-1]
            else:
                _position = '/'.join(position)
                _position = os.path.abspath(_position)
                read_content = False
                if position:
                    update_file(argument, {})
                else:
                    ROOT = argument
                    file_hierarchy[argument] = {}
                position.append(argument)
        elif 'ls' == command:
            read_content = True
        else:
            raise Exception(f'Got command {command} in line: {line}')
    elif read_content:
        size, file = line.split(' ', maxsplit=1)
        if 'dir' == size:
            update_file(file, {})
        else:
            size = int(size)
            update_file(file, size)
    else:
        raise Exception(f'Got line: {line}')

directory_sizes = {}


def _get_total_size(hierarchy, path=''):
    include_sums = []
    for key in hierarchy.keys():
        if isinstance(hierarchy[key], dict):
            full_path = os.path.abspath(os.path.join(path, key))
            size_ = _get_total_size(hierarchy[key], full_path)

            include_sums.append(size_)
            if full_path not in directory_sizes.keys():
                # size_ = max(size_, directory_sizes[key])
                directory_sizes.update({full_path: size_})
        else:
            size_ = hierarchy[key]
            include_sums.append(size_)
    return sum(include_sums)


_limit = 100000
size = _get_total_size(file_hierarchy)
total_size = sum([s for s in directory_sizes.values() if s <= _limit])

assert total_size < 50822529
assert total_size < 49774559
assert total_size < 3984500
assert total_size != 3230678
assert total_size != 3369299

assert 95437 == total_size if test_file == input_file else 1306611 == total_size

print(total_size)

total_system_size = 70_000_000
free_needed = 30_000_000
size_to_free = total_system_size - directory_sizes[ROOT]
size_to_free = free_needed - size_to_free

biggest, smallest = total_system_size, 0
biggest_path, smallest_path = 'XXX', 'YYY'

for key in directory_sizes.keys():
    path_size = directory_sizes[key]
    path = key
    if size_to_free <= path_size <= biggest:
        biggest = path_size
        biggest_path = path
    if smallest <= path_size <= size_to_free:
        smallest = path_size
        smallest_path = path

# print(smallest_path, smallest)
print(biggest_path, biggest)
