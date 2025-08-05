#OOPs
# class Student:
#     def __init__(self, name="Tony", marks=None):
#         self.name = name
#         self.marks = marks
#         self.total = sum(marks)  # Store as instance variable

#     def report(self):
#         avg = self.total / len(self.marks)
#         print(f"Hello {self.name}, your avg score is {avg}")

# s1 = Student(marks=[80,56,77])
# s1.report()

class account:
    def __init__(self,acc_no,balance=0):
        self.acc_no = acc_no
        self.balance = balance
    def bal(self):
        print(f"Your balance is {self.balance}")
    def credit(self, amount):
        self.balance += amount
        print(f"Ammount Rs.{amount} successfully credited to your account.")
        self.bal()
    def debit(self,deb_val):
        self.balance -= deb_val
        print(f"Ammount Rs.{deb_val} successfully debited from your account.")
    @staticmethod
    def welcome():
        print("Welcome to Furfuri bank '-'")

ac1 = account(7,1000)
#ac1.bal()
ac1.credit(500)
#ac1.debit(500)