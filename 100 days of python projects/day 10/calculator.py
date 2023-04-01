import art


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def subtract(a, b):
    return a - b


def start_calculator():
    print(art.logo)
    operations = {
        "+": add,
        "*": multiply,
        "/": divide,
        "-": subtract
    }

    result = float(input("What's the first number? "))
    do_continue = True

    while do_continue:
        for operation in operations:
            print(operation)

        operation_type = input(f"Pick an operation: ")
        while operation_type not in operations:
            operation_type = input("Invalid operation. Please pick a valid operation: ")

        other_number = float(input("Enter next number: "))

        function_calc = operations[operation_type]
        result = function_calc(result, other_number)

        print(f"{result} {operation_type} {other_number}  =  {result}")

        user_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation ")
        while user_continue not in ['y', 'n']:
            user_continue = input("Invalid input. Please type 'y' or 'n': ")

        if user_continue == 'n':
            do_continue = False

    if do_continue == False:
        start_calculator()

start_calculator()


