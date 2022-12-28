from lab_python_oop.figure import geometric_figure
from lab_python_oop.color import color_figure

class rectangle(geometric_figure):

    figure_type = "Прямоугольник "
    @classmethod
    def get_figure_type(t):
        return t.figure_type
    
    def __init__(self, w, h, c):
        self.width = w
        self.height = h
        self.fcolor = color_figure()
        self.fcolor.get_color = c

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return '{}{} цвета шириной {} и высотой {} площадью {}'.format(
            rectangle.get_figure_type(),self.fcolor.get_color,
            self.height, self.width, self.square())
        
        
        

