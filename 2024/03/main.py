import re

input = open("input.txt", "r").read()

print(sum([int(s.split("(")[1].split(",")[0])*int(s.split(")")[0].split(",")[1]) for s in re.findall(r'mul\([0-9]+\,[0-9]+\)', input)]))

parts = re.findall(r'(mul\([0-9]+\,[0-9]+\)|do\(\)|don\'t\(\))', input)
res = 0
do = True
for p in parts:
    if p == "do()":
        do = True
    elif p  == "don't()":
        do = False
    elif do:
        res += int(p.split("(")[1].split(",")[0])*int(p.split(")")[0].split(",")[1])
print(res)
