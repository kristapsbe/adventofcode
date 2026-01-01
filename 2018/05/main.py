import string

with open("input.txt", "r") as f:
    data = f.read().strip()

pairs = [
    p
    for ps in [
        [
            f"{string.ascii_lowercase[i]}{string.ascii_uppercase[i]}",
            f"{string.ascii_uppercase[i]}{string.ascii_lowercase[i]}",
        ]
        for i in range(26)
    ]
    for p in ps
]

tmp_data = str(data)
prev_len = len(tmp_data) + 1
while prev_len != len(tmp_data):
    prev_len = len(tmp_data)
    for p in pairs:
        tmp_data = tmp_data.replace(p, "")
print(len(tmp_data))

res = []
for c in string.ascii_lowercase:
    tmp_data = str(data)
    tmp_data = tmp_data.replace(c, "").replace(c.upper(), "")
    prev_len = len(tmp_data) + 1
    while prev_len != len(tmp_data):
        prev_len = len(tmp_data)
        for p in pairs:
            tmp_data = tmp_data.replace(p, "")
    res.append(len(tmp_data))
print(min(res))
