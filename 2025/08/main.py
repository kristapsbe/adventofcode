import math
from copy import copy

with open("input.txt", "r") as f:
    coords = [[int(c) for c in l.strip().split(",")] for l in f.readlines()]

distances = {}
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        d = (
            ((coords[i][0] - coords[j][0]) ** 2)
            + ((coords[i][1] - coords[j][1]) ** 2)
            + ((coords[i][2] - coords[j][2]) ** 2)
        ) ** (0.5)
        distances[d] = set([i, j])

sorted_keys = sorted(distances.keys())
circuits = []
for i in range(1000):
    unmatched = []
    new_circuit = copy(distances[sorted_keys[i]])
    for c in circuits:
        if len(c & new_circuit) > 0:
            new_circuit |= c
        else:
            unmatched.append(c)
    circuits = unmatched
    circuits.append(new_circuit)
print(math.prod(sorted([len(c) for c in circuits], reverse=True)[:3]))


node_ct = len(sorted_keys)
circuits = []
i = -1
while len(circuits) != 1 or len(circuits[0]) != len(coords):
    i += 1
    unmatched = []
    new_circuit = copy(distances[sorted_keys[i]])
    for c in circuits:
        if len(c & new_circuit) > 0:
            new_circuit |= c
        else:
            unmatched.append(c)
    circuits = unmatched
    circuits.append(new_circuit)
last = list(distances[sorted_keys[i]])
print(coords[last[0]][0] * coords[last[1]][0])
