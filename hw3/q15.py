def check_proposition(set1):


    for x in set1:
        yCount = 0
        if (x % 2 == 0):
            for y in set1:
                if (x == (2*y)):
                    yCount += 1
            if (yCount == 0):
                return False
    return True


def main():

    set1 = [-2,-1,0,1,3,4]

    print(check_proposition(set1))


if __name__ == '__main__':
    main()
