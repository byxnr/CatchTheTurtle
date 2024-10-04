import random
import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.title("Turtle Clicker Game")
screen.bgcolor("lightblue")
screen.setup(width=800, height=800)

# Score and timer variables
score = 0
timer = 15  # 30 seconds for the game
turtle_visible_duration = 650

# Turtle setup
t = turtle.Turtle()
t.shape("turtle")
t.shapesize(2,2)
t.color("green")
t.penup()
t.speed(0)
t.hideturtle()

# Score display
score_display = turtle.Turtle()
score_display.penup()
score_display.hideturtle()
# Position score at the upper middle center
score_display.goto(0, 350)
score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# Timer display
timer_display = turtle.Turtle()
timer_display.penup()
timer_display.hideturtle()
# Position timer under the score
timer_display.goto(0, 320)
timer_display.write(f"Time left: {timer}s", align="center", font=("Arial", 24, "normal"))

# Function to move the turtle to a random position
def move_turtle():
    if timer > 0:
        x = random.randint(-390, 390)
        y = random.randint(-290, 290)
        t.goto(x, y)
        t.showturtle()
        screen.ontimer(t.hideturtle, turtle_visible_duration)
        screen.ontimer(move_turtle, turtle_visible_duration)
    else:
        t.hideturtle()

# Function to update score when turtle is clicked
def on_turtle_click(x, y):
    global score
    if timer > 0:  # Only allow clicks if timer is running
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# Countdown timer function
def countdown():
    global timer
    if timer > 0:
        timer -= 1
        timer_display.clear()
        timer_display.write(f"Time left: {timer}s", align="center", font=("Arial", 24, "normal"))
        # Call countdown again after 1 second
        screen.ontimer(countdown, 1000)
    else:
        timer_display.clear()
        timer_display.write("Time's up!", align="center", font=("Arial", 24, "normal"))
        t.hideturtle()  # Hide the turtle when time's up

# Binding click event to the turtle
t.onclick(on_turtle_click)

# Main game loop
move_turtle()
countdown()  # Start the countdown
screen.mainloop()
