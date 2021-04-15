def summation(no1):
    #  using recursive
    ans = 0
    a = 0
    for i in range(len(no1)):
        ans = ans + int(no1[i])

        if len(no1) - 1 < 0:
            summation(no1)

    print("summation of digits: ", ans)

    """
    
    #using: for loop without recursive 
    ans=0
    for i in range(len(no1)):
        ans = ans + int(no1[i])

    print("summation of digits: ", ans)"""


def main():
    no = list(input("Enter Number : "))
    summation(no)


if __name__ == "__main__":
    main()
