

#random number generator 
#import random
#print(f"Random number: {random.randint(1,100)}")



#Calendar printer
#import calendar 
#year = int(input("Enter Year:"))
#month = int(input("Enter month:"))
#cal = calendar.month(year,month)
#print(cal)

#a = float(input("Enter a number: "))
#if a > 0:
#    print("Positive ")
#elif a == 0:
#    print("Zero")
#else:
#    print("Negative ")

#OddEven
#a = float(input("Enter a number: "))
#if a % 2 == 0:
#    print("Even number ")
#else:
#    print("Odd number ")

#leap year  ???
#year = int(input("Enter the year: "))
#if year%100==0 and year%400==0:
#    print(f"{year} is a leap year.")
#elif year%100!=0 and year%4==0:
#    print(f"{year} is leap year.")
#else:
#    print("Not a leap year.")

#Prime number
#import math
#n = int(input("Enter a number: "))
#is_prime = False
#if n <= 1:
#    print(f"{n} is not a prime number.")
#elif n > 1:
#    for i in range(2, int(math.sqrt(n)) + 1):
#        if (n % i)== 0:
#            is_prime = True
#            break
#if flag:
#    print(f"{n} not a prime number.")
#else:
#    print(f"{n} is a prime number.")

#Print prime numbers in range
#import math
#a = int(input("Enter range, from: "))
#b = int(input("To: "))
#print(f"Prime numbers in the range of {a} to {b} are:")
#for n in range(a, b):
#    if n > 1:
#        is_prime = True
#        for i in range(2, int(math.sqrt(n)) + 1):
#            if(n % i) == 0:
#                is_prime = False
#                break
#        if is_prime:
#            print(n)

#factorial
#nterms = int(input("Enter number of terms: "))
#factorial = 1
#if nterms < 0:
#    print("Factorial for negetive number is not possible ")
#elif nterms == 0:
#    print("Factorial is 1.")
#else:
#    for i in range(1,nterms + 1):
#        factorial = factorial * i
#    print(f"Factorial of {nterms} is equals to {factorial }.")

#Fibonacci series 
#nterms = int(input("Enter number of terms: "))
#n1, n2 = 0, 1
#count = 0
#if nterms == 0:
#    print("Please enter only positive number.")
#elif nterms == 1:
#    print(n1)
#else:
#    print("Fibonacci series: ")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1

#armstrong number 
#num = int(input("Enter a number: "))
#num_digit = len(str(num))
#sum_of_powers = 0
#temp_num = num
#while temp_num > 0:
#    digit = temp_num % 10
#    sum_of_powers += digit ** num_digit
#    temp_num //= 10

#if sum_of_powers == num:
#    print(f"{num} is a Armstrong number.")
#else:
#    print(f"{num} is not a Armstrong number.")  

#Program to count Armstrong number in interval
#lower = int(input("Enter lower limit:"))
#upper = int(input("Enter upper limit:"))
#for num in range(lower, upper + 1):
#    order = len(str(num))
#    temp_num = num
#    sum = 0
#    while temp_num > 0:
#        digit = temp_num % 10
#        sum += digit ** order
#        temp_num //= 10
#    if sum == num:
#        print(num)

#Sum of natural numbers 
#limit = int(input("Enter the limit: "))
#sum = 0
#for num in range(1, limit + 1):
#    sum += num
#    
#print(f"{sum} is the sum of {limit} natural numbers ")

#Decimal to binary, octal, hexadecimal
#num = int(input("Enter decimal number: "))
#print(f"Decimal value of {num} is:")
#print(f"{bin(num)} in binary.")
#print(f"{oct(num)} in octal.")
#print(f"{hex(num)} in hexadecimal.")

#basic calculator 
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def multi(a, b):
    return a * b
def div(a, b):
    return a / b

print("Select one of the operation:")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = int(input("Enter your choice: "))
    if choice in (1,2,3,4):
        try:
            x = int(input("Enter first number: "))
            y = int(input("Enter first number: "))
        except ValueError:
            print("Invalid input, enter a number.")

        if choice == 1:
            print(x,"+",y,"=",add(x, y))
        elif choice == 2:
            print(x,"-",y,"=",sub(x, y))
        elif choice == 3:
            print(x,"-",y,"=",multi(x, y))