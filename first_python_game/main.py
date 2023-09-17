
"""
123
"""
import turtle
import winsound

wn = turtle.Screen()
wn.title("Ping pong game, made using tuturial")
wn.bgcolor("black")
screen_width = 800
screen_height = 600
wn.setup(width=screen_width, height=screen_height)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

#Panddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a_position = -350
paddle_a.goto(paddle_a_position, 0)

#Panddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b_position = 350
paddle_b.goto(paddle_b_position, 0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

# moving paddles
def paddle_a_up():
    if paddle_a.ycor() < screen_height/2 - 50:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    if paddle_a.ycor() > -screen_height/2 + 60:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)
    
def paddle_b_up():
    if paddle_b.ycor() < screen_height/2 - 50:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if paddle_b.ycor() > -screen_height/2 + 60:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)
    
# Keyboard binind
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = 0.4

while(True):
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.xcor() >(screen_width/2 - 20):
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        winsound.PlaySound("laser1.wav", winsound.SND_ASYNC)
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        
    if  ball.xcor() <(-screen_width/2 + 10):
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        winsound.PlaySound("laser1.wav", winsound.SND_ASYNC)
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        
    if ball.ycor() >(screen_height/2 - 10) or ball.ycor() <(-screen_height/2 + 20):
        #ball.sety(screen_height/2 - 10)
        ball.dy *= -1
        
    # Paddle ball collisions
    # if ball.xcor() > (paddle_b_position/2-10) and  ball.xcor() < (paddle_b_position/2) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > (paddle_b.ycor() - 10)):
    if (ball.xcor() > (paddle_b_position-10) and ball.xcor() < paddle_b_position) and (ball.ycor()< paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor()-40):
         ball.setx(paddle_b_position-10)
         ball.dx *=-1
         
    if (ball.xcor() < (paddle_a_position+10) and ball.xcor() > paddle_a_position) and (ball.ycor()< paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40):
         ball.setx(paddle_a_position+10)
         ball.dx *=-1