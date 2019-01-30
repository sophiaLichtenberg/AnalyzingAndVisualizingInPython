import turtle as t
import os
import time

wn = t.Screen()
wn.bgcolor("black")
wn.setup(640, 480)

score = 0
level_counter = 0

wall_shape = os.path.join(os.getcwd(), "wall.gif")
fruit_shape = os.path.join(os.getcwd(), "cherry.gif")
player_shape = os.path.join(os.getcwd(), "pacman_right.gif")
monster_shape = os.path.join(os.getcwd(), "monster.gif")
door_shape = os.path.join(os.getcwd(), "door.gif")
wn.register_shape(wall_shape)
wn.register_shape(fruit_shape)
wn.register_shape(player_shape)
wn.register_shape(door_shape)
wn.register_shape(monster_shape)

width = 32


class Monster(t.Turtle):
    go_left = False
    go_right = True

    def __init__(self, shape):
        t.Turtle.__init__(self)
        self.shape(shape)
        self.penup()
        self.speed(0)

    def move(self):
        for current_wall in walls:
            if current_wall[1] == self.ycor():
                if self.go_right and current_wall[0] > 0:
                    if self.xcor() + width + 1 < current_wall[0]:
                        # self.goto(self.xcor() + 1, self.ycor())
                        self.forward(1)
                    elif self.xcor() + width + 1 == current_wall[0]:
                        self.go_left = True
                        self.go_right = False
                        self.left(180)
                if self.go_left and current_wall[0] < 0:
                    if self.xcor() > current_wall[0] + width - 1:
                        # self.goto(self.xcor() - 1, self.ycor())
                        self.forward(1)
                    elif self.xcor() == current_wall[0] + width - 1:
                        self.go_left = False
                        self.go_right = True
                        self.left(180)

    def checkCollision(self, player):
        global keepGoing
        px = player.xcor()  # Player x
        py = player.ycor()  # Player y
        mx = self.xcor()  # Monster x
        my = self.ycor()  # Monster y

        if py == my:
            if px <= mx + width and px + width >= mx:
                print 'hit'
                keepGoing = False


# Die Mauern des Labyrinths

class Sprite(t.Turtle):
    def __init__(self, shape):
        t.Turtle.__init__(self)
        self.shape(shape)
        self.penup()
        self.speed(0)


class Player(Sprite):

    def __init__(self, shape):
        Sprite.__init__(self, shape)

    def changeShape(self, res):
        wn.register_shape(os.path.join(os.getcwd(), res))
        self.shape(os.path.join(os.getcwd(), res))

    def go_left(self):
        global score, level_counter
        res = "pacman_left.gif"
        self.changeShape(res)

        go_to_x = self.xcor() - width
        go_to_y = self.ycor()

        # hit the wall
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        # hit monster --> end game
        # if go_to_x <= monster.xcor() + width and go_to_y == monster.ycor():
        #    print "Monster"

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
            level_counter += 1
            setup_maze()

        # hit a cherry
        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                fruit[0].goto(-1000, 1000)
                fruit[0].clear()
                self.goto(go_to_x, go_to_y)
                print "Cherry"
                fruits.remove(fruit)
                print fruits
                score += 1
                t.undo()
                t.penup()
                t.hideturtle()
                t.color("white")
                t.setposition(-260, 207)
                t.write("Score " + str(score), move=False, align="center", font=("Arial", 20, "normal"))

    def go_right(self):
        global score, level_counter
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
            t.write("Score " + str(score), move=False, align="center", font=("Arial", 20, "normal"))
            wn.tracer(0)
            time.sleep(2)
            wn.clear()
            wn.bgcolor("black")
            del walls[:]
            del fruits[:]
            level_counter += 1
            setup_maze()

        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                fruit[0].goto(-1000, 1000)
                fruit[0].clear()
                self.goto(go_to_x, go_to_y)
                print "Cherry"
                fruits.remove(fruit)
                print fruits
                score += 1
                t.undo()
                t.penup()
                t.hideturtle()
                t.color("white")
                t.setposition(-260, 207)
                t.write("Score " + str(score), move=False, align="center", font=("Arial", 20, "normal"))

    def go_up(self):
        global score, level_counter
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
            level_counter += 1
            setup_maze()

        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                fruit[0].goto(-1000, 1000)
                fruit[0].clear()
                self.goto(go_to_x, go_to_y)
                print "Cherry"
                fruits.remove(fruit)
                print fruits
                score += 1
                t.undo()
                t.penup()
                t.hideturtle()
                t.color("white")
                t.setposition(-260, 207)
                t.write("Score " + str(score), move=False, align="center", font=("Arial", 20, "normal"))

    def go_down(self):
        global score, level_counter

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
            level_counter += 1
            setup_maze()

        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                fruit[0].goto(-1000, 1000)
                fruit[0].clear()
                self.goto(go_to_x, go_to_y)
                print "Cherry"
                fruits.remove(fruit)
                print fruits
                score += 1
                t.undo()
                t.penup()
                t.hideturtle()
                t.color("white")
                t.setposition(-260, 207)
                t.write("Score " + str(score), move=False, align="center", font=("Arial", 20, "normal"))


# List of Labyrinth
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
    "#              #   #",
    "#   ########   #   #",
    "#   #  d# f#   #   #",
    "#   #          #   #",
    "#   ############   #",
    "#         m        #",
    "####################"
]

level_3 = [
    "####################",
    "#@       # d#     f#",
    "#### #####  #  #####",
    "# f#     #  #     f#",
    "# f####  #  #     f#",
    "#        #  #     f#",
    "#        #     #   #",
    "#  #############   #",
    "#              #   #",
    "#   ########   #   #",
    "#   #   # f#   #   #",
    "#   #          #   #",
    "#   ############   #",
    "#         m        #",
    "####################"
]

levels.append(level_1)
levels.append(level_2)
levels.append(level_3)


# Level Setup
def setup_maze():
    global level_counter
    global keepGoing

    if level_counter == 0:
        level = levels[0]
        endGame()
    if level_counter == 1:
        level = levels[1]
    if level_counter == 2:
        level = levels[2]
    if level_counter > 2:
        endGame()

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
                player = Player(player_shape)
                player.goto(screen_x, screen_y)

                # Auf Tastaturereignisse lauschen
                t.listen()
                t.onkey(player.go_left, "Left")
                t.onkey(player.go_right, "Right")
                t.onkey(player.go_up, "Up")
                t.onkey(player.go_down, "Down")
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
                monster = Monster(monster_shape)
                monster.goto(screen_x, screen_y)
    while keepGoing:
        wn.update()
        monster.move()
        monster.checkCollision(player)


def exitGame():
    global keepGoing
    keepGoing = False


def endGame():
    # bisherigen Highscore auslesen
    with open("highscore.txt") as highscoreContainer:
        highscore = highscoreContainer.readline()
    print "highscore " + highscore
    print type(highscore)
    highscoreContainer.close()

    if score > float(highscore):
        f = open("highscore.txt", "w")
        f.write(str(score))


walls = []
fruits = []
wall = Sprite(wall_shape)
door = Sprite(door_shape)

wn.tracer(0)
keepGoing = True

setup_maze()
