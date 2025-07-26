def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("Select one of the operations:")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if choice in (1, 2, 3, 4):
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == 1:
            print(f"{x} + {y} = {add(x, y)}")
        elif choice == 2:
            print(f"{x} - {y} = {sub(x, y)}")
        elif choice == 3:
            print(f"{x} × {y} = {multi(x, y)}")
        elif choice == 4:
            result = div(x, y)
            print(f"{x} ÷ {y} = {result}")

        next_calculation = input("Do another calculation? (yes/no): ").lower()
        if next_calculation != "yes":
            print("Thanks for using the calculator!")
            break
    else:
        print("Invalid choice. Please select from 1 to 4.")