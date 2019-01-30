import turtle as t
import os
import time

wn = t.Screen()
wn.bgcolor("black")
wn.setup(640, 480)

counter = 0

wall_shape = os.path.join(os.getcwd(), "wall.gif")
fruit_shape = os.path.join(os.getcwd(), "cherry.gif")
player_shape = os.path.join(os.getcwd(), "pacman_right.gif")
monster_shape = os.path.join(os.getcwd(), "monster.gif")
door_shape = os.path.join(os.getcwd(), "door.gif")
monster_shape = os.path.join(os.getcwd(), "monster.gif")
wn.register_shape(wall_shape)
wn.register_shape(fruit_shape)
wn.register_shape(player_shape)
wn.register_shape(door_shape)
wn.register_shape(monster_shape)

width = 32


# Die Mauern des Labyrinths
class Sprite(t.Turtle):

    def __init__(self, shape):
        t.Turtle.__init__(self)
        self.shape(shape)
        self.penup()
        self.speed(0)

    def move(self, go_left=True, go_right=False):
        # print str(self.xcor()) + " " + str(self.ycor())
        for wall in walls:
            if wall[1] == self.ycor():
                if go_right:
                    if self.xcor() + width <= wall[0]:
                        self.goto(self.xcor() + 1, self.ycor())
                    else:
                        go_left = True
                        go_right = False

                if go_left:
                    if self.xcor() >= wall[0] + width:
                        self.goto(self.xcor() - 1, self.ycor())


class Player(Sprite):
    global counter

    def __init__(self, shape):
        Sprite.__init__(self, shape)

    def changeShape(self, res):
        wn.register_shape(os.path.join(os.getcwd(), res))
        self.shape(os.path.join(os.getcwd(), res))

    def getCounter(self):
        return  self.counter

    def go_left(self):
        res = "pacman_left.gif"
        self.changeShape(res)

        go_to_x = self.xcor() - width
        go_to_y = self.ycor()

        # hit the wall
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        if (go_to_x, go_to_y) == (monster.xcor(), monster.ycor()):
            keepGoing = False
            print "Monster"

        # Hit the door
        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            t.undo()
            t.penup()
            t.hideturtle()
            t.color("white")
            t.setposition(width / 2, 0)
            t.write("Next Level ", move=False, align="center", font=("Arial", 20, "normal"))
            wn.tracer(0)
            time.sleep(2)
            wn.clear()
            wn.bgcolor("black")
            del walls[:]
            del fruits[:]
            setup_maze(levels[1])

        # hit a cherry
        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                fruit[0].goto(-1000, 1000)
                fruit[0].clear()
                self.goto(go_to_x, go_to_y)
                print "Cherry"
                fruits.remove(fruit)
                print fruits
                self.counter += 1
                t.undo()
                t.penup()
                t.hideturtle()
                t.color("white")
                t.setposition(-260, 207)
                t.write("Score " + str(self.counter), move=False, align="center", font=("Arial", 20, "normal"))

    def go_right(self):
        res = "pacman_right.gif"
        self.changeShape(res)

        go_to_x = self.xcor() + width
        go_to_y = self.ycor()
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            t.undo()
            t.penup()
            t.hideturtle()
            t.color("white")
            t.setposition(-260, 207)
            t.write("Score " + str(self.counter), move=False, align="center", font=("Arial", 20, "normal"))
            wn.tracer(0)
            time.sleep(2)
            wn.clear()
            wn.bgcolor("black")
            del walls[:]
            del fruits[:]
            setup_maze(levels[1])

        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                fruit[0].goto(-1000, 1000)
                fruit[0].clear()
                self.goto(go_to_x, go_to_y)
                print "Cherry"
                fruits.remove(fruit)
                print fruits
                self.counter += 1
                t.undo()
                t.penup()
                t.hideturtle()
                t.color("white")
                t.setposition(-260, 207)
                t.write("Score " + str(self.counter), move=False, align="center", font=("Arial", 20, "normal"))

    def go_up(self):
        res = "pacman_up.gif"
        self.changeShape(res)
        go_to_x = self.xcor()
        go_to_y = self.ycor() + width
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            t.undo()
            t.penup()
            t.hideturtle()
            t.color("white")
            t.setposition(width / 2, 0)
            t.write("Next Level ", move=False, align="center", font=("Arial", 20, "normal"))
            wn.tracer(0)
            time.sleep(2)
            wn.clear()
            wn.bgcolor("black")
            del walls[:]
            del fruits[:]
            setup_maze(levels[1])

        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                fruit[0].goto(-1000, 1000)
                fruit[0].clear()
                self.goto(go_to_x, go_to_y)
                print "Cherry"
                fruits.remove(fruit)
                print fruits
                self.counter += 1
                t.undo()
                t.penup()
                t.hideturtle()
                t.color("white")
                t.setposition(-260, 207)
                t.write("Score " + str(self.counter), move=False, align="center", font=("Arial", 20, "normal"))

    def go_down(self):
        res = "pacman_down.gif"
        self.changeShape(res)
        go_to_x = self.xcor()
        go_to_y = self.ycor() - width
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        # hit the door
        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            t.undo()
            t.penup()
            t.hideturtle()
            t.color("white")
            t.setposition(width / 2, 0)
            t.write("Next Level ", move=False, align="center", font=("Arial", 20, "normal"))
            wn.tracer(0)
            time.sleep(2)
            wn.clear()
            wn.bgcolor("black")
            del walls[:]
            del fruits[:]
            print str(self.getCounter())
            setup_maze(levels[1])

        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                fruit[0].goto(-1000, 1000)
                fruit[0].clear()
                self.goto(go_to_x, go_to_y)
                print "Cherry"
                fruits.remove(fruit)
                print fruits
                self.counter += 1
                t.undo()
                t.penup()
                t.hideturtle()
                t.color("white")
                t.setposition(-260, 207)
                t.write("Score " + str(self.counter), move=False, align="center", font=("Arial", 20, "normal"))

class Monster(Sprite):

    def __init__(self, shape):
        Sprite.__init__(self, shape)

    def move(self):
        self.forward(1)




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
    "#           m # f d#",
    "#  #################",
    "#         m        #",
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
    "#        m     #   #",
    "#   ########   #   #",
    "#   #  d# f#   #   #",
    "#   #          #   #",
    "#   ############   #",
    "#         m        #",
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
                rogue = Player(player_shape)
                rogue.goto(screen_x, screen_y)

                # Auf Tastaturereignisse lauschen
                t.listen()
                t.onkey(rogue.go_left, "Left")
                t.onkey(rogue.go_right,"Right")
                t.onkey(rogue.go_up, "Up")
                t.onkey(rogue.go_down, "Down")
                t.onkey(exitGame, "Escape")  # Escape beendet das Spiel
            if sprite == "f":
                fruit = Sprite(fruit_shape)
                fruit.goto(screen_x, screen_y)
                fruits.append([fruit, (screen_x, screen_y)])
                fruit.stamp()
            if sprite == "d":
                door.goto(screen_x, screen_y)
                door.stamp()
            if sprite == "m":
                monster.goto(screen_x, screen_y)


def exitGame():
    global keepGoing
    keepGoing = False


walls = []
fruits = []
wall = Sprite(wall_shape)
door = Sprite(door_shape)
monster = Sprite(monster_shape)

wn.tracer(0)

# bisherigen Highscore auslesen
with open("highscore.txt") as highscoreContainer:
    highscore = highscoreContainer.read().decode("utf-8")
print "highscore "+highscore

setup_maze(levels[0])

keepGoing = True
while keepGoing:
    wn.update()
    monster.move()
