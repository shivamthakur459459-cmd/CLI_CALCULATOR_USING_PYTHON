# calculator.py

# Functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    print("=== Simple CLI Calculator ===")
    print("Operations: +  -  *  /")
    print("Type 'exit' anytime to quit.\n")

    while True:
        # Take user input
        choice = input("Enter operation (+, -, *, /) or 'exit': ").strip()

        if choice.lower() == 'exit':
            print("Goodbye! 👋")
            break

        if choice not in ['+', '-', '*', '/']:
            print("Invalid operation! Try again.\n")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number! Please enter numeric values.\n")
            continue

        # Perform operation
        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)

        # ✅ Correct print
        print(f"Result: {result}\n")


if __name__ == "__main__":
    calculator()
