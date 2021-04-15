import functools


def chk_prime(no1):
    z = 0
    for i in range(2, no1//2+1):
        if no1 % i == 0:
            z = z+1
    if z <= 0:
        return True
    else:
        return False


def multi(no2):
    return 2 * no2


#def max_num(no3,no4):

def main():
    no = int(input("Enter number of elements : "))
    arr = []
    brr = []
    crr = []
    ans = 0
    for i in range(0, no):
        ret = int(input("Enter the elements in List = "))
        arr.append(ret)
        if arr:
            brr = list(filter(chk_prime, arr))
        crr = list(map(multi, brr))
        if crr:
            ans = functools.reduce(lambda a, b: a if a > b else b, crr)
            #ans = functools.reduce(max_num, crr)
    print("Input List is = ", arr)
    print("List after filter = ", brr)
    print("List after map ", crr)
    print("Output of reduce = ", ans)


if __name__ == '__main__':
    main()
