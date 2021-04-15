class Circle:
    def __init__(self, no1):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
        self.PI = 3.14

    def Accept(self, no1):
        self.Radius = no1

    def CalculateArea(self):
        self.Area = self.PI * self.Radius ** 2

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius

    def Display(self):
        print("Circle Radius is = ", self.Radius)
        print("Circle Area is = ", self.Area)
        print("Circle Circumference is =  ", self.Circumference)


def main():
    no = int(input("Enter the Radius : "))
    obj = Circle(no)
    obj.Accept(no)
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()


if __name__ == '__main__':
    main()
