import turtle
import random
import time

# ---------------------------
# Game Configuration
# ---------------------------
delay = 0.1
score_value = 0
high_score = 0
bodies = []

# ---------------------------
# Screen Setup
# ---------------------------
screen = turtle.Screen()
screen.title("🐍 Snake Game - Enhanced Edition 🐍")
screen.bgcolor("#f0f8ff")  # light blue background
screen.setup(width=700, height=700)
screen.tracer(0)  # turn off auto updates

# ---------------------------
# Border Frame
# ---------------------------
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.pensize(3)
border.color("dark blue")
border.goto(-300, 300)
border.pendown()
for _ in range(4):
    border.forward(600)
    border.right(90)

# ---------------------------
# Score Display Box
# ---------------------------
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 310)
score_display.color("black")
score_display.write("SCORE: 0  |  HIGH SCORE: 0", align="center", font=("Courier", 18, "bold"))

# ---------------------------
# Snake Head
# ---------------------------
head = turtle.Turtle()
head.shape("circle")
head.color("#ff4500")  # orange-red
head.fillcolor("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# ---------------------------
# Food
# ---------------------------
food = turtle.Turtle()
food.shape("turtle")
food.color("green")
food.shapesize(0.8, 0.8)
food.penup()
food.goto(100, 100)

# ---------------------------
# Movement Functions
# ---------------------------
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def stop_movement():
    head.direction = "stop"

# ---------------------------
# Keyboard Bindings
# ---------------------------
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(stop_movement, "space")

# ---------------------------
# Game Loop
# ---------------------------
while True:
    screen.update()

    # Border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = "stop"

        for b in bodies:
            b.hideturtle()
        bodies.clear()

        score_value = 0
        delay = 0.1
        score_display.clear()
        score_display.write(f"SCORE: {score_value}  |  HIGH SCORE: {high_score}", align="center", font=("Courier", 18, "bold"))

    # Food collision
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Create new body part
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("circle")
        new_body.color(random.choice(["#006400", "#228B22", "#32CD32"]))  # shades of green
        new_body.penup()
        bodies.append(new_body)

        score_value += 100
        if score_value > high_score:
            high_score = score_value
        delay -= 0.001
        score_display.clear()
        score_display.write(f"SCORE: {score_value}  |  HIGH SCORE: {high_score}", align="center", font=("Courier", 18, "bold"))

    # Move snake body
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if bodies:
        bodies[0].goto(head.xcor(), head.ycor())

    move()

    # Check self-collision
    for segment in bodies:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"
            for b in bodies:
                b.hideturtle()
            bodies.clear()
            score_value = 0
            delay = 0.1
            score_display.clear()
            score_display.write(f"SCORE: {score_value}  |  HIGH SCORE: {high_score}", align="center", font=("Courier", 18, "bold"))

    time.sleep(delay)
