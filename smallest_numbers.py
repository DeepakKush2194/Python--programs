# Write a Python program to find smallest number in a list.
def smallest2(numbers):# 1.Iterative method
    sml = 1
    for i in numbers:
        if sml > i:
            sml = i
    return sml
def smallest(numbers):# 2.By using sorting
    numbers.sort()
    return numbers[0]
numbers = [30, 10, -45, 5, 20]
res = smallest(numbers)
print("The smallest number in the list is:",res)