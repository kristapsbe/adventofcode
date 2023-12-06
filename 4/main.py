# https://adventofcode.com/2023/day/4


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/4/input
    lines = f.read().split("\n")

# PART ONE
win_vals = [[cv.strip() for cv in l.split("|")[0].split(":")[1].split(" ")] for l in lines]
card_vals = [[cv.strip() for cv in l.split("|")[1].split(" ")] for l in lines]

win_nums = []
for i in range(len(card_vals)):
    win_nums.append([cv for cv in card_vals[i] if cv in win_vals[i] and cv != '']) 

print(f"PART ONE: {sum([2**(len(w)-1) for w in win_nums if len(w) > 0])}") # I always forget that pow is ** instead of ^

# PART TWO
cards = [1]*len(lines)

for i in range(len(cards)):
    if len(win_nums[i]) > 0: # we may as well reuse the scores we calculated before
        for j in range(len(win_nums[i])):
            cards[i+j+1] = cards[i+j+1]+cards[i]
        # remember you don't need to remove the cards that you've processed

print(f"PART TWO: {sum(cards)}")
