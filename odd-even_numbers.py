#Write a Python program to print even numbers in a list
def evens(numbers):
    even_nums = [num for num in numbers if num % 2 == 0]
    return even_nums
def odds(numbers):
    odd_nums = [num for num in numbers if num % 2 != 0]
    return odd_nums
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = evens(numbers)
print("Even numbers from the list:",res)
res2 = odds(numbers)
print("Even numbers from the list:",res2)

