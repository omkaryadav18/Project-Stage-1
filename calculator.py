def add(a, b):
    return a+b

def sub(a, b):
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    if b != 0:
        return a/b
    return "Division not allowed"

while True:
    print("MENU:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. MUltiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("enter ur choice: ")

    if choice == "5":
        print("exiting program")
        break

    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))

    if choice == "1":
        print("Result: ", add(num1,num2))
    elif choice == "2":
        print("Result: ", sub(num1,num2))
    elif choice == "3":
        print("Result: ", mul(num1,num2))
    elif choice == "4":
        print("Result: ", div(num1,num2))
    else:
        print("invalid choice. Please try again")