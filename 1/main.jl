# https://adventofcode.com/2023/day/1

# https://docs.julialang.org/en/v1/base/io-network/
io = open(string(join(split(@__FILE__, "/")[1:end-1], "/"), "/input.txt"), "r"); # https://adventofcode.com/2023/day/1/input
lines = split(read(io, String), "\n")
close(io)

# PART ONE
num_lines = Vector{Int}()
for l in lines
    # get only numbers
    tmp = filter(isdigit, l) # https://discourse.julialang.org/t/how-get-only-numbers-from-a-string/61524
    append!(num_lines, parse(Int, string(tmp[1], tmp[end]))) # https://www.geeksforgeeks.org/string-to-number-conversion-in-julia/
end

println(string("PART ONE: ", sum(num_lines)))

# PART TWO
# using a array instead of a Dict because julia is 1-indexed (indices line up nicely as a result)
nums = String["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num_lines = Vector{Int}()
for l in lines
    tmp = Int[]
    for i in eachindex(l) # https://www.geeksforgeeks.org/iterating-over-each-index-of-array-in-julia-eachindex-method/
        for n in eachindex(nums)
            # TODO: not sure why I have to cast both sides to string to compare them
            if string(l[i]) == string(n) || l[i:min(i+length(nums[n])-1, length(l))] == nums[n]
                append!(tmp, n)
            end
        end
    end
    if length(tmp) > 0
        append!(num_lines, parse(Int, string(tmp[1], tmp[end])))
    end
end

println(string("PART TWO: ", sum(num_lines)))