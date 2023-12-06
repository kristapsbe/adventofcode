# https://adventofcode.com/2023/day/3


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/3/input
    lines = f.read().split("\n")

# PART ONE
def check_is_symbol(lines, i, j, k, l, w, h):
    return (not lines[max(min(i+k, w)-1, 0)][max(min(j+l, h)-1, 0)].isnumeric() and not lines[max(min(i+k, w)-1, 0)][max(min(j+l, h)-1, 0)] == '.')


part_nums = []
h = len(lines)
w = len(lines[0]) if h > 0 else 0
for i in range(h):
    curr_num = []
    is_symbol = False
    for j in range(w): # I only expect numbers to be written out horizontally 
        if lines[i][j].isnumeric():
            if not is_symbol: # no point checking if we already know there was a symbol
                for k in range(3): # looping through the 9 cells around the current digit and checking if I we can find a symbol
                    for l in range(3):
                        is_symbol = is_symbol or check_is_symbol(lines, i, j, k, l, w, h)
            curr_num.append(lines[i][j])
        else:
            if len(curr_num) > 0: # only need to do something if a number has ended
                if is_symbol:
                    part_nums.append(int("".join(curr_num)))
                curr_num = []
            is_symbol = False
                
    if len(curr_num) > 0: # dealing with cases where a number is at the end of the line
        if is_symbol:
            part_nums.append(int("".join(curr_num)))
        curr_num = []

print(f"PART ONE: {sum(part_nums)}")

# PART TWO
def is_valid_coord(i, j, k, l, w, h):
    return i+k <= w and i+k > 0 and j+l <= h and j+l > 1


gear_products = []
for i in range(h):
    for j in range(w):
        if lines[i][j] == '*': # I don't think there's much of a point in looking for numbers unless we find a *
            surr_nums = {} # note - I still only think of digits as forming numbers horizontally
            for k in range(3):
                for l in range(3):
                    if is_valid_coord(i, j, k, l, w, h) and lines[i+k-1][j+l-1].isnumeric(): # check if we'er not trying to start outside of the input and if there's a digit to work with
                        ik = i+k-1 # row that we're working with
                        l_jl = j+l-1
                        while l_jl-1 >= 0 and lines[ik][l_jl-1].isnumeric():
                            l_jl = l_jl-1
                        r_jl = j+l-1
                        while r_jl+1 < w and lines[ik][r_jl+1].isnumeric():
                            r_jl = r_jl+1
                        surr_nums[f"{ik}:{l_jl}-{r_jl}"] = int(lines[ik][l_jl:r_jl+1])
            if len(surr_nums) == 2:
                vals = list(surr_nums.values())
                gear_products.append(vals[0]*vals[1])
                        
print(f"PART TWO: {sum(gear_products)}")