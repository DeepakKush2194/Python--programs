#Calendar printer
import calendar 
year = int(input("Enter Year:"))
month = int(input("Enter month:"))
cal = calendar.month(year,month)
print(cal)