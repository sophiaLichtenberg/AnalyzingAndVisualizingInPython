BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]


def checkNeighbours(ant_array):
    neighbourCounter = 0
    antNeighbours =[]
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
                if ant_array[row -1][col - 1] != WHITE:
                        neighbourCounter += 1
                if ant_array[row - 1][col] != WHITE:
                        neighbourCounter += 1
                if ant_array[row][col-1] != WHITE:
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
    # Ersetzen Sie bitte die foldenden Zeilen durch Ihre Loesung von Aufgabenteil a)

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
