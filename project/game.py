import turtle as t
import os
import time

# screen
wn = t.Screen()
wn.bgcolor("black")
wn.setup(640, 480)  # width and height of  screen --> size Quelle1

score_label = t.Turtle()  # turtle to write the score
nextLevel_label = t.Turtle()  # turtle to announce the next level
button = t.Turtle()  # turtle for start button

score_label.hideturtle()
nextLevel_label.hideturtle()
button.hideturtle()

score = 0
level_counter = 0  # tells the current level - 1
width = 32  # width of cherries, door, pacman, etc. is always 32

# shapes of the different game components
wall_shape = os.path.join(os.getcwd(), "wall.gif")
fruit_shape = os.path.join(os.getcwd(), "cherry.gif")
player_shape = os.path.join(os.getcwd(), "pacman_right.gif")
monster_shape = os.path.join(os.getcwd(), "monster.gif")
door_shape = os.path.join(os.getcwd(), "door.gif")

# register shapes Quelle1
# screen turtle registers the different shapes
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

    # movement of monster
    # if there is a collision with a wall -> has to change movement direction
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

    # check collision with packman
    def checkCollision(self, player):
        global keepGoing
        px = player.xcor()  # Player x
        py = player.ycor()  # Player y
        mx = self.xcor()  # Monster x
        my = self.ycor()  # Monster y

        if py == my:
            if px <= mx + width and px + width >= mx:
                endGame()  # in case of collision, game is ended
                self.goto(-1000, -1000)


# Walls and Fruits of the game --> Quelle1
class Component(t.Turtle):
    def __init__(self, shape):
        t.Turtle.__init__(self)
        self.shape(shape)
        self.penup()
        self.speed(0)


# player class
# angelehnt and Player Klasse in Quelle1
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
        nextLevel_label.undo()
        nextLevel_label.penup()
        nextLevel_label.hideturtle()
        nextLevel_label.color("white")
        nextLevel_label.setposition(width / 2, 0)
        if not level_counter == 2:  # only annouces next level, if there exists a next level
            nextLevel_label.write("Next Level ", move=False, align="center", font=("Arial", 20, "normal"))
        wn.tracer(0)
        time.sleep(2)
        wn.clear()
        wn.bgcolor("black")
        del walls[:]  # empty the Walls and Fruits Array --> will be refilled in setup_level
        del fruits[:]
        level_counter += 1  # count up for next Level
        init_level()  # init the next level

    # method to collect the cherries
    @staticmethod
    def collect_fruit(fruit):
        global score
        fruit[0].goto(-1000, 1000)  # put fruit out of Screen and clear, bc delete Turtle not possbile
        fruit[0].clear()
        fruits.remove(fruit)  # remove from Array of fruits, so Play won't recognize again
        score += 1  # count up the global Var Score
        score_label.undo()  # rewrite the Score Label-Turtle
        score_label.penup()
        score_label.hideturtle()
        score_label.color("white")
        score_label.setposition(-260, 207)
        score_label.write("Score " + str(score), move=False, align="center", font=("Arial", 20, "normal"))

    def go_left(self):
        self.changeShape("pacman_left.gif")

        # go_to_x / y -> Quelle1
        go_to_x = self.xcor() - width
        go_to_y = self.ycor()

        # hit the wall
        # Quelle 1
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

        # go_to_x / y -> Quelle1
        go_to_x = self.xcor() + width
        go_to_y = self.ycor()

        # hit the wall
        # Quelle 1
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        # hit the door
        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            self.next_level()

        # hit a cherry
        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                self.goto(go_to_x, go_to_y)
                self.collect_fruit(fruit)

    def go_up(self):
        self.changeShape("pacman_up.gif")
        # go_to_x / y -> Quelle1
        go_to_x = self.xcor()
        go_to_y = self.ycor() + width

        # hit the wall
        # Quelle 1
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        # hit the door
        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            self.next_level()

        # hit a cherry
        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                self.goto(go_to_x, go_to_y)
                self.collect_fruit(fruit)

    def go_down(self):
        self.changeShape("pacman_down.gif")
        # go_to_x / y -> Quelle1
        go_to_x = self.xcor()
        go_to_y = self.ycor() - width

        # hit the wall
        # Quelle 1
        if (go_to_x, go_to_y) not in walls:
            self.goto(go_to_x, go_to_y)

        # hit the door
        if (go_to_x, go_to_y) == (door.xcor(), door.ycor()):
            self.goto(go_to_x, go_to_y)
            self.next_level()

        # hit a cherry
        for fruit in fruits:
            if (go_to_x, go_to_y) == fruit[1]:
                self.goto(go_to_x, go_to_y)
                self.collect_fruit(fruit)


