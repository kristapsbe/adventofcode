import functools
# https://adventofcode.com/2023/day/7


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/7/input
    lines = f.read().split("\n")


def assign_type(cd, part): # just being really explicit about it to avoid confusion
    c_count = max([v for _,v in cd.items()])

    if part == 2 and 'J' in cd and len(cd) > 1:
        c_count = max([v if k != 'J' else 0 for k,v in cd.items()])+cd['J']
        del cd['J'] # it's technically possible to get full house if you start off with something like AATTJ https://www.reddit.com/r/adventofcode/comments/18cr4xr/2023_day_7_better_example_input_not_a_spoiler/
    if c_count == 5: # Five of a kind
        return 0
    if c_count == 4: # Four of a kind
        return 1
    if c_count == 3 and len(cd) == 2: # Full house
        return 2
    if c_count == 3: # Three of a kind
        return 3
    if c_count == 2 and len(cd) == 3: # Two pair
        return 4
    if c_count == 2: # One pair
        return 5
    # High card
    return 6


# PART ONE
card_order = "AKQJT98765432" 


def compare(item1, item2): # https://stackoverflow.com/questions/5213033/sort-a-list-of-lists-with-a-custom-compare-function
    if item1[3] != item2[3]:
        return item2[3]-item1[3]
	# second ordering rule - go from left to right and find the strongest card
    for i in range(len(item1[0])):
        if card_order.index(item1[0][i]) != card_order.index(item2[0][i]):
            return card_order.index(item2[0][i])-card_order.index(item1[0][i])
	# same score
    return 0	


def do_score(hands, affix, part):
    p_hands = list(hands)
    for i in range(len(p_hands)): # need to have the num of each card worked out anyhow - may as well do it now
        tmp = {c: p_hands[i][0].count(c) for c in set(p_hands[i][0])} # https://www.simplilearn.com/tutorials/python-tutorial/count-in-python
        p_hands[i].append(tmp) 
        p_hands[i].append(assign_type(tmp, part))

    p_hands.sort(key=functools.cmp_to_key(compare))
    res = []
    for i in range(len(p_hands)):
        res.append(int(p_hands[i][1])*(i+1))
    print(f"{affix}: {sum(res)}")


hands = [l.split() for l in lines if l.strip() != ""]
do_score(hands, "PART ONE", 1)

# PART TWO
part = 2
card_order = "AKQT98765432J" 

hands = [l.split() for l in lines if l.strip() != ""]
do_score(hands, "PART TWO", 2) # should be 249356515 - I've still got it wrong
