def chkDiv():

    no = float(input("Enter number =  "))
    if no % 5 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(chkDiv())
