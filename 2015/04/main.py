import hashlib

with open("input.txt", "r") as f:
    data = f.read().strip()

p1 = 1
while str(hashlib.md5(f"{data}{p1}".encode()).hexdigest())[:5] != "00000":
    p1 += 1
print(p1)

p2 = p1
while str(hashlib.md5(f"{data}{p2}".encode()).hexdigest())[:6] != "000000":
    p2 += 1
print(p2)
