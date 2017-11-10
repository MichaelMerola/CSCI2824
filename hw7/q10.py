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

def goldbachCheck(N):

    #check if a j in a range is prime, then if N - j (i) is primer. i + j = N
    for p in range(2, N):
        if (isPrime(p)):
            q = N - p
            if (isPrime(q)):
                return (p, q)
    return 0

def main():

    print(goldbachCheck(12))


if __name__ == '__main__':
    main()
