import turtle as t
import os
import time

wn = t.Screen()
wn.bgcolor("black")
wn.setup(640, 480)

score_label = t.Turtle()
nextLevel_label = t.Turtle()

score_label.hideturtle()
nextLevel_label.hideturtle()

score = 0
level_counter = 0
width = 32

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


# Monster class

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
                        self.forward(1)
                    elif self.xcor() + width + 1 == current_wall[0]:
                        self.go_left = True  # turtle change direction
                        self.go_right = False
                        self.left(180)  # turtle turn around
                if self.go_left and current_wall[0] < 0:
                    if self.xcor() > current_wall[0] + width - 1:
                        self.forward(1)
                    elif self.xcor() == current_wall[0] + width - 1:
                        self.go_left = False  # turtle change direction
                        self.go_right = True
                        self.left(180)  # turtle turn around

    def checkCollision(self, player):
        global keepGoing
        px = player.xcor()  # Player x
        py = player.ycor()  # Player y
        mx = self.xcor()  # Monster x
        my = self.ycor()  # Monster y

        if py == my:
            if px <= mx + width and px + width >= mx:
                endGame()
                self.goto(-1000, -1000)


# Walls and Fruits of the game
class Component(t.Turtle):
    def __init__(self, shape):
        t.Turtle.__init__(self)
        self.shape(shape)
        self.penup()
        self.speed(0)


class Player(Component):

    def __init__(self, shape):
        Component.__init__(self, shape)

    # method to replace the Shape Img
    def changeShape(self, res):
        wn.register_shape(os.path.join(os.getcwd(), res))
        self.shape(os.path.join(os.getcwd(), res))

    # method to get to next Level
    @staticmethod
    def next_level():
        global level_counter
        global level_stop
        nextLevel_label.undo()
        nextLevel_label.penup()
        nextLevel_label.hideturtle()
        nextLevel_label.color("white")
        nextLevel_label.setposition(width / 2, 0)
        nextLevel_label.write("Next Level ", move=False, align="center", font=("Arial", 20, "normal"))
        wn.tracer(0)
        time.sleep(2)
        wn.clear()
        wn.bgcolor("black")
        del walls[:]                # empty the Walls and Fruits Array --> will be refilled in setup_level
        del fruits[:]
        level_counter += 1          # count up for next Level
        level_stop = True
        level_stop = False
        init_level()



    @staticmethod
    def collect_fruit(fruit):
        global score
        fruit[0].goto(-1000, 1000)  # put fruit out of Screen and clear, bc delete Turtle not possbile
        fruit[0].clear()
        fruits.remove(fruit)        # remove from Array of fruits, so Play won't recognize again
        score += 1                  # count up the global Var Score
        score_label.undo()          # rewrite the Score Label-Turtle
        score_label.penup()
        score_label.hideturtle()
        score_label.color("white")
        score_label.setposition(-260, 207)
        score_label.write("Score " + str(score), move=False, align="center", font=("Arial", 20, "normal"))

    def go_left(self):
        self.changeShape("pacman_left.gif")

        go_to_x = self.xcor() - width
        go_to_y = self.ycor()

        # hit the wall
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        # Hit the door
        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            self.next_level()

        # hit a cherry
        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                self.goto(go_to_x, go_to_y)
                self.collect_fruit(fruit)

    def go_right(self):
        self.changeShape("pacman_right.gif")

        go_to_x = self.xcor() + width
        go_to_y = self.ycor()

        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            self.next_level()

        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                self.goto(go_to_x, go_to_y)
                self.collect_fruit(fruit)

    def go_up(self):
        self.changeShape("pacman_up.gif")
        go_to_x = self.xcor()
        go_to_y = self.ycor() + width
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            self.next_level()

        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                self.goto(go_to_x, go_to_y)
                self.collect_fruit(fruit)

    def go_down(self):
        self.changeShape("pacman_down.gif")
        go_to_x = self.xcor()
        go_to_y = self.ycor() - width
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        # hit the door
        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            self.next_level()

        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                self.goto(go_to_x, go_to_y)
                self.collect_fruit(fruit)


# List of Level
levels = []
# two dimensional Array for the Level Design
level_1 = [
    "####################",
    "#  #ff             #",
    "#  #######  #####  #",
    "#        #  #f     #",
    "# f      #  #####  #",
    "#######  #  #f     #",
    "#        #  ##### p#",
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
    "#ff#ff  #f  #   p  #",
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
    "#p       # d#     f#",
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
def init_level():
    global level_counter
    global keepGoing

    if level_counter == 0:
        setup_level(levels[0])
    if level_counter == 1:
        setup_level(levels[1])
    if level_counter == 2:
        setup_level(levels[2])
    if level_counter > 2:
        endGame()


def setup_level(level):
    global score
    global level_stop
    # iterate over the levels Array for y-coordinate and x-coordinate
    for y in range(len(level)):
        for x in range(len(level[y])):
            symbol = level[y][x]
            screen_x = -308 + (x * width)
            screen_y = 224 - (y * width)

            if symbol == "#":
                wall.goto(screen_x, screen_y)
                walls.append((screen_x, screen_y))
                wall.stamp()
            if symbol == "p":
                player = Player(player_shape)
                player.goto(screen_x, screen_y)

                # listen to player key events
                t.listen()
                t.onkey(player.go_left, "Left")
                t.onkey(player.go_right, "Right")
                t.onkey(player.go_up, "Up")
                t.onkey(player.go_down, "Down")
                t.onkey(exitGame, "Escape")  # Escape beendet das Spiel
            if symbol == "f":
                fruit = Component(fruit_shape)
                fruit.goto(screen_x, screen_y)
                fruits.append([fruit, (screen_x, screen_y)])
                fruit.stamp()
            if symbol == "d":
                door.goto(screen_x, screen_y)
                door.stamp()
            if symbol == "m":
                monster = Monster(monster_shape)
                monster.goto(screen_x, screen_y)
    score_label.penup()
    score_label.hideturtle()
    score_label.color("white")
    score_label.setposition(-260, 207)
    score_label.write("Score " + str(score), move=False, align="center", font=("Arial", 20, "normal"))

    while keepGoing:
        wn.update()
        monster.move()
        monster.checkCollision(player)
        print str(monster.pos())
        if level_stop:
            print "bla"
            break


def exitGame():
    global keepGoing
    keepGoing = False


def endGame():
    print "End game"
    wn.clear()
    wn.bgcolor("black")
    nextLevel_label.undo()
    nextLevel_label.penup()
    nextLevel_label.hideturtle()
    nextLevel_label.color("white")
    nextLevel_label.write("END", move=False, align="center", font=("Arial", 20, "normal"))
    # bisherigen Highscore auslesen
    # with open("highscore.txt") as highscoreContainer:
    #   highscore = highscoreContainer.readline()
    # print "highscore " + highscore
    # print type(highscore)
    # highscoreContainer.close()

    # if score > float(highscore):
    #   f = open("highscore.txt", "w")
    #  f.write(str(score))


walls = []
fruits = []
wall = Component(wall_shape)
door = Component(door_shape)


wn.tracer(0)
keepGoing = True
level_stop = False

init_level()