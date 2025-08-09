#Write a Python program to find N largest elements from a list
def n_largest(numbers,k):
    numbers.sort(reverse=True)
    result = numbers[:k]
    return result
numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]
k = int(input("Number of largest numbers: "))
res = n_largest(numbers,k)
print(f"The {k} largests number in the list is:",res)
