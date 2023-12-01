lines = []
with open('input.txt', 'r') as f:
    lines = f.read().split("\n")

# get only numbers
tmp = ["".join([c for c in l if c.isnumeric()]) for l in lines if l.strip() != '']

# work out the final result
print(sum([int(f"{l[0]}{l[-1]}") for l in tmp]))
