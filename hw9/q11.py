import math

def Comb(n, r):
    c = math.factorial(n)/(math.factorial(n-r) * math.factorial(r))
    return c

def binom_product(a, b, n):

    product = 1

    for k in range(0, 25):
        comboX = Comb(n, k)
        aX = a**(n-k)
        bX = b**(k)

        coef = comboX*aX*bX
        product = product * coef

    return product

def main():

    print(round(binom_product(2,-1,3)))


if __name__ == '__main__':
    main()
