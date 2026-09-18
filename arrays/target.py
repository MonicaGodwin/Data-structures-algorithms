numbers = [10, 5, 8, 20, 3]
target = 3
found = False
for i, number in enumerate(numbers):
    if number == target:
        print(i)
        found = True
if not found:
    print("Not found")