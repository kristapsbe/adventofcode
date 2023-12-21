# https://adventofcode.com/2023/day/20


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/20/input
    lines = [l.strip() for l in f.read().split("\n") if l.strip() != ""]

