from turtle import *

def draw_space():
    # Add a space 30 pixels wide.
    penup()
    forward(30)
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
    forward(100)
    # Draw the bar of the H.
    # The turtle starts at the top of the left leg, pointing up.
    forward(-50)
    right(90)
    forward(50)
    # Draw the right leg of the H.
    # The turtle starts on the right side of the bar, pointing right.
    left(90)
    forward(50)
    forward(-100)
    right(90)
    # The H is drawn.
    # The turtle is at the bottom right, pointing right.
    draw_space()


def draw_E():
    # Draw an E.
    left(90)
    forward(100)
    right(90)
    forward(50)
    forward(-50)
    right(90)
    forward(50)
    left(90)
    forward(50)
    forward(-50)
    right(90)
    forward(50)
    left(90)
    forward(50)
    draw_space()

def draw_L():
    # Draw an L.
    left(90)
    forward(100)
    forward(-100)
    right(90)
    forward(50)
    draw_space()

def draw_O():
# Draw an O.
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    draw_space()


def draw_newline():
    # This function will pick up the turtle and move it to a second line.
    penup()
    goto(-200,-50)
    pendown()

def draw_W():
    # Draw a W.
    right(90)
    forward(100)
    right(-90)
    forward(25)
    right(-90)
    forward(100)
    right(180)
    forward(100)
    right(-90)
    forward(25)
    right(-90)
    forward(100)
    right(180)
    forward(100)
    left(90)
    draw_space()
    
def draw_R():
    # Draw an R.
    right(-90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(180)
    forward(50)
    right(90)
    forward(50)
    left(90)
    draw_space()
    

draw_H()
draw_E()
draw_L()
draw_L()
draw_O()
draw_newline()
draw_W()
draw_O()
draw_R()
draw_L()
draw_O()
move_turtle()
exitonclick()
