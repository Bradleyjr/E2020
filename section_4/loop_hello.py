from turtle import *

# Function variables
space_width = 10 # Default value: 30
letter_height = 50 # Default value: 100
letter_width = 30 # Default value: 50
pen_color = input("Enter a color to set the pen's color. ")
#pen_width = input("Enter a number from 1-10 to set the pen width: ")

def draw_space():
    # Add a space 30 pixels wide.
    penup()
    forward(space_width)
    pendown()

def move_turtle():
    # Pick up the turtle and move it to its starting location.
    penup()
    goto(-200, 100)
    pendown()



def draw_H():
    # Draw the left leg of the H.
    # The turtle starts at the bottom left of the letter, pointing right.
    left(90)
    forward(letter_height)
    # Draw the bar of the H.
    # The turtle starts at the top of the left leg, pointing up.
    forward(-letter_height / 2)
    right(90)
    forward(letter_width)
    # Draw the right leg of the H.
    # The turtle starts on the right side of the bar, pointing right.
    left(90)
    forward(letter_height / 2)
    forward(-letter_height)
    right(90)
    # The H is drawn.
    # The turtle is at the bottom right, pointing right.
    draw_space()


def draw_E():
    # Draw an E.
    left(90)
    forward(letter_height)
    right(90)
    forward(letter_width)
    forward(-letter_width)
    right(90)
    forward(letter_height / 2)
    left(90)
    forward(letter_width)
    forward(-letter_width)
    right(90)
    forward(letter_height / 2)
    left(90)
    forward(letter_width)
    draw_space()

def draw_L():
    # Draw the L
    left(90)
    forward(letter_height)
    forward(-letter_height)
    right(90)
    forward(letter_width)
    draw_space()

def draw_O():
    # Draw the O.
    forward(letter_width)
    left(90)
    forward(letter_height)
    left(90)
    forward(letter_width)
    left(90)
    forward(letter_height)
    left(90)
    forward(letter_width)
    draw_space()

def HELLO():    
    color(pen_color)
    #width(pen_width)
    move_turtle()
    draw_H()
    draw_E()
    draw_L()
    draw_L()
    draw_O()
    exitonclick()


for i in range(10):
    HELLO()
    width(i)
    right(i)
