class Demo:
    def __init__(self, value1, value2):
        self.no1 = value1
        self.no2 = value2
        # print(self.no1, self.no2)

    def Fun(self):
        print(self.no1, self.no2)

    def Gun(self):
        print(self.no1, self.no2)


def main():
    # no1 = int(input("Enter no1 Value : "))
    # no2 = int(input("Enter no2 value : "))
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)
    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()


if __name__ == '__main__':
    main()

