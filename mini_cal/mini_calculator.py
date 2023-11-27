def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


def display_result(result):
    print(f"Result: {result}")


def save_to_history(operation, x, y, result):
    with open("calculator_history.txt", "a") as file:
        file.write(f"{x} {operation} {y} = {result}\n")


while True:
    print("Mini Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Display History")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '6':
        print("Exiting the calculator program.")
        break

    if choice in ['1', '2', '3', '4']:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))

        if choice == '1':
            result = add(x, y)
            operation = "+"
        elif choice == '2':
            result = subtract(x, y)
            operation = "-"
        elif choice == '3':
            result = multiply(x, y)
            operation = "*"
        else:
            result = divide(x, y)
            operation = "/"

        display_result(result)
        save_to_history(operation, x, y, result)
    elif choice == '5':
            print("Calculator History:")
            with open("calculator_history.txt", "r") as file:
                history = file.read()
                print(history)

    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5/6).")
