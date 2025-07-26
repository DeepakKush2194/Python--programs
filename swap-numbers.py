#swap numbers with variable
num1, num2 = int(input("Enter first number:")),int(input("Enter second number:"))
print(f"Before swapping\nFirst number:{num1}\tSecond number:{num2}")
temp = num1
num1 = num2
num2 = temp
print(f"After swapping\nFirst number:{num1}\tSecond number:{num2}")

#swapping without temp variable
a = 5
b = 10
a, b = b, a
print(f"a = {a}\tb = {b}")