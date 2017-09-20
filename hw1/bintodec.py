
def DecToBin(d):
    # initialize
    binOut = []
    n = d
    # recursive
    while (n >= 1):
        if (n % 2 == 0):
            binOut.append(0)
            n = n/2
        else:
            binOut.append(1)
            n = (n-1)/2

    binOut.reverse()

    return (binOut)

def main():

    dec_in = 10

    print DecToBin(73)


if __name__ == '__main__':
    main()
