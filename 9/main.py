# https://adventofcode.com/2023/day/9


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/9/input
    lines = f.read().split("\n")

seqs = [[int(c) for c in l.strip().split(" ") if c.strip() != ""] for l in lines if l.strip() != ""]


# PART ONE
def find_next(seq):
    if len([s for s in seq if s != 0]) > 0:
        return seq[-1]+find_next([seq[i+1]-seq[i] for i in range(len(seq)-1)])
    else:
        return 0


print(f"PART ONE: {sum([find_next(s) for s in seqs])}")


# PART TWO
def find_first(seq):
    if len([s for s in seq if s != 0]) > 0:
        return seq[0]-find_first([seq[i+1]-seq[i] for i in range(len(seq)-1)])
    else:
        return 0
    
    
print(F"PART TWO: {sum([find_first(s) for s in seqs])}")