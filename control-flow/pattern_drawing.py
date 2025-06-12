# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer loop using while
while row < size:
    # Inner loop using for to print each row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
