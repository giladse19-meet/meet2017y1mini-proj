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
TIME_STEP = 100
SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

#call functions
def up():
    global direction
    direction = UP
    print("You pressed the up key!")
def left():
    global direction
    direction = LEFT
    print("You pressed the left key!")
def down():
    global direction
    direction = DOWN
    print("You pressed the down key!")
def right():
    global direction
    direction = RIGHT
    print("You pressed the right key!")

#make turtle listen
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()


#location of food
def make_food():

    food = turtle.clone()
    food.shape("circle")
    food.stamps = []
    food.hideturtle()
    
    min_x = -int(size_x/2/square_size)+1
    max_x = int(size_x/2/square_size)-1
    min_x = -int(size_y/2/square_size)-1
    max_y = int(size_y/2/square_size)+1

    food_x = random.randint(min_x, max_x)*squre_size
    food_y = random.randint(min_y, max_y)*square_size

    for i in food_pos:
    food.goto(food_x, food_y)
    food_id = food.stamp()
    food_stamps.append(food_id)

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

    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    global food_stamps, food_pos
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])

        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have eaten a food!")
        
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! game over!")
        quit()

    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! game over!")
        quit()

    elif new_y_pos >= UP_EDGE:
        print("You hit the up edge! game over!")
        quit()

    elif new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! game over!")
        quit()
        
    turtle.ontimer(move_snake, TIME_STEP)

move_snake()
