def addition(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")
    return answer


def subtraction(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}")
    return answer


def multiplication(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer}")
    return answer


def division(a, b):
    try:
        answer = a / b
        print(f"{a} / {b} = {answer}")
        return answer
    except:
        print("you cannot divide by zero")
        return None


while True:
    print("Welcome to simple Calculator. Coose an operator ")
    print("A for Addition")
    print("B for Substraction")
    print("C for Multiplication")
    print("D for Division")
    print("E for quitting")
    print()

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    choice = input("Enter the operator: ").lower()

    if choice == 'a':
        print("Addition")
        addition(a, b)
    elif choice == 'b':
        print("Subtraction")
        subtraction(a, b)
    elif choice == 'c':
        print("Multiplication")
        multiplication(a, b)
    elif choice == 'd':
        print("Division")
        division(a, b)
    elif choice == 'e':
        break
