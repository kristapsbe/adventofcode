with open("input.txt", "r") as f:
    data = f.readlines()

doubles = 0
triples = 0
for l in data:
    cts = {c: l.count(c) for c in set(l)}
    if len([c for c in cts.values() if c == 2]) > 0:
        doubles += 1
    if len([c for c in cts.values() if c == 3]) > 0:
        triples += 1
print(doubles*triples)

rows = len(data)
str_len = len(data[0])
finish = False
for i in range(rows):
    for j in range(i, rows):
        same = [data[i][k] for k in range(str_len) if data[i][k] == data[j][k]]
        if len(same) == str_len - 1:
            print("".join(same))
            finish = True
            break
    if finish:
        break
