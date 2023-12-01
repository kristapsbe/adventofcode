tmp_lines = []
with open('input.txt', 'r') as f:
    tmp_lines = f.read().split("\n")

# setting up to have something easy to refence when looking for number strings
int_map = {}
ct = 1
for d in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
  int_map[d] = f"{ct}"
  ct = ct + 1

lines = []
for l in tmp_lines:
  tmp_l = ""
  for pos in range(len(l)):
    for d, ct in int_map.items():
      # the numbers can overlap, so we can't just replace
      if l[pos:pos+len(d)] == d or l[pos] == ct:
        tmp_l = f"{tmp_l}{ct}"
  if len(tmp_l) > 0:
    lines.append(tmp_l)

# work out the final result
print(sum([int(f"{l[0]}{l[-1]}") for l in lines]))



