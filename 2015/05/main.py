with open("input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

vowels = set("aeiou")

blacklist = ["ab", "cd", "pq", "xy"]

p1 = 0
for d in data:
    if (
        not any([b in d for b in blacklist])
        and len([c for c in d if c in vowels]) > 2
        and len([i for i in range(len(d) - 1) if d[i] == d[i + 1]]) > 0
    ):
        p1 += 1
print(p1)

p2 = 0
for d in data:
    cl = len(d)
    if (
        any([cl - len(d.replace(d[i : i + 2], "")) > 3 for i in range(len(d) - 1)])
        and len([i for i in range(cl - 2) if d[i] == d[i + 2]]) > 0
    ):
        p2 += 1
print(p2)
