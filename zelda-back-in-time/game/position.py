class Position:
    def __init__(self, x, y):
        self._x = x

        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, value):
        self._x = value

    def set_y(self, value):
        self._y = value