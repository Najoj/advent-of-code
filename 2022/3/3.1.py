input_file = 'data.txt'
# input_file = 'testdata.txt'
with open(input_file, 'r') as f:
    data = f.readlines()

priorities = 0


def get_priority(a):
    """
    >>> get_priority('a')
    1
    >>> get_priority('p')
    16
    >>> get_priority('z')
    26
    >>> get_priority('A')
    27
    >>> get_priority('P')
    42
    >>> get_priority('Z')
    52
    """
    if a.islower():
        return ord(a) - ord('a') + 1
    return ord(a) - ord('A') + 27


for line in data:
    line = line.strip()
    length = len(line)
    assert length % 2 == 0
    half_length = int(length/2)

    first = line[:half_length]
    second = line[half_length:]

    common = None
    for a in first:
        if a in second:
            common = a

    priority = get_priority(common)
    priorities += priority

print(priorities)
