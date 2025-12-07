from dataclasses import dataclass
from operator import le

with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

p1 = 0
p2 = 0
for l in data:
    parts = l.split(": ")
    pw = parts[1]
    parts = parts[0].split(" ")
    letter = parts[1]

    min_max = [int(i) for i in parts[0].split("-")]
    cts = {c: pw.count(c) for c in set(pw)}
    if letter in cts and (cts[letter] >= min_max[0] and cts[letter] <= min_max[1]):
        p1 += 1
    if bool(min_max[0] <= len(pw) and pw[min_max[0] - 1] == letter) != bool(
        min_max[1] <= len(pw) and pw[min_max[1] - 1] == letter
    ):
        p2 += 1
print(p1)
print(p2)
