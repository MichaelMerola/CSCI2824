import math

def isPrime(c):
    if (c == 2):
        return True
    elif (c < 2 or (c % 2) == 0):
        return False
    else:
        for i in range(3, math.ceil(math.sqrt(c))):
            if ((c % i) == 0):
                return False

    return True

def factorMe(N):

    for p in range(2, math.ceil(math.sqrt(N))):
        if (isPrime(p)):
            if ((N % p) == 0):
                q = math.floor(N / p)
                return (p, q)
    return 0

def main():

    print(goldbachCheck(12))


if __name__ == '__main__':
    main()
