class figure_color(object):
    def __init__(self):
        self._color = None

    def getcolor(self):
        return self._color

    def setcolor(self, color):
        self._color = color

    def delcolor(self):
        del self._color

    color = property(getcolor, setcolor, delcolor, "I'm the property.")
