import matplotlib.pyplot as plt

def makemovement(name, origin, pace):
    x = origin[0]
    y = origin[1]
    def movement(direction):
        nonlocal x, y
        if direction == 'N':
            y -= pace
        elif direction == 'S':
            y += pace
        elif direction == 'E':
            x += pace
        elif direction == 'W':
            x -= pace
        else:
            raise directionError
        print("%s's New position: (%d, %d)" % (name, x, y))
        plt.plot(x, y, 'r')
        plt.axis('scaled')
        plt.axis('off')
    return movement

if __name__ == "__main__":
    player_one = makemovement('Sam', (0, 0), 2)
    player_two = makemovement('James', (4, 3), 3)
    player_one('N')
    player_two('W')
    player_one('E')
    player_one('E')
    plt.show()
    
