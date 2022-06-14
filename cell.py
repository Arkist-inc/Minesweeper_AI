class Cell:
    def __init__(self, x, y, value=None):
        self.value = value
        self.x = x
        self.y = y

    def setvalue(self, value):
        self.value = value
