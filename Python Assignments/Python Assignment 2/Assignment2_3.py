def main():
    no = int(input("Enter number = "))
    b_factorial = 1
    for a in range(1, no + 1):
        # print(a, end=" ")
        b_factorial = a * b_factorial
    print(b_factorial)


if __name__ == '__main__':
    main()
