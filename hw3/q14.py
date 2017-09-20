def tarski(shapes, colors):

    for x in range(len(colors)):
        for y in range(len(colors[x])):
            if (colors[x][y] == 'gray'):
                if (shapes[x][y] != 'circle'):
                    return False

    return True

def main():

    shapes = [['circle'  , 'circle', 'circle'],
            ['triangle', 'circle', 'square'],
            ['triangle', 'square', 'circle']]
    colors = [['blue', 'red' , 'gray'],
              ['red' , 'gray', 'blue'],
              ['blue', 'red' , 'blue']]

    print(tarski(shapes, colors))


if __name__ == '__main__':
    main()
