with open("input.txt", "r") as f:
    s = f.read().strip()

w = 25
h = 6
l = w * h

min_zeros = l
min_layer = ""
total_image = "2" * l

for i in range(len(s) // l):
    curr_layer = s[i * l : i * l + l]
    total_image = "".join(
        [c if c != "2" else curr_layer[j] for j, c in enumerate(total_image)]
    )
    ct_zeros = curr_layer.count("0")
    if ct_zeros < min_zeros:
        min_zeros = ct_zeros
        min_layer = curr_layer

print(min_layer.count("1") * min_layer.count("2"))
for i in range(h):
    print([" " if c == "0" else c for c in total_image[i * w : i * w + w]])
