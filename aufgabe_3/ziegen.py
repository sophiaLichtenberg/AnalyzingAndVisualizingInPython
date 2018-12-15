import random


class Door:
    car = False
    chosen = False

    def __init__(self, id):
        self.id = id


class MontyHall:
    doors = []

    def __init__(self, numberDoors):
        self.numberDoors = numberDoors
        self.doors = []

        for i in range(1, int(numberDoors) + 1):
            self.doors.append(Door(str(i)))

        random.choice(self.doors).car = True

    def choose(self, id):
        for door in self.doors:
            if door.id == str(id):
                door.chosen = True

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


def play(number_doors=3):
    car_emoji = u'\U0001F697'
    goat_emoji = u'\U0001F410'
    door_emoji = u'\U0001F6AA'
    arrow_emoji = u"\U000027A1"

    if int(number_doors) < 3:
        number_doors = "3"
        print " --- Minimum 3 doors! --- "

    chosen_door = raw_input("Which door to choose (1-" + number_doors + "): ")

    if 0 < int(chosen_door) <= int(number_doors):
        game = MontyHall(number_doors)
        game.choose(str(chosen_door))
        for id in game.open_empty_doors():
            print "Host opens door " + id + " " + door_emoji + " " + arrow_emoji + " " + goat_emoji
        swap = raw_input("Swap (s) or keep (k): ")
        if swap == "s":
            if game.open_door(True):
                print "\n" + door_emoji + " " + arrow_emoji + " " + car_emoji + "\nCar! "
            else:
                print "\n" + door_emoji + " " + arrow_emoji + " " + goat_emoji + "\nGoat! "
        elif swap == "k":
            if game.open_door(False):
                print "\n" + door_emoji + " " + arrow_emoji + " " + car_emoji + "\nCar! "
            else:
                print "\n" + door_emoji + " " + arrow_emoji + " " + goat_emoji + "\nGoat! "
        else:
            print " --- Invalid input --- "
    else:
        print " --- Door ID not in possibilities! --- "
        play(number_doors)


def simulate(number_doors=3, number_games=10000, swap=True):
    counter = 0
    for i in range(1, number_games + 1):
        game = MontyHall(number_doors)
        game.choose_random()
        if swap:
            if game.open_door(True):
                counter += 1
        else:
            if game.open_door(False):
                counter += 1

    return float(float(counter) / float(number_games))


print simulate()
# play(raw_input("Please enter the number of doors(min. 3): "))
