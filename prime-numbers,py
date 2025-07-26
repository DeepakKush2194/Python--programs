#Prime number
import math
n = int(input("Enter a number: "))
is_prime = False
if n <= 1:
   print(f"{n} is not a prime number.")
elif n > 1:
   for i in range(2, int(math.sqrt(n)) + 1):
       if (n % i)== 0:
           is_prime = True
           break
if is_prime:
   print(f"{n} not a prime number.")
else:
   print(f"{n} is a prime number.")

#Print prime numbers in range
#import math
a = int(input("Enter range, from: "))
b = int(input("To: "))
print(f"Prime numbers in the range of {a} to {b} are:")
for n in range(a, b):
   if n > 1:
       is_prime = True
       for i in range(2, int(math.sqrt(n)) + 1):
           if(n % i) == 0:
               is_prime = False
               break
       if is_prime:
           print(n)