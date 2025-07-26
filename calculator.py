from datetime import datetime
def add(a, b): return a + b
def sub(a, b): return a - b
def multi(a, b): return a * b
def div(a, b): return "Error: Division by zero" if b == 0 else a / b

history = []

print("Select one of the operations:")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. View Calculation History")

while True:
    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice in (1, 2, 3, 4):
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if choice == 1:
            result = add(x, y)
            entry = f"[{timestamp}] {x} + {y} = {result}"
        elif choice == 2:
            result = sub(x, y)
            entry = f"[{timestamp}] {x} - {y} = {result}"
        elif choice == 3:
            result = multi(x, y)
            entry = f"[{timestamp}] {x} × {y} = {result}"
        elif choice == 4:
            result = div(x, y)
            entry = f"[{timestamp}] {x} ÷ {y} = {result}"

        print(entry)
        history.append(entry)

    elif choice == 5:
        if history:
            print("\nCalculation History:")
            for entry in history:
                print(entry)
        else:
            print("No calculations yet.")

    else:
        print("Invalid choice. Please select from 1 to 5.")

    next_calculation = input("Do another calculation? (yes/no): ").lower()
    if next_calculation != "yes":
        print("Thanks for using the calculator!")
        break