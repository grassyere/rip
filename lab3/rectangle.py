from lab_python_oop.geometric_figure import geometric_figure
from lab_python_oop.figure_color import figure_color

class rectangle(geometric_figure):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width

        self.clr = figure_color()
        self.clr.setcolor(color)

        self.figure_name = "Rectangle"

    def area(self):
        return self.width * self.height

    def repr(self):
        print(self.figure_name)
        print('Width: {}, Height: {}, Color: {}, Area: {}'.format(self.width, self.height, self.clr.getcolor(), self.area()))



