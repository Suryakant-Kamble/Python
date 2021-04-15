def main():
    my_list = []
    no = int(input("Number of Elements: "))
    print("Enter Elements: ")
    for i in range(0, no):
        ele = int(input())
        my_list.append(ele)
    print(my_list)

    print("Minimum number is: ", min(my_list))


if __name__ == '__main__':
    main()
