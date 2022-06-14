class Cell:
    def __init__(self, x, y, revealed=False, value=None):
        self.value = value
        self.x = x
        self.y = y
        self.revealed = revealed

    def setvalue(self, value):
        self.value = value

    def reveal(self):
        self.revealed = True
        return self.value
