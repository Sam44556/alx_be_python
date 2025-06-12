# Prompt the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to choose an operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match-case (Python 3.10+)
match operation:
    case "+":
        print(f"The result is {num1 + num2}.")
    case "-":
        print(f"The result is {num1 - num2}.")
    case "*":
        print(f"The result is {num1 * num2}.")
    case "/":
        if num2 != 0:
            print(f"The result is {num1 / num2}.")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation.")
