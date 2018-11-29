BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
DARK_GREEN = [0, 100, 0]
BROWN = [160, 82, 45]

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
        ant_array[10][0] = RED
        ant_array[10][1] = RED
        ant_array[10][2] = RED
        ant_array[11][2] = RED
        ant_array[11][3] = RED
        ant_array[12][0] = RED
        ant_array[12][1] = RED
        ant_array[12][2] = RED

        # Schwimmer 2
        ant_array[9][7] = RED
        ant_array[10][6] = RED
        ant_array[10][7] = RED
        ant_array[10][8] = RED
        ant_array[10][9] = RED
        ant_array[11][8] = RED
        ant_array[11][9] = RED
        ant_array[12][6] = RED
        ant_array[12][7] = RED
        ant_array[12][8] = RED
        ant_array[12][9] = RED
        ant_array[13][7] = RED

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

        # Schwimmer 1
        ant_array[30][0] = RED
        ant_array[30][1] = RED
        ant_array[30][2] = RED
        ant_array[31][2] = RED
        ant_array[31][3] = RED
        ant_array[32][0] = RED
        ant_array[32][1] = RED
        ant_array[32][2] = RED

        # Schwimmer 2
        ant_array[29][7] = RED
        ant_array[30][6] = RED
        ant_array[30][7] = RED
        ant_array[30][8] = RED
        ant_array[30][9] = RED
        ant_array[31][8] = RED
        ant_array[31][9] = RED
        ant_array[32][6] = RED
        ant_array[32][7] = RED
        ant_array[32][8] = RED
        ant_array[32][9] = RED
        ant_array[33][7] = RED

        # Schwimmer 1
        ant_array[40][0] = RED
        ant_array[40][1] = RED
        ant_array[40][2] = RED
        ant_array[41][2] = RED
        ant_array[41][3] = RED
        ant_array[42][0] = RED
        ant_array[42][1] = RED
        ant_array[42][2] = RED

        # Schwimmer 2
        ant_array[39][7] = RED
        ant_array[40][6] = RED
        ant_array[40][7] = RED
        ant_array[40][8] = RED
        ant_array[40][9] = RED
        ant_array[41][8] = RED
        ant_array[41][9] = RED
        ant_array[42][6] = RED
        ant_array[42][7] = RED
        ant_array[42][8] = RED
        ant_array[42][9] = RED
        ant_array[43][7] = RED

    for i in checkNeighbours(ant_array):
        if ant_array[i[0]][i[1]] == WHITE:
            if i[2] == 3:
                ant_array[i[0]][i[1]] = RED
        else:
            if i[2] != 3 and i[2] != 5:
                ant_array[i[0]][i[1]] = WHITE
    return ant_array


def christmas_tree(ant_array):
    if checkIfEmpty(ant_array):
        middle = len(ant_array[0])/2
        i = 0
        while i < len(ant_array) - len(ant_array) / 3:
            ant_array[i][middle - i] = DARK_GREEN
            ant_array[i][middle + i] = DARK_GREEN
            i += 1
        j = middle - i + 1
        while j < middle + i:
            ant_array[len(ant_array) * 2 / 3][j] = DARK_GREEN
            j += 1
        k = len(ant_array) * 2 / 3 + 1
        while k < len(ant_array):
            ant_array[k][len(ant_array[0])*3/7] = BROWN
            ant_array[k][len(ant_array[0])*4/7] = BROWN
            k += 1

    #    if checkIfEmpty(ant_array):
    #        middle = len(ant_array[0])
    #        i = 0
    #        while i < len(ant_array):
    #            ant_array[i][middle / 2] = GREEN
    #            i += 1
    #
    #    for i in checkNeighbours(ant_array):
    #       if ant_array[i[0]][i[1]] == WHITE:
    #            if i[2] == 3:
    #                ant_array[i[0]][i[1]] = RED
    #        else:
    #            if i[2] != 3 and i[2] != 5:
    #                ant_array[i[0]][i[1]] = WHITE
    return ant_array
