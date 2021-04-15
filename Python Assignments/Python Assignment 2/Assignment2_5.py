def main():
    a = int(input("Enter number: "))
    k = 0
    for i in range(2, a//2 + 1):
        if a % i == 0:
            k = k + 1
    if k <= 0:
        print("It is Prime Number ")
    else:
        print("It is not Prime Number")


if __name__ == '__main__':
    main()
