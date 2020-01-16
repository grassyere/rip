from lab_python_oop.geometric_figure import geometric_figure
from lab_python_oop.figure_color import figure_color
from math import pi

class circle(geometric_figure):
    def __init__(self, rad, color):
        self.rad = rad
        self.clr = figure_color()
        self.clr.setcolor(color)
        self.figure_name = "Circle"

    def area(self):
        return pi * self.rad ** 2

    def repr(self):
        print(self.figure_name)
        print('Radius: {}, Color: {}, Area: {}'.format(self.rad, self.clr.getcolor(), self.area()))
