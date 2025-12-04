with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

elf_cals = []
curr_cals = 0

for d in data:
    if not d:
        elf_cals.append(curr_cals)
        curr_cals = 0
    else:
        curr_cals += int(d)

elf_cals = sorted(elf_cals, reverse=True)
print(elf_cals[0])
print(sum(elf_cals[:3]))
