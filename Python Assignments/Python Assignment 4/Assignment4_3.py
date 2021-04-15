import functools


def chk_num(no1):
    if no1 >= 70:
        if no1 <= 90:
            return no1


def add(no2):
    return 10 + no2


def multi(no3, no4):
    return no3 * no4


def main():
    no = int(input("Enter number of elements : "))
    arr = []
    brr = []
    crr = []
    ans = 0
    for i in range(0, no):
        ret = int(input("Enter the elements in List = "))
        arr.append(ret)
        brr = list(filter(chk_num, arr))
        crr = list(map(add, brr))
        if crr:
            ans = functools.reduce(multi, crr)
    print("Input List is = ", arr)
    print("List after filter = ", brr)
    print("List after map ", crr)
    print("Output of reduce = ", ans)


if __name__ == '__main__':
    main()
