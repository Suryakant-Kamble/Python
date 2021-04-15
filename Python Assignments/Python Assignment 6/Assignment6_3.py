class Arithmetic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self, no1, no2):
        self.value1 = no1
        self.value2 = no2

    def Addition(self):
        result = self.value1 + self.value2
        print("Addition is = ", result)

    def Subtraction(self):
        result = self.value1 - self.value2
        print("Subtraction is = ", result)

    def Multiplication(self):
        result = self.value1 * self.value2
        print("Multiplication is = ", result)

    def Division(self):
        result = self.value1 / self.value2
        print("Division is = ", result)


def main():
    a = int(input("Enter value1 : "))
    b = int(input("Enter value2 = "))
    obj = Arithmetic()
    obj.Accept(a, b)
    obj.Addition()
    obj.Subtraction()
    obj.Multiplication()
    obj.Division()


if __name__ == '__main__':
    main()
