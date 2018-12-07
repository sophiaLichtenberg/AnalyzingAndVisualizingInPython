BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]
DARK_GREEN = [0, 100, 0]
BROWN = [160, 82, 45]


def checkNeighbours(ant_array):
    neighbourCounter = 0
    antNeighbours = []
    neighbour_row = 0
    neighbour_col = 0
    for row in range(len(ant_array)):
        for col in range(len(ant_array[row])):
            if row + 1 < len(ant_array) and col + 1 < len(ant_array[row]):
                if ant_array[row + 1][col] != WHITE:
                    neighbourCounter += 1
                    neighbour_row = row + 1
                    neighbour_col = col
                if ant_array[row + 1][col + 1] != WHITE:
                    neighbourCounter += 1
                    neighbour_row = row + 1
                    neighbour_col = col + 1
                if ant_array[row][col + 1] != WHITE:
                    neighbourCounter += 1
                    neighbour_row = row
                    neighbour_col = col + 1
                if row - 1 >= 0 or col - 1 >= 0:
                    if ant_array[row + 1][col - 1] != WHITE:
                        neighbourCounter += 1
                        neighbour_row = row + 1
                        neighbour_col = col - 1
                    if ant_array[row - 1][col + 1] != WHITE:
                        neighbourCounter += 1
                        neighbour_row = row - 1
                        neighbour_col = col + 1
            if row - 1 >= 0 or col - 1 >= 0:
                if ant_array[row - 1][col - 1] != WHITE:
                    neighbourCounter += 1
                    neighbour_row = row - 1
                    neighbour_col = col - 1
                if ant_array[row - 1][col] != WHITE:
                    neighbourCounter += 1
                    neighbour_row = row - 1
                    neighbour_col = col
                if ant_array[row][col - 1] != WHITE:
                    neighbourCounter += 1
                    neighbour_row = row
                    neighbour_col = col - 1
            if neighbourCounter > 0:
                antNeighbours.append([row, col, neighbourCounter, neighbour_row, neighbour_col])
            neighbour_row = 0
            neighbour_col = 0
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

        # Schwimmer 3
        ant_array[20][0] = YELLOW
        ant_array[20][1] = YELLOW
        ant_array[20][2] = YELLOW
        ant_array[21][2] = YELLOW
        ant_array[21][3] = YELLOW
        ant_array[22][0] = YELLOW
        ant_array[22][1] = YELLOW
        ant_array[22][2] = YELLOW

        # Schwimmer 4
        ant_array[19][7] = YELLOW
        ant_array[20][6] = YELLOW
        ant_array[20][7] = YELLOW
        ant_array[20][8] = YELLOW
        ant_array[20][9] = YELLOW
        ant_array[21][8] = YELLOW
        ant_array[21][9] = YELLOW
        ant_array[22][6] = YELLOW
        ant_array[22][7] = YELLOW
        ant_array[22][8] = YELLOW
        ant_array[22][9] = YELLOW
        ant_array[23][7] = YELLOW

        # Schwimmer 5
        ant_array[30][0] = BLUE
        ant_array[30][1] = BLUE
        ant_array[30][2] = BLUE
        ant_array[31][2] = BLUE
        ant_array[31][3] = BLUE
        ant_array[32][0] = BLUE
        ant_array[32][1] = BLUE
        ant_array[32][2] = BLUE

        # Schwimmer 6
        ant_array[29][7] = BLUE
        ant_array[30][6] = BLUE
        ant_array[30][7] = BLUE
        ant_array[30][8] = BLUE
        ant_array[30][9] = BLUE
        ant_array[31][8] = BLUE
        ant_array[31][9] = BLUE
        ant_array[32][6] = BLUE
        ant_array[32][7] = BLUE
        ant_array[32][8] = BLUE
        ant_array[32][9] = BLUE
        ant_array[33][7] = BLUE

        # Schwimmer 7
        ant_array[40][0] = GREEN
        ant_array[40][1] = GREEN
        ant_array[40][2] = GREEN
        ant_array[41][2] = GREEN
        ant_array[41][3] = GREEN
        ant_array[42][0] = GREEN
        ant_array[42][1] = GREEN
        ant_array[42][2] = GREEN

        # Schwimmer 8
        ant_array[39][7] = GREEN
        ant_array[40][6] = GREEN
        ant_array[40][7] = GREEN
        ant_array[40][8] = GREEN
        ant_array[40][9] = GREEN
        ant_array[41][8] = GREEN
        ant_array[41][9] = GREEN
        ant_array[42][6] = GREEN
        ant_array[42][7] = GREEN
        ant_array[42][8] = GREEN
        ant_array[42][9] = GREEN
        ant_array[43][7] = GREEN

    for i in checkNeighbours(ant_array):
        if ant_array[i[0]][i[1]] == WHITE:
            if i[2] == 3:
                if ant_array[i[3]][i[4]] == RED:
                    ant_array[i[0]][i[1]] = RED
                elif ant_array[i[3]][i[4]] == BLUE:
                    ant_array[i[0]][i[1]] = BLUE
                elif ant_array[i[3]][i[4]] == GREEN:
                    ant_array[i[0]][i[1]] = GREEN
                elif ant_array[i[3]][i[4]] == YELLOW:
                    ant_array[i[0]][i[1]] = YELLOW
                else:
                    ant_array[i[0]][i[1]] = BLACK
        else:
            if i[2] != 3 and i[2] != 5:
                ant_array[i[0]][i[1]] = WHITE
    return ant_array


