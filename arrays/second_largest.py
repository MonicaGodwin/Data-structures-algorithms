numbers = [10, 5, 8, 20, 3, 1]
largest_num = 0
second_largest = largest_num
for number in numbers:
    if number > largest_num:
        second_largest = largest_num
        largest_num = number
            
    elif number > second_largest:
        second_largest = number

print(largest_num)
print(second_largest)
