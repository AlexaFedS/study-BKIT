import math

from lab_python_oop.abc_class import geometry_figure
from lab_python_oop.color_geometry import color_geometry

class circle(geometry_figure):

    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        self.rad = radius
        self.color = color_geometry()
        self.color.change_color(color)

    def get_type(self):
        return self.FIGURE_TYPE

    def square(self):
        return self.rad * self.rad * math.pi

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            self.get_type(),
            self.color.get_color(),
            self.rad,
            self.square()
        )