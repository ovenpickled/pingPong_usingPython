

# we start by laying out out foundation for the game
import turtle

windows = turtle.Screen()
windows.title("Ping Pong Game")
windows.bgcolor("black")
windows.setup(width=800, height=600)
windows.tracer(0)

# score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)

# Ball
balls = turtle.Turtle()
balls.speed(0)
balls.shape("square")
balls.penup()
balls.goto(0, 0)
balls.color("white")
balls.dx = 0.65
balls.dy = -0.65

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(0, 260)
pen.color("white")
pen.hideturtle()
pen.write("Player A: 0  Player B: 0", align="center", font=("bold", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Key Bindings
windows.listen()
windows.onkeypress(paddle_a_up, "w")
windows.onkeypress(paddle_a_down, "s")
windows.onkeypress(paddle_b_up, "Up")
windows.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    windows.update()

    # for moving the ball
    balls.setx(balls.xcor() + balls.dx)
    balls.sety(balls.ycor() + balls.dy)

    # for the borders
    if balls.ycor() > 290:
        balls.sety(290)
        balls.dy *= -1

    if balls.ycor() < -290:
        balls.sety(-290)
        balls.dy *= -1

    if balls.xcor() > 390:
        balls.goto(0, 0)
        balls.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("bold", 24, "normal"))

    if balls.xcor() < -390:
        balls.goto(0, 0)
        balls.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("bold", 24, "normal"))
    
    # Collision detection
    if (balls.xcor() > 340 and balls.xcor() < 350) and (balls.ycor() < paddle_b.ycor() + 40 and balls.ycor() > paddle_b.ycor() -40):
        balls.setx(340)
        balls.dx *= -1
    if (balls.xcor() < -340 and balls.xcor() >- 350) and (balls.ycor() < paddle_a.ycor() + 40 and balls.ycor() > paddle_a.ycor() -40):
        balls.setx(-340)
        balls.dx *= -1