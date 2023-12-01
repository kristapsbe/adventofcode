lines = []
with open('input.txt', 'r') as f:
    lines = f.read().split("\n")

tmp = ["".join([c for c in l if c.isnumeric()]) for l in lines if l.strip() != '']
print(sum([int(f"{l[0]}{l[-1]}") for l in tmp]))
