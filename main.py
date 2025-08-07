#Write a Python program to Multiply all numbers in the list.
def list_multi(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
# numbers = [10, 20, 30, 40, 50]
# res = list_multi(numbers)
#print("Product of elements in the list:",res)

# Write a Python program to find smallest number in a list.
def smallest(numbers):
    sml = 1
    for i in numbers:
        if sml > i:
            sml = i
    return sml
# numbers = [30, 10, -45, 5, 20]
# res = smallest(numbers)
#print("The smallest number in the list is:",res)

# Write a Python program to find largest number in a list
def largest(numbers):
    large= 1
    for i in numbers:
        if large < i:
            large = i
    return large
# numbers = [30, 10, -45, 5, 20]
# res = largest(numbers)
#print("The largest number in the list is:",res)

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

#Write a Python program to find N largest elements from a list
def n_largest(numbers):
    


numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]
