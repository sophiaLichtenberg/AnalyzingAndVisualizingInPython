def getMinPrice(requiredSeats, seatPrices):
    result = -1
    found = False
    for row in seatPrices:
        counted_list = []
        sum = 0
        for e in row:
            if e == -1:
                counted_list = []
                sum = 0
            else:
                # Check if there were requiredSeats before
                if len(counted_list) == requiredSeats:
                    sum -= counted_list.pop(0)
                counted_list.append(e)
                sum += e
                if len(counted_list) == requiredSeats:
                    if result > sum or result == -1:
                        result = sum
                        found = True
    return result if found else -1


def solve(input):
    blacks = {}
    whites = {}
    black = True
    black_start = True
    row_size = 0
    # First we count how many of each there are
    for row in input:
        row_size = len(row)
        black = black_start
        for char in row:
            if black:
                blacks[char] = blacks.get(char, 0) + 1
            else:
                whites[char] = whites.get(char, 0) + 1
            black = not black
        black_start = not black_start
    black_max_1 = {}
    black_max_2 = {}
    white_max_1 = {}
    white_max_2 = {}
    # Now we get the maximums
    for key, value in blacks.items():
        if value > black_max_1.get("value", -1):
            black_max_2 = black_max_1
            black_max_1 = {
                "key": key,
                "value": value,
            }
        elif value > black_max_2.get("value", -1):
            black_max_2 = {
                "key": key,
                "value": value,
            }
    for key, value in whites.items():
        if value > white_max_1.get("value", -1):
            white_max_2 = white_max_1
            white_max_1 = {
                "key": key,
                "value": value,
            }
        elif value > white_max_2.get("value", -1):
            white_max_2 = {
                "key": key,
                "value": value,
            }
    total = row_size * row_size

    if white_max_1["key"] != black_max_1["key"]:
        return total - (white_max_1["value"] + black_max_1["value"])
    elif white_max_2.get("value", -1) > black_max_2.get("value", -1):
        return total - (white_max_2["value"] + black_max_1["value"])
    return total - (white_max_1["value"] + black_max_2.get("value", 0))