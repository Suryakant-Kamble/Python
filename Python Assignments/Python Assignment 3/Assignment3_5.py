from MarvellousNum import chkprime


def ListPrime():
    no = int(input("Enter Number of elements: "))
    arr = []
    e = 0
    crr = []
    print("Enter elements: ")
    for i in range(0, no):
        ele = int(input())
        arr.append(ele)
    print("List is: ", arr)
    for a in range(len(arr)):
        ret = chkprime(arr[a])
        if ret:
            crr.append(arr[a])
    print("List of prime no : ", crr)
    for b in range(len(crr)):
        d = int(crr[b])
        e = e + d
    print("total = ", e)


if __name__ == '__main__':
    ListPrime()
