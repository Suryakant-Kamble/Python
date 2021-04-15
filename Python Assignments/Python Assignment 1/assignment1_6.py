def chk_number():

    print("Check whether number is Positive or Negative or Zero")
    no = float(input("Enter the Number = "))
    if no > 0:
        print("Positive Number")
    elif no == 0:
        print("Zero")
    else:
        print("Negative Number")


if __name__ == '__main__':
    chk_number()
