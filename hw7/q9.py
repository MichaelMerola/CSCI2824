import math

def sieve_of_E_sum(N):

    primeArray = []
    numPrimes = 0
    sumPrimes = 0

    for i in range(0, N):
        primeArray.append(True)

    for p in range(2, maq10th.ceil(math.sqrt(N))):
        if (primeArray[p] == True):
            m = p + p
            while (m <= N):
                primeArray[m] = False # "remove" the multiples of the prime number
                m = m + p
    for x in primeArray:
        if (x == True):
            numPrimes = numPrimes + 1
            sumPrimes = sumPrimes + x

    return (numPrimes, sumPrimes)

def main():

    print(sieve_of_E_sum(10))


if __name__ == '__main__':
    main()
