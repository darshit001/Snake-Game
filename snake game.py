import turtle
import time
import random   
import winsound
from playsound import playsound

def play():
    winsound.PlaySound('bg.wav',winsound.SND_ASYNC)

def crash():
    winsound.PlaySound('cresh.wav',winsound.SND_ASYNC)

delay = 0.1
level = 1
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("light green")
wn.bgpic('img.gif')
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates


turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,310)
turtle.pendown()
turtle.color('green') 
turtle.forward(620)
turtle.right(90)
turtle.forward(620)
turtle.right(90)
turtle.forward(620)
turtle.right(90)
turtle.forward(620)
turtle.penup()
turtle.hideturtle()


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("orange")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.fillcolor("blue")
food.penup()
food.goto(0,80)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 320)
pen.write("Score: 0  High Score: 0  Level: 1", align="center", font=("Courier", 16, "normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(play," ")

while True:
    wn.update()

   
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

      

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1
        
        # Reset level
        level = 1

        pen.clear()
        pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center", font=("Courier", 16, "normal"))


    if head.distance(food) < 20: 
        
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("pink")
        new_segment.fillcolor("orange")
        new_segment.penup()
        segments.append(new_segment)        
        delay -= 0.001
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center", font=("Courier", 16, "normal"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

   
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    for segment in segments:
        if segment.distance(head) < 20:
            crash()
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
            
            # Reset the level
            level = 1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align="center", font=("Courier", 16, "normal"))

    if level == 1 and score == 50:
        level += 1
        delay *= 0.9
    if level == 2 and score == 100:
        level += 1
        delay *= 0.9
    if level == 3 and score == 150:
        level += 1
        delay *= 0.9          
    time.sleep(delay)
wn.mainloop()
