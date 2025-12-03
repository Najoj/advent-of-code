# INPUT = 'example.in'
INPUT = 'my.in'

with open(INPUT) as f:
    banks = f.readlines()

def joltage(bank_: str) -> int:
    while len(bank_) > 12:
        max_bank = 0
        for i in range(len(bank_)):
            new_bank = int(bank_[:i] + bank_[i+1:])
            if new_bank > max_bank:
                max_bank = new_bank
        bank_ = str(max_bank)

    assert len(bank_) == 12
    jolt = int(bank_)
    print(f'{bank_}: {jolt}')
    return jolt

total_joltage = 0
for bank in banks:
    bank = bank.strip()
    total_joltage += joltage(bank)

if 'example.in' in INPUT:
    assert total_joltage == 3121910778619

print(f'Total joltage: {total_joltage}')