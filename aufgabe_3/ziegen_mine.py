import random


class Door:
    car = False
    chosen = False

    def __init__(self, id):
        self.id = id


class MontyHall:
    doors = []

    def __init__(self, num_doors):
        self.numDoors = num_doors
        self.doors = []

        for i in range(1, num_doors + 1):
            self.doors.append(Door(str(i)))

        random.choice(self.doors).car = True

    def choose(self, id):
        for i in self.doors:
            if i.id == id:
                i.chosen = True

    def choose_random(self):
        random.choice(self.doors).chosen = True

    def open_empty_doors(self):
        openedDoors = set()
        for door in self.doors:
            if not door.chosen and not door.car:
                openedDoors.add(door.id)
        if len(openedDoors) != len(self.doors) - 2:
            openedDoors.remove(str(random.sample(openedDoors, 1)[0]))

        return openedDoors

    def open_door(self, swap):
        if not swap:
            for door in self.doors:
                if door.chosen:
                    if door.car:
                        return True
                    else:
                        return False
        if swap:
            for door in self.doors:
                if door.chosen:
                    if door.car:
                        return False
                    else:
                        return True


def play(num_doors=3):
    car_emoji = u'\U0001F697'
    goat_emoji = u'\U0001F410'
    door_emoji = u'\U0001F6AA'
    arrow_emoji = u"\U000027A1"
    if int(num_doors) < 3:
        num_doors = "3"
        print " --- Minimum 3 doors! --- "
    chosen_door = raw_input("Which door to choose (1-" + num_doors + "): ")
    if int(chosen_door) <= int(num_doors):
        doors = MontyHall(int(num_doors))
        doors.choose(str(chosen_door))
        for i in doors.open_empty_doors():
            print "Host opens door " + i + " " + door_emoji + " " + arrow_emoji + " " + goat_emoji
        swap_or_keep = raw_input("Swap (s) or keep (k): ")

        if swap_or_keep == "s":
            if doors.open_door(True):
                print "\n" + door_emoji + " " + arrow_emoji + " " + car_emoji + "\nCar! "
            else:
                print "\n" + door_emoji + " " + arrow_emoji + " " + goat_emoji + "\nGoat! "
        elif swap_or_keep == "k":
            if doors.open_door(False):
                print "\n" + door_emoji + " " + arrow_emoji + " " + car_emoji + "\nCar! "
            else:
                print "\n" + door_emoji + " " + arrow_emoji + " " + goat_emoji + "\nGoat! "
        else:
            print " --- Not valid input! --- "
    else:
        print " --- Door ID not in possibilities! --- "


def simulate(num_doors=3, num_games=10000, strategy=True):
    won = 0
    for i in range(num_games):
        game = MontyHall(num_doors)
        game.choose_random()
        game.open_empty_doors()
        if game.open_door(strategy):
                won += 1

    return float(float(won) / float(num_games))


# play(raw_input("Enter number of Doors: "))
print simulate(3, 100, True)
print simulate(3, 100, False)
