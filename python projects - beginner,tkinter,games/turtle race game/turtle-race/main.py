from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def announce(winning_color, win=False):
    ann = Turtle()
    ann.hideturtle()
    ann.color("blue")
    ann.penup()
    ann.goto(x=-130, y=180)
    if win:
        text = f"You've won! The {winning_color} turtle is the winner!"
        ann.write(text, font=("Calibri", 12, "bold"))
    else:
        text = f"You've lost! The {winning_color} turtle is the winner!"
        ann.write(text, font=("Calibri", 12, "bold"))

y = -70
for c, color in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y + 30*c)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230: # each turtle is 40x40
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                # print(f"You've won! The {winning_color} turtle is the winner!")
                announce(winning_color, win=True)
            else:
                # print(f"You've lost! The {winning_color} turtle is the winner!")
                announce(winning_color, win=False)
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()