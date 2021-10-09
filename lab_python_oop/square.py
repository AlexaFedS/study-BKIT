from rectangle import rectangle

class square(rectangle):
    FIGURE_TYPE = "Квадрат"

    def get_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, side):
        self.side = side
        super().__init__(self.side, self.side, color)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            self.get_type(),
            self.clr.get_color(),
            self.side,
            self.square()
        )