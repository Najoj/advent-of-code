INPUT = 'example.in'
INPUT = 'my.in'

with open(INPUT) as f:
    banks = f.readlines()


def joltage(bank_: str) -> int:
    for d in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
        index_t = bank_.find(str(d), 0, len(bank_) - 1)
        if index_t > -1:
            jolt = 10*d
            break
    for d in [9,8,7,6,5,4,3,2,1]:
        if -1 < bank_.find(str(d), index_t+1, len(bank_)):
            jolt += d
            break

    print(f'{bank_}: {jolt}')
    return jolt



total_joltage = 0
for bank in banks:
    bank = bank.strip()
    total_joltage += joltage(bank)

if 'example.in' in INPUT:
    assert total_joltage == 357

print(f'Total joltage: {total_joltage}')