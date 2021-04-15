def main():
    no = int(input("Enter the number: "))
    total = 0
    for i in range(1, no + 1):
        if no % i == 0:
            if i < no:
                print(i, end=" ")
                total = total + i
    print()
    print("Addition of factors= ", total)


if __name__ == '__main__':
    main()
