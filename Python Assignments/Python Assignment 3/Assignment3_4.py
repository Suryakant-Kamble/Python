def main():
    no = int(input("Enter Number of elements: "))
    arr = []
    print("Enter elements: ")
    for i in range(0, no):
        ele = int(input())
        arr.append(ele)
    print(arr)
    a = int(input(" Element to search : "))
    brr = []
    for b in range(len(arr)):
        ret = arr[b]
        if ret == a:
            brr.append(ret)

    print(brr)

    print("Frequency of that number from list : ",len(brr))


if __name__ == '__main__':
    main()
