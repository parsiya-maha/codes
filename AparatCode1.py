import turtle as t
from time import sleep

wn = t.Screen()
wn.setup(600,600)
wn.title('python')
wn.bgcolor("green")
wn.tracer(0)


obj = t.Turtle()
obj.penup()
obj.width(3)
obj.pencolor('blue')
obj.pendown()
obj.lt(90)
obj.color('red')
obj.direction = 'stop'

 
def go_up():
    obj.direction = 'up'

def go_down():
    obj.direction = 'down'

def go_right():
    obj.direction = 'right'

def go_left():
    obj.direction = 'left'


def move() :

    if obj.direction == 'up':
        y = obj.ycor()
        obj.sety(y+30)

    if obj.direction == 'down':
        y = obj.ycor()
        obj.sety(y-30)

    if obj.direction == 'right':
        x = obj.xcor()
        obj.setx(x+30)

    if obj.direction == 'left' :
        x = obj.xcor()
        obj.setx(x-30)


wn.listen()


wn.onkeypress(go_up,'w')
wn.onkeypress(go_down,'s')
wn.onkeypress(go_right,'d')
wn.onkeypress(go_left,'a')



while True:
    wn.update()
    sleep(0.1)

    move()


wn.mainloop()