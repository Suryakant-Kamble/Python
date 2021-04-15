def factorial(no):
    if no == 1:
        return no
    else:
        return no * factorial(no - 1)

"""
# Factorial using for loop Without Recursive
ans = 1
for i in range(1, no+1):
    ans = ans * i
print(ans)
"""


def main():
    no = int(input("Enter number : "))
    # ret = no+1
    print(factorial(no))


if __name__ == '__main__':
    main()
