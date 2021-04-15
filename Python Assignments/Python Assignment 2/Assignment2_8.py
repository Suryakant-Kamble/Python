def num_pattern():
    no = int(input("Input: "))
    for i in range(1, no+3):
        for a in range(1, i-1):
            print(a, end="   ")
        print()


if __name__ == '__main__':
    num_pattern()
