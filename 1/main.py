lines = []
with open('input.txt', 'r') as f:
    lines = f.read().split("\n")

# PART ONE
# get only numbers
tmp = [[c for c in l if c.isnumeric()] for l in lines if l.strip() != '']

# work out the final result
print(f"PART ONE: {sum([int(f'{l[0]}{l[-1]}') for l in tmp])}")

# PART TWO
# setting up to have something easy to refence when looking for number strings
int_map = {}
ct = 1
for d in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
  int_map[d] = f"{ct}"
  ct = ct + 1

num_lines = []
for l in lines:
  tmp_l = []
  for pos in range(len(l)):
    for d, ct in int_map.items():
      # the numbers can overlap, so we can't just replace
      if l[pos:pos+len(d)] == d or l[pos] == ct:
        tmp_l.append(ct)
  if len(tmp_l) > 0:
    num_lines.append(tmp_l)

# work out the final result
print(f"PART TWO: {sum([int(f'{l[0]}{l[-1]}') for l in num_lines])}")



