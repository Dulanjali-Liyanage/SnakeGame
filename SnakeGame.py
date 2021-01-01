from turtle import *
from random import randrange
from freegames import square,vector

food = vector(0,0)
snake = [vector(10,0)]
aim = vector(0,-10)

#change the snake direction
def change(x,y):
    aim.x = x # x axis
    aim.y = y # y axis

#return true if head hits the boundary
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

#sanke only moves forward
#this function helps to move the snake in forward direction
def move():
    #-1 is the forward movememnt value and
    #copy will copy the same forward value
    head = snake[-1].copy()
    head.move(aim)

    
    if not inside(head) or head in snake:
        square(head.x,head.y,9,'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:',len(snake))
        food.x = randrange(-15,15)*10
        food.y = randrange(-15,15)*10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x,body.y,9,'black')

    square(food.x,food.y,9,'green')
    update()
    ontimer(move,100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False) #bring backs the elements to the initial state
listen()

#set the key controls
#giving x and y values
onkey(lambda:change(10,0),'Right')
onkey(lambda:change(-10,0),'Left')
onkey(lambda:change(0,10),'Up')
onkey(lambda:change(0,-10),'Down')

move()
done()
    
