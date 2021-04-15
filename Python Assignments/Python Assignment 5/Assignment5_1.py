def dispstar(no1):
    ans = 0
    if no1 > 0:
        print(" * ", end=" ")
        ans = no1-1
        dispstar(ans)


def main():
    no = int(input("Enter Number : "))
    dispstar(no)


if __name__ == "__main__":
    main()
