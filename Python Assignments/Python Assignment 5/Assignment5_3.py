def dispnum(no1):
    ans = 0
    if no1 > 0:
        print(no1, end=" ")
        ans = no1-1
        dispnum(ans)


def main():
    no = int(input("Enter Number : "))
    dispnum(no)


if __name__ == "__main__":
    main()
