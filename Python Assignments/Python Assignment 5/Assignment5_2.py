def dispnumb(no1):
    if no1 > 0:
        ans = no1-1
        dispnumb(ans)
        print(no1, end=" ")


def main():
    no = int(input("Enter Number : "))
    dispnumb(no)


if __name__ == "__main__":
    main()
