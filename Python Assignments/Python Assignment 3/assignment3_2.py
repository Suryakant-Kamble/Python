def main():
    a_list = []
    no = int(input("Number of elements: "))
    print()
    for i in range(0, no):
        n = int(input("Enter elements: "))
        a_list.append(n)
    print(a_list)
    print("Maximum Number is: ", max(a_list))


if __name__ == '__main__':
    main()
