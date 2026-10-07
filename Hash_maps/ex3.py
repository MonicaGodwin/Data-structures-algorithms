nums = [1, 2, 3, 4]

seen = {}
duplicate = False
for num in nums:
    if num in seen:
        duplicate = True
    else:
        seen[num] = 1
print(duplicate)
