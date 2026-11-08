#TACHAWUT HIRUNBURANA 6810545581


"""Our own Square class: an object that uses a Turtle object to draw."""
import turtle
import time


class Square:
    def __init__(self, x, y, size, color):
        if size <= 0:
            raise ValueError("size must be positive")
        self._x = x
        self._y = y
        self._size = size
        self._color = color
        self._pen = turtle.Turtle()
        self._pen.hideturtle()
        self._pen.speed(0)


    def draw(self):
        """Draw the square with (x, y) as its lower-left corner."""
        self._pen.penup()
        self._pen.goto(self._x, self._y)
        self._pen.setheading(0)
        self._pen.pencolor(self._color)
        self._pen.pendown()
        for _ in range(4):
            self._pen.forward(self._size)
            self._pen.left(90)
        self._pen.penup()


    def move_to(self, x, y):
        """Erase this square's old drawing, then redraw at (x, y)."""
        self._x = x
        self._y = y
        self._pen.clear()
        self.draw()


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        if sides < 3 or side_length <= 0 or pen_size <= 0:
            raise ValueError()


        self._x = x
        self._y = y
        self._pen_size = pen_size
        self._angle = angle
        self._sides = sides
        self._side_length = side_length
        self._color = color
        self._pen = turtle.Turtle()
        self._pen.hideturtle()
        self._pen.speed(0)


    def draw(self):
        """Draw the polygon with (x, y) as its first point."""
        self._pen.penup()
        self._pen.goto(self._x, self._y)
        self._pen.setheading(self._angle)
        self._pen.pencolor(self._color)
        self._pen.pensize(self._pen_size)
        self._pen.pendown()
        for _ in range(self._sides):
            self._pen.forward(self._side_length)
            self._pen.left(360 / self._sides)
        self._pen.penup()


    def move_to(self, x, y):
        """Erase this polygon's old drawing, then redraw at (x, y)."""
        self._x = x
        self._y = y
        self._pen.clear()
        self.draw()


# class Triangle:
#     def __init__(self, x, y, size, color):
#         if size <= 0:
#             raise ValueError("size must be positive")
#         self._x = x
#         self._y = y
#         self._size = size
#         self._color = color
#         self._pen = turtle.Turtle()
#         self._pen.hideturtle()
#         self._pen.speed(0)


#     def draw(self):
#         """Draw the square with (x, y) as its lower-left corner."""
#         self._pen.penup()
#         self._pen.goto(self._x, self._y)
#         self._pen.setheading(0)
#         self._pen.pencolor(self._color)
#         self._pen.pendown()
#         for _ in range(3):
#             self._pen.forward(self._size)
#             self._pen.left(180//3)
#         self._pen.penup()


#     def move_to(self, x, y):
#         """Erase this square's old drawing, then redraw at (x, y)."""
#         self._x = x
#         self._y = y
#         self._pen.clear()
#         self.draw()


# class Hexagon:
#     def __init__(self, x, y, size, color):
#         if size <= 0:
#             raise ValueError("size must be positive")
#         self._x = x
#         self._y = y
#         self._size = size
#         self._color = color
#         self._pen = turtle.Turtle()
#         self._pen.hideturtle()
#         self._pen.speed(0)


#     def draw(self):
#         """Draw the square with (x, y) as its lower-left corner."""
#         self._pen.penup()
#         self._pen.goto(self._x, self._y)
#         self._pen.setheading(0)
#         self._pen.pencolor(self._color)
#         self._pen.pendown()
#         for _ in range(4):
#             self._pen.forward(self._size)
#             self._pen.left(360//5)
#         self._pen.penup()


#     def move_to(self, x, y):
#         """Erase this square's old drawing, then redraw at (x, y)."""
#         self._x = x
#         self._y = y
#         self._pen.clear()
#         self.draw()