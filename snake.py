import turtle
import random

turtle.tracer(1, 0)

size_X = 800
size_Y = 500
turtle.setup(size_X, size_Y)

turtle.penup()

square_size = 20
start_length = 5

pos_list = []
stamp_list = []
food_pos = []
food_stamp = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

for num in range(start_length):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]
    x_pos = x_pos + square_size
    my_pos = (x_pos, y_pos)
    snake.goto(my_pos)
    pos_list.append(my_pos)
    stamp_id = snake.stamp()
    stamp_list.append(stamp_id)
    
UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
TIME_ARROW = 100
SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

#call functions
def up():
    global direction
    direction = UP
    move_snake()
    print("You pressed the up key!")
def left():
    global direction
    direction = LEFT
    move_snake()
    print("You pressed the left key!")
def down():
    global direction
    direction = DOWN
    move_snake()
    print("You pressed the down key!")
def right():
    global direction
    direction = RIGHT
    move_snake()
    print("You pressed the right key!")

#make turtle listen
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

#make turtle move
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        snake.goto(x_pos + square_size, y_pos)
        print("You moved right!")
    elif direction == LEFT:
        snake.goto(x_pos - square_size, y_pos)
        print("You moved left!")
    elif direction == UP:
        snake.goto(x_pos, y_pos + square_size)
        print("You moved up!")
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - square_size)
        print("You moved down!")

