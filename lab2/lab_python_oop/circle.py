from lab_python_oop.figure import geometric_figure
from lab_python_oop.color import color_figure

import math

class circle(geometric_figure):
    
    figure_type = "Круг"
    @classmethod
    def get_figure_type(t):
        return t.figure_type

    def __init__(self, r, c):
        self.radius = r;
        self.fcolor = color_figure()
        self.fcolor.get_color = c

    def square(self):
        return math.pi * (self.radius**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} и площадью {}'.format(circle.get_figure_type(),
            self.fcolor.get_color, self.radius, self.square())
                                                             
                                                             
    
    
