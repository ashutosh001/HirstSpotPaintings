from turtle import Turtle,Screen
from extract_color import extract_colors
import random

class Painting():
    def __init__(self):
        self.color_list = list()
        self.diameter = 20
        self.gap = 50
        self.row = 10
        self.column = 10

    def get_colors(self):
        """Extracts the colors from the example painting and stores their rgb values in a list"""
        colors = extract_colors('images/hirst_painting.jpg', 20)
        self.color_list = colors

    def starting_point(self,turtle):
        """Moves the turtle object to starting point cordinates"""
        move = int((self.diameter*self.row+self.gap*(self.row-1))/2)
        
        turtle.up()
        turtle.setheading(225)
        turtle.forward(move)
        turtle.setheading(0)
        turtle.down()

    def next_row(self,turtle):
        """Moves the turtle to the next row"""
        move = self.gap*(self.row)
        turtle.up()
        turtle.right(180)
        turtle.forward(move)
        turtle.right(90)
        turtle.forward(self.gap)
        turtle.right(90)

    def paint(self):
        """Draws the Hirst Spot Painting"""
        my_turtle = Turtle()
        my_screen = Screen()
        my_screen.colormode(255)
        my_turtle.hideturtle() #hides the turtle
        my_turtle.speed("fastest")

        self.starting_point(my_turtle)
        for x in range(self.column):
            for y in range(self.row):
                pick_color = random.choice(self.color_list)

                #my_turtle.color(pick_color) only the dots are colored and not the turtle
                my_turtle.dot(self.diameter,pick_color)
                my_turtle.up()
                my_turtle.forward(self.gap)
                print(int(my_turtle.xcor()),int(my_turtle.ycor()))
            
            self.next_row(my_turtle)

        my_screen.exitonclick()

if __name__ == "__main__":
    my_painting = Painting()
    my_painting.get_colors()
    my_painting.paint()