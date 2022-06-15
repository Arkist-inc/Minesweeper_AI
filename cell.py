class Cell:
    def __init__(self, x, y, neighbours=None, revealed=False, value=None):
        self.value = value
        self.x = x
        self.y = y
        self.revealed = revealed
        self.neighbours = neighbours
        self.flagged = False

    def setvalue(self, value):
        self.value = value

    def reveal(self):
        if self.revealed:
            return

        self.revealed = True
        if self.value == 0:
            for cell in self.neighbours:
                cell.reveal()
        return self.value

    def setneighbours(self, neighbours):
        self.neighbours = neighbours

    def flag(self):
        if self.revealed:
            return

        if self.flagged:
            self.flagged = False
        else:
            self.flagged = True

    def zeroarea(self, zeroes=[]):
        if self in zeroes:
            return
        if self.value == 0:
            zeroes.append(self)
            for x in self.neighbours:
                x.zeroarea(zeroes)

            print(zeroes)
            return zeroes
