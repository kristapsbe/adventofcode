from copy import copy


with open("input.txt", "r") as f:
    orig_nums = [int(c) for c in f.read().strip().split(",")]

nums = copy(orig_nums)
nums[1] = 12
nums[2] = 2

pos = 0
while True:
    match nums[pos]:
        case 1:
            nums[nums[pos+3]] = nums[nums[pos+1]]+nums[nums[pos+2]]
        case 2:
            nums[nums[pos+3]] = nums[nums[pos+1]]*nums[nums[pos+2]]
        case 99:
            break
    pos += 4
print(nums[0])

done = False
for i in range(100):
    for j in range(100):
        nums = copy(orig_nums)
        nums[1] = i
        nums[2] = j

        pos = 0
        while True:
            match nums[pos]:
                case 1:
                    nums[nums[pos+3]] = nums[nums[pos+1]]+nums[nums[pos+2]]
                case 2:
                    nums[nums[pos+3]] = nums[nums[pos+1]]*nums[nums[pos+2]]
                case 99:
                    break
            pos += 4
        if nums[0] == 19690720:
            done = True
            break
    if done:
        break
print(100 * nums[1] + nums[2])
