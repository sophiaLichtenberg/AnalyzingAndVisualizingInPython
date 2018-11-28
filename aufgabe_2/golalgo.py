BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]


def checkNeighbours(ant_array):
    neighbourCounter = 0
    antNeighbours = []
    for row in range(len(ant_array)):
        for col in range(len(ant_array[row])):
            if row + 1 < len(ant_array) and col + 1 < len(ant_array[row]):
                if ant_array[row + 1][col] != WHITE:
                    neighbourCounter += 1
                if ant_array[row + 1][col + 1] != WHITE:
                    neighbourCounter += 1
                if ant_array[row][col + 1] != WHITE:
                    neighbourCounter += 1
                if row - 1 >= 0 or col - 1 >= 0:
                    if ant_array[row + 1][col - 1] != WHITE:
                        neighbourCounter += 1
                    if ant_array[row - 1][col + 1] != WHITE:
                        neighbourCounter += 1
            if row - 1 >= 0 or col - 1 >= 0:
                if ant_array[row - 1][col - 1] != WHITE:
                    neighbourCounter += 1
                if ant_array[row - 1][col] != WHITE:
                    neighbourCounter += 1
                if ant_array[row][col - 1] != WHITE:
                    neighbourCounter += 1
            if neighbourCounter > 0:
                antNeighbours.append([row, col, neighbourCounter])
            neighbourCounter = 0
    return antNeighbours


def checkIfEmpty(ant_array):
    for row in range(len(ant_array)):
        for col in range(len(ant_array[row])):
            if ant_array[row][col] != WHITE:
                return False

    return True


def simple_gol(ant_array):
    if checkIfEmpty(ant_array):
        ant_array[20][21] = BLACK
        ant_array[21][20] = BLACK
        ant_array[21][21] = BLACK
        ant_array[21][22] = BLACK
        ant_array[22][20] = BLACK
        ant_array[22][22] = BLACK
        ant_array[23][21] = BLACK

    for i in checkNeighbours(ant_array):
        if ant_array[i[0]][i[1]] == WHITE:
            if i[2] == 3:
                ant_array[i[0]][i[1]] = BLACK
        else:
            if i[2] < 2 or i[2] > 3:
                ant_array[i[0]][i[1]] = WHITE
    return ant_array


def multicolor_ants(ant_array):
    if checkIfEmpty(ant_array):
        ant_array[20][21] = RED
        ant_array[21][20] = RED
        ant_array[21][21] = RED
        ant_array[21][22] = RED
        ant_array[22][20] = RED
        ant_array[22][22] = RED
        ant_array[23][21] = RED

    for i in checkNeighbours(ant_array):
        if ant_array[i[0]][i[1]] == WHITE:
            if i[2] == 2:
                ant_array[i[0]][i[1]] = GREEN
            if i[2] == 3:
                ant_array[i[0]][i[1]] = BLUE
        else:
            if i[2] < 1 or i[2] > 4:
                ant_array[i[0]][i[1]] = WHITE
    return ant_array


def special_ants(ant_array):
    if checkIfEmpty(ant_array):
        # Schwimmer 1
        ant_array[20][0] = RED
        ant_array[20][1] = RED
        ant_array[20][2] = RED
        ant_array[21][2] = RED
        ant_array[21][3] = RED
        ant_array[22][0] = RED
        ant_array[22][1] = RED
        ant_array[22][2] = RED

        # Schwimmer 2
        ant_array[19][7] = RED
        ant_array[20][6] = RED
        ant_array[20][7] = RED
        ant_array[20][8] = RED
        ant_array[20][9] = RED
        ant_array[21][8] = RED
        ant_array[21][9] = RED
        ant_array[22][6] = RED
        ant_array[22][7] = RED
        ant_array[22][8] = RED
        ant_array[22][9] = RED
        ant_array[23][7] = RED



    for i in checkNeighbours(ant_array):
        if ant_array[i[0]][i[1]] == WHITE:
            if i[2] == 3:
                ant_array[i[0]][i[1]] = RED
        else:
            if i[2] != 3 and i[2] != 5:
                ant_array[i[0]][i[1]] = WHITE
    return ant_array