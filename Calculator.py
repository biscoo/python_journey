# Simple Calculator Program

def add(n1, n2):
    """Return the sum of two numbers."""
    return n1 + n2

def sub(n1, n2):
    """Return the difference of two numbers (n1 - n2)."""
    return n1 - n2

def mul(n1, n2):
    """Return the product of two numbers."""
    return n1 * n2

def div(n1, n2):
    """Return the quotient of two numbers (n1 / n2)."""
    return n1 / n2


# Dictionary mapping operator symbols to corresponding functions
operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

# Main calculator loop
func = True
while func:
    mem = 'y'
    # Ask the user to type the first number
    num_1 = int(input("Please enter the first number: "))

    while mem == 'y':
        # Ask for operator
        op = input("Please choose an operation (+, -, *, /): ")
        num_2 = int(input("Please enter the second number: "))

        # Perform calculation using operator dictionary
        output = operators[op](num_1, num_2)
        print(f"You chose to {op} {num_1} and {num_2}, result = {output}")

        # Ask whether to continue with result
        mem = input("Do you want to continue with the same result? [y/n]: ").lower()
        if mem == 'y':
            num_1 = output
        else:
            # Clear screen
            print("\n" * 20)
            mem = 'n'
