#TACHAWUT HIRUNBURANA 6810545581


"""Example 4: Make and move objects of our own Square class."""
import turtle
from square_shape_diy import Polygon
import random
import time

#init
screen = turtle.Screen()
screen.title("Static One")
screen.bgcolor("black")

screen.tracer(0)

def find_color(n):
    if n == 1:
        return "red"
    elif n == 2:
        return "orange"
    elif n == 3:
        return "yellow"
    elif n == 4:
        return "green"
    elif n == 5:
        return "cyan"
    elif n == 6:
        return "blue"
    elif n == 7:
        return "purple"
    elif n == 8:
        return "gray"

anim_polygons = []

#at least 15 Polygon, note
for _ in range(22):
    sides = random.randint(3, 7)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    side_length = random.randint(40, 100)
    color = find_color(sides)
    pen_size = random.randint(1, 8)
    angle = random.randint(0, 360)
#fill
    p = Polygon(x, y, sides, side_length, color, pen_size, angle)
    p.draw()
    anim_polygons.append(p)

screen.update()
screen.mainloop()