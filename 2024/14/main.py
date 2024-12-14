input = [[[int(c) for c in e.split("=")[1].strip().split(",")] for e in l.split(" ")] for l in open("input.txt", "r").readlines()]

w = 11
h = 7
s = 100
w = 101
h = 103

end_pos = []
for i in input:
    end_pos.append([(i[0][0]+s*i[1][0])%w, (i[0][1]+s*i[1][1])%h])

quadrants = [
    len([e for e in end_pos if e[0] < w//2 and e[1] < h//2]),
    len([e for e in end_pos if e[0] > w//2 and e[1] < h//2]),
    len([e for e in end_pos if e[0] < w//2 and e[1] > h//2]),
    len([e for e in end_pos if e[0] > w//2 and e[1] > h//2]),
]

print(quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3])

def has_square(pos, all_pos, size=4):
    for i in range(size):
        for j in range(size):
            if [pos[0]+i, pos[1]+j] not in all_pos:
                return False
    return True

for t in range(10000): # this is very slow and very dumb, but ir works :D ...
    end_pos = []
    for i in input:
        end_pos.append([(i[0][0]+t*i[1][0])%w, (i[0][1]+t*i[1][1])%h])
    if len([e for e in end_pos if has_square(e, end_pos, 4)]) > 0:
        print("BOOP", t)
