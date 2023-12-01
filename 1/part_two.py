int_map = {}
ct = 1
for d in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
  int_map[d] = f"{ct}"
  ct = ct + 1

tmp_lines = []
with open('input.txt', 'r') as f:
    tmp_lines = f.read().split("\n")

lines = []
for l in tmp_lines:
  tmp_l = ""
  for pos in range(len(l)):
    for d, ct in int_map.items():
      if l[pos:pos+len(d)] == d or l[pos] == ct:
        tmp_l = f"{tmp_l}{ct}"
  if len(tmp_l) > 0:
    lines.append(tmp_l)

print(sum([int(f"{l[0]}{l[-1]}") for l in lines]))



