
def BinToDec(binary_in):
    # initialize
    decimal_out = 0
    # add up the binary expression of the decimal number
    for position in range(0, len(binary_in)): #range(0, 4) not including 4
        decimal_out = decimal_out + binary_in[len(binary_in)-position-1] * (2**position)

    return (decimal_out)

def main():

    binNum = [0, 1, 0, 0, 1, 1, 0, 1]

    print BinToDec(binNum)


if __name__ == '__main__':
    main()
