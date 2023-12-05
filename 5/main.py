# https://adventofcode.com/2023/day/5

lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/5/input
    lines = f.read().split("\n")

# PART ONE
seeds = [int(l.strip()) for l in lines[0].split(":")[1].split(" ") if l.strip() != ""]
destinations = {}
for l in lines[1:]: # do this is two steps - prep the maps first
    if l.strip() == "":
        continue
    elif ":" in l:
        seeds = [destinations[i] if i in destinations else seeds[i] for i in range(len(seeds))]
        destinations = {}
    else:
        parts = [int(sl.strip()) for sl in l.split(" ") if sl.strip() != ""]
        for i in range(len(seeds)):
            if seeds[i] >= parts[1] and seeds[i] < parts[1]+parts[2]:
                destinations[i] = (seeds[i]-parts[1]+parts[0])
seeds = [destinations[i] if i in destinations else seeds[i] for i in range(len(seeds))]

print(f"PART ONE: {min(seeds)}")

# PART TWO
seeds = []
tmp = [int(l.strip()) for l in lines[0].split(":")[1].split(" ") if l.strip() != ""]
for i in range(int(len(tmp)/2)):
    seeds.append((tmp[2*i], tmp[2*i]+tmp[2*i+1]-1))
    
destinations = []
for l in lines[1:]: # do this is two steps - prep the maps first
    if l.strip() == "":
        continue
    elif ":" in l:
        seeds = seeds+destinations
        destinations = []
    else:
        parts = [int(sl.strip()) for sl in l.split(" ") if sl.strip() != ""]
        seed_start = parts[1]
        seed_end = parts[1]+parts[2]
        dest_start = parts[0]
        dest_end = parts[0]+parts[2]
        delta = dest_start-seed_start

        tmp = []
        for i in range(len(seeds)):
            if seeds[i][1] < seed_start or seeds[i][0] > seed_end: # seed falls fully outside of dest
                tmp.append(seeds[i])
            elif seeds[i][1] <= seed_end and seeds[i][0] >= seed_start: # seed falls fully within dest
                destinations.append((seeds[i][0]+delta, seeds[i][1]+delta))
            elif seeds[i][1] > seed_end and seeds[i][0] < seed_start: # dest falls fully within seed
                destinations.append((dest_start, dest_end))
                tmp.append((seeds[i][0], seed_start))
                tmp.append((seed_end, seeds[i][1]))
            elif seeds[i][0] < seed_start: # seed overlaps dest on the lower side
                destinations.append((dest_start, seeds[i][1]+delta))
                tmp.append((seeds[i][0], seed_start))
            elif seeds[i][1] > seed_end: # seed overlaps dest on the higher side
                destinations.append((seeds[i][0]+delta, dest_end))
                tmp.append((seed_end, seeds[i][1]))
        seeds = list(tmp)

print(f"PART TWO: {min([s[0] for s in seeds+destinations])}")
