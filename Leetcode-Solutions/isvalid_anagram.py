s = "ab"
t = "aba"

count = {}
count1 = {}

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1
    
for char in t:
    if char in count1:
        count1[char] += 1
    else:
        count1[char] = 1

if count == count1:
    print(True)
else:
    print(False)