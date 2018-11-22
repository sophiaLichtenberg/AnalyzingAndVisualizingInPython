def simple_gol(ant_array):
    # Ersetzen Sie bitte die foldenden Zeilen durch Ihre Loesung von Aufgabenteil a)
    ant_array[0][0] = [0, 0, 0]  # Pixel links oben schwarz
    ant_array[0][1] = [0, 0, 255]  # Pixel rechts daneben blau
    ant_array[1][0] = [255, 0, 0]  # Pixel darunter rot
    return ant_array


def multicolor_ants(ant_array):
    # Ersetzen Sie bitte die foldenden Zeilen durch Ihre Loesung von Aufgabenteil b)
    ant_array[0][0] = [0, 0, 0]  # Pixel links oben schwarz
    return ant_array
