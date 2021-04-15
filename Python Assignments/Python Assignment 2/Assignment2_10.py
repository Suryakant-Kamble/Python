def main():
    a = list(input("Enter the number: "))
    total = 0
    for i in range(len(a)):
        b = int(a[i])
        total = total + b
    print(total)


main()
