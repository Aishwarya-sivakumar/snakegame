import turtle
import time
import random

delay= 0.2

#screensetting

ash = turtle.Screen()
ash.title("snake game")
ash.bgcolor("yellow")
ash.setup(width=700, height=700)
ash.tracer(0)

#function for movement

def go_up():
    head.direction= "up"

def go_down():
    head.direction= "down"

def go_left():
    head.direction= "left"

def go_right():
    head.direction= "right"

def move():
    if head.direction== "up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction== "down":
        y=head.ycor()
        head.sety(y-20)
        
    if head.direction== "left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction== "right":
        x=head.xcor()
        head.setx(x+20)    

#keyboard bindings

    ash.listen()
    ash.onkeypress(go_up,"Up")
    ash.onkeypress(go_down,"Down")
    ash.onkeypress(go_left,"Left")
    ash.onkeypress(go_right,"Right")
    


#snake head

head=turtle.Turtle()
head.speed(0)
head.color("red")
head.shape("triangle")
head.penup()
head.goto(0,0)
head.direction= "stop"

#snake food

food=turtle.Turtle()
food.speed(0)
food.color("blue")
food.shape("circle")
food.penup()
food.goto(0,100)

segments = []



#main game hoop

while True:
    ash.update()

    #check for border collsion
    if head.xcor() > 340 or head.xcor() < -340 or head.ycor() > 340 or head.ycor() < -340:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        #hide the segments
        for segment in segments:
            segment.goto(4000,4000)
        #clear the segments list
            segments.clear()

       
    

    if head.distance(food) < 20:
        #move the food to random place
        
        x = random.randint(-340, 340)
        y = random.randint(-340, 340)
        food.goto(x,y)

        #snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("pink")
        new_segment.penup()
        segments.append(new_segment)

    #move the end segments in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segment 0 to wherethe head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    time.sleep(delay)

ash.mainloop()

