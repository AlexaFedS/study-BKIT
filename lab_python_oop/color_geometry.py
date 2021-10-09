class color_geometry:
    def __init__(self):
        self._color = None

    def get_color(self):
        return self._color

    def change_color(self, value):
        self._color = value

    def del_color(self):
        del self._color