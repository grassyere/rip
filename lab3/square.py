from lab_python_oop.rectangle import rectangle

class square(rectangle):
    def __init__(self, a, color):
        super().__init__(a, a, color)

        self.figure_name = "Square"

    def rep(self):
        print(self.figure_name)
        print('Side: {}, Color: {}, Area: {}'.format(self.width, self.clr.getcolor(), self.area()))