import turtle as t
import os
import time

wn = t.Screen()
wn.bgcolor("black")
wn.setup(640, 480)

wall_shape = os.path.join(os.getcwd(), "wall.gif")
fruit_shape = os.path.join(os.getcwd(), "cherry.gif")
player_shape = os.path.join(os.getcwd(), "pacman_right.gif")
door_shape = os.path.join(os.getcwd(), "door.gif")
wn.register_shape(wall_shape)
wn.register_shape(fruit_shape)
wn.register_shape(player_shape)
wn.register_shape(door_shape)

width = 32


# Die Mauern des Labyrinths
class Sprite(t.Turtle):

    def __init__(self, shape):
        t.Turtle.__init__(self)
        self.shape(shape)
        self.penup()
        self.speed(0)

    def delete(self):
        self.shape(None)


class Player(Sprite):
    counter = 0

    def __init__(self, shape):
        Sprite.__init__(self, shape)

    def changeShape(self, res):
        wn.register_shape(os.path.join(os.getcwd(), res))
        self.shape(os.path.join(os.getcwd(), res))

    def go_left(self):
        res = "pacman_left.gif"
        self.changeShape(res)

        go_to_x = self.xcor() - width
        go_to_y = self.ycor()

        #hit the wall
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        # Hit the door
        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            t.color("white")
            t.hideturtle()
            t.write("Next Level", move=False, align="center", font=("Arial", 20, "normal"))
            wn.tracer(0)
            time.sleep(2)
            wn.clear()
            wn.bgcolor("black")
            setup_maze(levels[1])

        # hit a cherry
        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                fruit[0].goto(-1000,1000)
                fruit[0].clear()
                self.goto(go_to_x, go_to_y)
                print "Cherry"
                fruits.remove(fruit)
                print fruits
                self.counter += 1

    def go_right(self):
        res = "pacman_right.gif"
        self.changeShape(res)

        go_to_x = self.xcor() + width
        go_to_y = self.ycor()
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            t.color("white")
            t.hideturtle()
            t.write("Next Level", move=False, align="center", font=("Arial", 20, "normal"))
            wn.tracer(0)
            time.sleep(2)
            wn.clear()
            wn.bgcolor("black")
            setup_maze(levels[1])

        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                fruit[0].goto(-1000,1000)
                fruit[0].clear()
                self.goto(go_to_x, go_to_y)
                print "Cherry"
                fruits.remove(fruit)
                print fruits
                self.counter += 1

    def go_up(self):
        res = "pacman_up.gif"
        self.changeShape(res)
        go_to_x = self.xcor()
        go_to_y = self.ycor() + width
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            t.color("white")
            t.hideturtle()
            t.write("Next Level", move=False, align="center", font=("Arial", 20, "normal"))
            wn.tracer(0)
            time.sleep(2)
            wn.clear()
            wn.bgcolor("black")
            setup_maze(levels[1])

        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                fruit[0].goto(-1000,1000)
                fruit[0].clear()
                self.goto(go_to_x, go_to_y)
                print "Cherry"
                fruits.remove(fruit)
                print fruits
                self.counter += 1

    def go_down(self):
        res = "pacman_down.gif"
        self.changeShape(res)
        go_to_x = self.xcor()
        go_to_y = self.ycor() - width
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            t.color("white")
            t.hideturtle()
            t.write("Next Level", move=False, align="center", font=("Arial", 20, "normal"))
            wn.tracer(0)
            time.sleep(2)
            wn.clear()
            wn.bgcolor("black")

            setup_maze(levels[1])

        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                fruit[0].goto(-1000,1000)
                fruit[0].clear()
                self.goto(go_to_x, go_to_y)
                print "Cherry"
                fruits.remove(fruit)
                print fruits
                self.counter += 1


# Liste der Labyrinthe
levels = []

level_1 = [
    "####################",
    "# @#ff             #",
    "#  #######  #####  #",
    "#        #  #f     #",
    "# f      #  #####  #",
    "#######  #  #f     #",
    "#        #  #####  #",
    "#  #######    #    #",
    "#             # f d#",
    "#  #################",
    "#                  #",
    "####  ###########  #",
    "#            #     #",
    "#            #f    #",
    "####################"
]

level_2 = [
    "####################",
    "#ff#ff  #f  #   @  #",
    "#  # #####  #  #####",
    "#  #     #  #      #",
    "#  ####  #  ####   #",
    "#        #  #f     #",
    "#        #     #   #",
    "#  #############   #",
    "#              #   #",
    "#   ########   #   #",
    "#   #  d# f#   #   #",
    "#   #          #   #",
    "#   ############   #",
    "#                  #",
    "####################"
]

levels.append(level_1)
levels.append(level_2)


# Level Setup
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            sprite = level[y][x]
            screen_x = -308 + (x * width)
            screen_y = 224 - (y * width)

            if sprite == "#":
                wall.goto(screen_x, screen_y)
                walls.append((screen_x, screen_y))
                wall.stamp()
            if sprite == "@":
                rogue.goto(screen_x, screen_y)
                print str(screen_x) + " " + str(screen_y)
                #rogue.stamp
            if sprite == "f":
                fruit = Sprite(fruit_shape)
                fruit.goto(screen_x, screen_y)
                fruits.append([fruit, (screen_x, screen_y)])
                fruit.stamp()
            if sprite == "d":
                door.goto(screen_x, screen_y)
                door.stamp()


def exitGame():
    global keepGoing
    keepGoing = False


walls = []
fruits = []
wall = Sprite(wall_shape)
rogue = Player(player_shape)
door = Sprite(door_shape)

# Auf Tastaturereignisse lauschen
t.listen()
t.onkey(rogue.go_left, "Left")
t.onkey(rogue.go_right, "Right")
t.onkey(rogue.go_up, "Up")
t.onkey(rogue.go_down, "Down")
t.onkey(exitGame, "Escape")  # Escape beendet das Spiel

wn.tracer(0)
setup_maze(levels[0])
# print(walls)

keepGoing = True
while keepGoing:
    wn.update()