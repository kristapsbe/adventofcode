# https://adventofcode.com/2023/day/13


lines = []
# __file__ contains the path to the current file - https://stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
with open(f'{"/".join(__file__.split("/")[:-1])}/input.txt', 'r') as f: # https://adventofcode.com/2023/day/13/input
	lines = [l.strip() for l in f.read().split("\n")]

blocks = []
block = []
for l in lines:
	if l == "":
		blocks.append(block)
		block = []
	else:
		block.append(l)
if len(block) > 0:
	blocks.append(block)


# TODO: I can just turn both of these into one
def find_reflection(b):
	ret_val = 0
	h = len(b)
	for r in range(h-1):
		ri = r+1
		# reflection between rows
		is_same = True
		for i in range(min(ri, h-ri)):
			if b[ri-i-1] != b[ri+i]:
				is_same = False
				break
		if is_same:
			ret_val = ri
			break
		# reflection on row
		is_same = True
		for i in range(min(ri, h-ri)+1):
			if b[ri-i] != b[ri+i-1]:
				is_same = False
				break
		if is_same:
			ret_val = ri
			break	
	return ret_val


def find_reflection_with_one_c(b):
	ret_val = 0
	h = len(b)
	w = len(b[0])
	for r in range(h-1):
		ri = r+1
		# TODO: there's probably a neater way to deal with the two entries being different
		# reflection between rows
		is_same = True
		used_c = False
		for i in range(min(ri, h-ri)):
			if b[ri-i-1] != b[ri+i]:
				if not used_c and len([0 for j in range(w) if b[ri-i-1][j] != b[ri+i][j]]) == 1:
					used_c = True
				else:
					is_same = False
					break
		if is_same and used_c:
			ret_val = ri
			break
		# reflection on row
		is_same = True
		for i in range(min(ri, h-ri)+1):
			if b[ri-i] != b[ri+i-1]:
				if not used_c and len([0 for j in range(w) if b[ri-i][j] != b[ri+i-1][j]]) == 1:
					used_c = True
				else:
					is_same = False
					break
		if is_same and used_c:
			ret_val = ri
			break	

	return ret_val


ret = []
for b in blocks:
	bt = [[br[j] for br in b] for j in range(len(b[0]))] # transpose
	ret.append(100*find_reflection(b)+find_reflection(bt))

#print(ret)
print(f"PART ONE: {sum(ret)}")

ret = []
for b in blocks:
	bt = [[br[j] for br in b] for j in range(len(b[0]))] # transpose
	ret.append(100*find_reflection_with_one_c(b)+find_reflection_with_one_c(bt))

#print(ret)
print(f"PART TWO: {sum(ret)}")