# 24/3 Welt, sh. Wikipedia
def special_ants2(ant_array):
    if checkIfEmpty(ant_array):
        #Object 1
        ant_array[20][21] = RED
        ant_array[21][20] = RED
        ant_array[21][21] = RED
        ant_array[21][22] = RED
        ant_array[22][21] = RED

        #Object 2
        ant_array[40][40] = RED
        ant_array[40][41] = RED
        ant_array[41][40] = RED
        ant_array[41][41] = RED
        ant_array[42][41] = RED

        # Object 3
        ant_array[30][61] = RED
        ant_array[31][60] = RED
        ant_array[31][61] = RED
        ant_array[32][61] = RED
        ant_array[32][62] = RED


    for i in checkNeighbours(ant_array):
        if ant_array[i[0]][i[1]] == WHITE:
            if i[2] == 3:
                ant_array[i[0]][i[1]] = RED
        else:
            if i[2] != 2 or i[2] != 4:
                ant_array[i[0]][i[1]] = WHITE
            if i[2] == 4:
                ant_array[i[0]][i[1]] = RED
            if i[2] == 2:
                ant_array[i[0]][i[1]] = RED
    return ant_array


# Qualle, sh. Wikipedia
def special_ants3(ant_array):
    if checkIfEmpty(ant_array):
        ant_array[20][20] = BLUE
        ant_array[21][20] = BLUE
        ant_array[21][21] = BLUE
        ant_array[22][20] = BLUE
        ant_array[22][21] = BLUE
        ant_array[22][22] = BLUE

        ant_array[40][40] = BLUE
        ant_array[41][40] = BLUE
        ant_array[41][41] = BLUE
        ant_array[42][40] = BLUE
        ant_array[42][41] = BLUE
        ant_array[42][42] = BLUE


    for i in checkNeighbours(ant_array):
        if ant_array[i[0]][i[1]] == WHITE:
            if i[2] == 3:
                ant_array[i[0]][i[1]] = BLUE
        else:
            if i[2] != 2 or i[2] != 4 or i[2] != 5:
                ant_array[i[0]][i[1]] = WHITE
            if i[2] == 2:
                ant_array[i[0]][i[1]] = BLUE
            if i[2] == 4:
                ant_array[i[0]][i[1]] = BLUE
            if i[2] == 5:
                ant_array[i[0]][i[1]] = BLUE
    return ant_array
