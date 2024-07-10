#### Turtle Race #####

from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=1000, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = [-250, -150, -50, 50, 150, 250]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.turtlesize(2, 2, 2)
    new_turtle.penup()
    # tim.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-460, y=y_position[turtle_index])  # position of turtle on the graph
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 446:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)

screen.exitonclick()