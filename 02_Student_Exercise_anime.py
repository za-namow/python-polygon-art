#TACHAWUT HIRUNBURANA 6810545581

"""Example 4: Make and move objects of our own Square class."""
import turtle
from square_shape_diy import Square, Polygon
import random
import time

random_n1 = random.randint(3,10) #from triangle to decagon
random_n2 = random.randint(3,10) #from triangle to decagon
random_n3 = random.randint(3,10) #from triangle to decagon
random_n4 = random.randint(3,10) #from triangle to decagon


def find_color(n):
    if n == 3 or n == 11:
        return "red"
    elif n == 4:
        return "orange"
    elif n == 5:
        return "yellow"
    elif n == 6:
        return "green"
    elif n == 7:
        return "cyan"
    elif n == 8:
        return "blue"
    elif n == 9:
        return "purple"
    elif n == 10:
        return "gray"

yn = input("do you wanna pick pen size, if not, this code will randomize for you: (Y/N) ")
if yn == "Y":
    n = int(input("(3-10)>>> "))
    random_n1d = n
    random_n2d = n
    random_n3d = n
    random_n4d = n

elif yn == "N":
    random_n1d = random_n1
    random_n2d = random_n2
    random_n3d = random_n3
    random_n4d = random_n4

screen = turtle.Screen()
screen.title("My Own Happy Homework - Kudos to all Ajarns, I love this work")

small_s = Square(-170, -60, 70, "green")
large_s = Square(40, -60, 120, "orange")
small_s.draw()
large_s.draw()

#new ver.
small_ss = Polygon(-30, 0, 4, 70, "green")
large_ss = Polygon(-55, -25, 4, 120, "orange")
small_greens = Polygon(-30, -70, 4, 70, "green")
small_iin = Polygon(-30, 210, 4, 70, "green")
small_iis = Polygon(-30, -210, 4, 70, "green")




# This changes only the small square's drawing.
small_s.move_to(-100, 50)
large_s.move_to(-170, -100)
small_s.move_to(80, 60)
large_s.move_to(-155, 80)
small_s.move_to(-30, 0)
large_s.move_to(-55, -25)


small_ss.draw()
large_ss.draw()
small_s.move_to(1000,1000)


small_ss.move_to(-30,70)
small_greens.draw()
small_ss.move_to(-30,140)
small_greens.move_to(-30,-140)
small_iin.draw()
small_iis.draw()
small_iin.move_to(-30,280)
small_iis.move_to(-30,-280)

large_s.move_to(1000,1000)

screen.bgcolor("black")

screen.tracer(0)

#after black
anim_polygons = [
    Polygon(-30, 280, random_n1, 70, find_color(random_n1), random_n1d),
    Polygon(-30, 140, random_n2, 70, find_color(random_n2), random_n2d),
    Polygon(-28, -25, 5, 80, "orange", max(1, random_n1-1)),
    Polygon(-30, -140, random_n3, 70, find_color(random_n3), random_n3d),
    Polygon(-30, -280, random_n4, 70, find_color(random_n4), random_n4d),
    Polygon(50, 100, 3, 60, "red", 2),
    Polygon(-100, 100, 6, 50, "cyan", 3),
    Polygon(100, -100, 8, 40, "purple", 2)
]


#init
for p in anim_polygons:
    p.draw()


# at least 60 frames
for frame in range(70):
    for i, p in enumerate(anim_polygons):
        new_x = p._x + (i + 1) % 3 - 1
        new_y = p._y + ((frame + i) % 5) - 2
        p.move_to(new_x, new_y)


    screen.update()
    time.sleep(0.03)

screen.mainloop()