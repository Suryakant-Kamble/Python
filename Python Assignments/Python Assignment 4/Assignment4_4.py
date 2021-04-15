import functools


def chk_even(no1):
    if no1 % 2 == 0:
        return True
    else:
        return False


def square(no2):
    return no2 ** 2


def add(no3, no4):
    return no3 + no4


def main():
    no = int(input("Enter number of elements : "))
    arr = []
    brr = []
    crr = []
    ans = 0
    for i in range(0, no):
        ret = int(input("Enter the elements in List = "))
        arr.append(ret)
        brr = list(filter(chk_even, arr))
        crr = list(map(square, brr))
        if crr:
            ans = functools.reduce(add, crr)
    print("Input List is = ", arr)
    print("List after filter = ", brr)
    print("List after map ", crr)
    print("Output of reduce = ", ans)


if __name__ == '__main__':
    main()
