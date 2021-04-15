def chkprime(no):
    k = 0
    for i in range(2, no//2 + 1):
        if no % i == 0:
            k = k+1
    if k <= 0:
        return True
    else:
        return False