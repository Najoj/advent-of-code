FACTOR = 1
input_file = 'testdata.txt'
input_file = 'data.txt'
#input_file = 'my_testdata.txt'
with open(input_file) as f:
    data = f.readlines()


class Monkey:
    def __init__(self, name):
        self.name = name
        # Items to pop
        self.items = []
        self.operation = ''
        self.test_divisible = 0
        # Which monkey
        self.if_true = 0
        self.if_false = 0

        self.inspections = 0

    def __str__(self) -> str:
        all_items = ''
        if self.items:
            all_items = ', '.join(self.items)

        s = f'Monkey {self.name}: ' + all_items + f'. Inspections: {self.inspections}'
        return s

    def inspect(self):
        self.inspections += 1

        item_ = self.items[0]
        self.items = self.items[1:]

        evaluate = self.operation
        if 'old' in self.operation:
            evaluate = self.operation.replace('old', str(item_))

        wl = eval(evaluate) % FACTOR

        if 0 == wl % self.test_divisible:
            return wl, self.if_true
        # return int(wl % 3), self.if_false  # 11.1
        return wl, self.if_false

    def __bool__(self):
        return len(self.items) > 0


worry_level = 0
monkeys = []

monkey_line = 'Monkey '
starting_line = 'Starting items: '
operation_line = 'Operation: new = '
test_divisible_line = 'Test: divisible by '
if_true_line = 'If true: throw to monkey'
if_false_line = 'If false: throw to monkey '

i = 0
for line in data:
    line = line.strip()

    if line[:len(monkey_line)] == monkey_line:
        monkeys.append(Monkey(i))

    elif line[:len(starting_line)] == starting_line:
        monkeys[i].items = [str(x) for x in line[len(starting_line):].split(',')]

    elif line[:len(operation_line)] == operation_line:
        monkeys[i].operation = line[len(operation_line):]

    elif line[:len(test_divisible_line)] == test_divisible_line:
        div_by = int(line[len(test_divisible_line):])
        FACTOR *= div_by
        monkeys[i].test_divisible = div_by

    elif line[:len(if_true_line)] == if_true_line:
        monkeys[i].if_true = int(line[len(if_true_line):])

    elif line[:len(if_false_line)] == if_false_line:
        monkeys[i].if_false = int(line[len(if_false_line):])

        print(monkeys[i])
        i += 1

    elif line:
        print('Strange line:', line)

print('Monkeys:', len(monkeys))
# range_ = 20  # 11.1
range_ = 10_000
for it in range(range_):
    for monkey in monkeys:
        # print(monkey.name, end='')
        while monkey:
            item, to_monkey = monkey.inspect()
            monkeys[to_monkey].items.append(str(item))
    """
    print(' ', it)
    print(f'After round {it}:')
    print('\n'.join(str(m) for m in monkeys))
    """

maximum = max(m.inspections for m in monkeys)
second = max(m.inspections for m in monkeys if m.inspections < maximum)

print()
print(maximum * second)
