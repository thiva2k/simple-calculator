def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("float division by zero")
        return None

def power(a, b):
    return a ** b

def remainder(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        print("float division by zero")
        return None

# Function to select and perform the operation
def select_op(choice):
    if choice in ['+', '-', '*', '/', '^', '%']:
        try:
            num1 = input("Enter first number: ")
            if num1 == '$':
                return 0
            num1 = float(num1)
        except ValueError:
            print("Not a valid number, please enter again")
            return 0

        try:
            num2 = input("Enter second number: ")
            if num2 == '$':
                return 0
            num2 = float(num2)
        except ValueError:
            print("Not a valid number, please enter again")
            return 0

        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            result = remainder(num1, num2)

        print(f"{num1} {choice} {num2} = {result}")

    elif choice == '#':
        return -1
    elif choice == '$':
        return 0
    else:
        print("Unrecognized operation")

# Main loop
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # Take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if select_op(choice) == -1:
        # Program ends here
        print("Done. Terminating")
        exit()
