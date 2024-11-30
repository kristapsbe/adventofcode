# https://adventofcode.com/2023/day/15


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/15/input
    lines = [l.strip() for l in f.read().split("\n") if l.strip() != ""]

vals = lines[0].split(",")


# PART ONE
def get_hash(s):
    cv = 0
    for c in s:
        cv = ((cv+ord(c)))*17%256
    return cv

hashes = [get_hash(v) for v in vals]
print(f"PART ONE: {sum(hashes)}")


# PART TWO
boxes = [[] for _ in range(256)]
lens_map = {}
for v in vals:
    #print(f"step {v}")
    if "=" in v:
        parts = v.split("=")
        lens_map[parts[0]] = int(parts[1])
        box_id = get_hash(parts[0])
        #print(f"= boxid {box_id} lens label {parts[0]} lens foc {parts[1]}")
        if parts[0] not in boxes[box_id]:
            boxes[box_id].append(parts[0])
    elif "-" in v:
        parts = v.split("-")
        box_id = get_hash(parts[0])
        #print(f"- boxid {box_id} lens label {parts[0]}")
        if parts[0] in boxes[box_id]:
            lens_pos = boxes[box_id].index(parts[0])
            boxes[box_id] = boxes[box_id][:lens_pos]+boxes[box_id][lens_pos+1:]

    #ct = 0
    #for b in boxes:
    #	if len(b) > 0:
    #		print(f"{ct} {b}")
    #	ct = ct+1
    #print()

res = []
for i in range(len(boxes)):
    if len(boxes[i]) > 0:
        for j in range(len(boxes[i])):
            res.append((i+1)*(j+1)*lens_map[boxes[i][j]])

print(f"PART TWO: {sum(res)}")