def main():
    my_list = []
    total = 0
    n = int(input("Enter Number of Elements : "))
    for i in range(0, n):
        ele = int(input("Input Elements: "))
        my_list.append(ele)
        total = total + ele
    print(my_list)
    print("Output", total)


if __name__ == '__main__':
    main()