# List of Levels
levels = []
# two dimensional Array for the Level Design
# '#' is the symbol for a wall
# 'd' is the symbol for a door
# 'c' is the symbol for a cherry
# 'p' is the symbol for a player
# 'm' is the symbol for a monster

# Level Design Quelle1
level_1 = [
    "####################",
    "# p#cc             #",
    "#  #######  #####  #",
    "#        #  #c     #",
    "# c      #  #####  #",
    "#######  #  #c     #",
    "#        #  #####  #",
    "#  #######    #    #",
    "#             # c d#",
    "#  #################",
    "#         m        #",
    "####  ###########  #",
    "#            #     #",
    "#            #c    #",
    "####################"
]
level_2 = [
    "####################",
    "#cc#cc  #c  #   p  #",
    "#  # #####  #  #####",
    "#  #     #  #      #",
    "#  ####  #  ####   #",
    "#        #  #c     #",
    "#        #     #   #",
    "#  #############   #",
    "#              #   #",
    "#   ########   #   #",
    "#   #  d# c#   #   #",
    "#   #          #   #",
    "#   ############   #",
    "#         m        #",
    "####################"
]

level_3 = [
    "####################",
    "#p       # d#     c#",
    "#### #####  #  #####",
    "# c#     #  #     c#",
    "# c####  #  #     c#",
    "#        #  #     c#",
    "#        #     #   #",
    "#  #############   #",
    "#              #   #",
    "#   ########   #   #",
    "#   #  c# c#   #   #",
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
    global keepGoing  # while true, game continues
    if level_counter == 0:
        setup_level(levels[0])
    if level_counter == 1:
        setup_level(levels[1])
    if level_counter == 2:
        setup_level(levels[2])
    if level_counter > 2:  # ends because there are only three levels
        endGame()


# setup Level Quelle1
def setup_level(level):
    global score
    # iterate over the levels Array for y-coordinate and x-coordinate
    for y in range(len(level)):
        for x in range(len(level[y])):
            symbol = level[y][x]
            screen_x = -308 + (x * width)
            screen_y = 224 - (y * width)
            # setup wall
            if symbol == "#":
                wall.goto(screen_x, screen_y)
                walls.append((screen_x, screen_y))
                wall.stamp()
            # setup player
            if symbol == "p":
                player = Player(player_shape)
                player.goto(screen_x, screen_y)

                # listen to player key events
                t.listen()
                # OnKey Listener Quelle1
                t.onkey(player.go_left, "Left")
                t.onkey(player.go_right, "Right")
                t.onkey(player.go_up, "Up")
                t.onkey(player.go_down, "Down")
                t.onkey(exitGame, "Escape")  # Escape beendet das Spiel
            # setup cherry
            if symbol == "c":
                fruit = Component(fruit_shape)
                fruit.goto(screen_x, screen_y)
                fruits.append([fruit, (screen_x, screen_y)])
                fruit.stamp()
            # setup door
            if symbol == "d":
                door.goto(screen_x, screen_y)
                door.stamp()
            # setup monster
            if symbol == "m":
                monster = Monster(monster_shape)
                monster.goto(screen_x, screen_y)
    # show the score
    score_label.penup()
    score_label.hideturtle()
    score_label.color("white")
    score_label.setposition(-260, 207)
    score_label.write("Score " + str(score), move=False, align="center", font=("Arial", 20, "normal"))

    # game loop
    # Quelle1
    while keepGoing:
        wn.update()
        monster.move()
        monster.checkCollision(player)


# start screen
def update_start_screen():
    wn.bgcolor("black")
    while updateStartScreen:
        wn.update()


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


# function to start the game, when the player clicks start
def buttonclick(x, y):
    global updateStartScreen
    x_left_border = width / 2 - 80
    x_right_border = 86
    # if users clicks on button, game starts
    if x_left_border < x < x_right_border and 0 < y < 30:  # rectangle of button
        button.undo()
        wn.bgcolor("black")
        updateStartScreen = False
        init_level()  # if start button is pressed, then the game starts


# define and setup the start button
def setupStartButton():
    button.goto(width / 2 - 80, 0)
    button.forward(150)
    button.left(90)
    button.forward(30)
    button.left(90)
    button.forward(150)
    button.left(90)
    button.forward(30)
    button.left(90)
    # draw rectangle of button
    button.penup()
    button.color("white")
    button.goto(width / 2, 0)
    button.write("Start game ", align="center", font=("Arial", 20, "normal"))


walls = []
fruits = []
wall = Component(wall_shape)
door = Component(door_shape)
wall.hideturtle()
door.hideturtle()

wn.tracer(0)
keepGoing = True
updateStartScreen = True

# create the start button
setupStartButton()
t.onscreenclick(buttonclick, 1)
t.listen()
update_start_screen()



# Quelle1: https://medium.com/@jkantel/ein-rogue-like-mit-python-und-der-turtle-stage-2-d3c3f5fa0401