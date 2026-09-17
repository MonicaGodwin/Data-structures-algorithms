numbers = [10, 5, 8, 20, 3]
target = 5
found = False
for i, number in enumerate(numbers):
    if number == target:
        print(i)
        found = True
        break
if not found:
    print("Not found")