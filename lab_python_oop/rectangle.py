from lab_python_oop.color_geometry import color_geometry
from lab_python_oop.abc_class import geometry_figure

class rectangle(geometry_figure):
    FIGURE_TYPE = "Прямоугольник"

    def get_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.clr = color_geometry()
        self.clr.change_color(color)

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            self.get_type(),
            self.clr.get_color(),
            self.width,
            self.height,
            self.square()
        )