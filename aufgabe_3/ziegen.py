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
        for i in range(1, numberDoors + 1):
            self.doors.append(Door(str(i)))
        print self.doors
        random.choice(self.doors).car = True
        #self.doors[0].car = True

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

            # openedDoors.remove(random.sample(openedDoors, 1))
            # openedDoors.discard(random.sample(openedDoors, 1))
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
                if door.chosen and door.car:
                    return False
                else:
                    return True

game = MontyHall(3)
game.choose(1)
print game.open_empty_doors()
