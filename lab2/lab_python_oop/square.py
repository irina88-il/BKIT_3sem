from lab_python_oop.rectangle import rectangle

class sq(rectangle):
    
    figure_type = "Квадрат"
    @classmethod
    def get_figure_type(t):
        return t.figure_type

    def __init__(self, s, c):
        self.side = s;
        super().__init__(self.side, self.side, c)


    def __repr__(self):
        return '{} {} цвета стороной {} и площадью {}'.format(
            sq.get_figure_type(),
            self.fcolor.get_color, self.side, self.square())
        
    
