"""EXERCISE: finish the Polygon class. Use import turtle (not selective imports)."""
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        if sides < 3:
            raise ValueError("sides must be atleast 3")
        if side_length <= 0:
            raise ValueError("side_length must be positive")
        if pen_size <= 0:
            raise ValueError("pen_size must be positive")

        self._x = x
        self._y = y
        self._sides = sides
        self._side_length = side_length
        self._color = color
        self._pen_size = pen_size
        self._angle = angle
        self._pen = turtle.Turtle()
        self._pen.hideturtle()
        self._pen.speed(0)
        self._pen.penup()

    def draw(self):
        pen = self._pen
        pen.penup()
        pen.goto(self._x, self._y)
        pen.setheading(self._angle)
        pen.color(self._color)
        pen.pensize(self._pen_size)
        pen.pendown()
        turn = 360 / self._sides
        for _ in range(self._sides):
            pen.forward(self._side_length)
            pen.left(turn)
        pen.penup()

    def move_to(self, x, y):
        self._x = x
        self._y = y
        self._pen.clear()
        self.draw()
