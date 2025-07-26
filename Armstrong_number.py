#Armstrong number 
num = int(input("Enter a number: "))
num_digit = len(str(num))
sum_of_powers = 0
temp_num = num
while temp_num > 0:
   digit = temp_num % 10
   sum_of_powers += digit ** num_digit
   temp_num //= 10

if sum_of_powers == num:
   print(f"{num} is a Armstrong number.")
else:
   print(f"{num} is not a Armstrong number.")

#Program to count Armstrong number in interval
lower = int(input("Enter lower limit:"))
upper = int(input("Enter upper limit:"))
for num in range(lower, upper + 1):
   order = len(str(num))
   temp_num = num
   sum = 0
   while temp_num > 0:
       digit = temp_num % 10
       sum += digit ** order
       temp_num //= 10
   if sum == num:
       print(num)