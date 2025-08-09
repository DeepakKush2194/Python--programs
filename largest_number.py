# Write a Python program to find largest number in a list
def largest2(numbers): # 1.Iterative method
    large= 1
    for i in numbers:
        if large < i:
            large = i
    return large
def largest(numbers): #2. Sorting method
    numbers.sort(reverse=True)
    return numbers[0]
numbers = [30, 10, -45, 5, 20]
res = largest(numbers)
print("The largest number in the list is:",res)

#Write a Python program to find second largest number in a list
def sec_largest(numbers):
    large = largest(numbers)
    sec_large = 1
    for i in numbers:
        if sec_large < i < large:
            sec_large = i
    return sec_large

def seclarge(numbers):#better way
    numbers.sort(reverse=True)
    #check for more than 2 elements in list
    if len(numbers) >= 2:
        return numbers[1]
    else:
        return "Insufficient elements"
# numbers = [30, 10, 45, 5, 20]
# res = sec_largest(numbers)
# res2 = seclarge(numbers)
# print("The second largest number in the list is:",res)
# print("The second largest number in the list is:",res2)