class color_figure():
    
    def __init__(self):
        self._color = None

    @property
    def get_color(self):
        return self._color

    @get_color.setter
    def get_color(self, value):
        self._color = value

    
