#factorial
nterms = int(input("Enter number of terms: "))
factorial = 1
if nterms < 0:
   print("Factorial for negetive number is not possible ")
elif nterms == 0:
   print("Factorial is 1.")
else:
   for i in range(1,nterms + 1):
       factorial = factorial * i
   print(f"Factorial of {nterms} is equals to {factorial }.")