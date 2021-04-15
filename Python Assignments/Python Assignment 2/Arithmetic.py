def add():
    print("Addition of two numbers")
    a = int(input("Enter the number "))
    b = int(input("Enter the number ", ))
    print("Addition is = ", a + b)


def sub():
    print("Subtraction of two numbers")
    a = int(input("Enter the number "))
    b = int(input("Enter the number ", ))
    if a < b:
        a, b = b, a
        print("Subtraction is =  ", a - b)
    else:
        print("Subtraction is =  ", a - b)


def mult():
    print("Multiplication of two numbers")
    a = float(input("Enter the number "))
    b = float(input("Enter the number ", ))
    ans = a * b
    print("Multiplication is = ", ans)


def div():
    print("Division of two numbers")
    a = float(input("Enter the number "))
    b = float(input("Enter the number ", ))
    print("Division is = ", a / b)
    print("Remainder is = ", a % b)


