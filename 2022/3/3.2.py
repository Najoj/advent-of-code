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


first = second = third = None

for line in data:
    if first is None:
        first = line.strip()
    elif second is None:
        second = line.strip()
    elif third is None:
        third = line.strip()

        common = None
        for a in first:
            if a in second and a in third:
                common = a

        priority = get_priority(common)
        priorities += priority

        first = second = third = None

print(priorities)
