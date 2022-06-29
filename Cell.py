class Cell:
    """
    1 cell van het minesweeper bordt
    """
    def __init__(self, x, y, neighbours=None, revealed=False, value=None):
        """
        :param x: int
            het x coordinaat van de cel
        :param y: int
            het y coordinaat van de cel
        :param neighbours: lst
            de omliggende cellen van cel
        :param revealed: bool
            of het cel als ondekt is
        :param value: int
            hoeveel bommen eromheenliggen of of het een bom is
        """
        self.value = value
        self.x = x
        self.y = y
        self.revealed = revealed
        self.neighbours = neighbours
        self.flagged = False

    def setvalue(self, value):
        """
        past de value van een cel aan

        :param value: int
            value van de cel
        """
        self.value = value

    def reveal(self, revealzero=True):
        """
        'klikt' de cel aan

        :param revealzero: bool
            of de cel alles eromheen moet revealen als er geen bommen omheenliggen
        :return:
            de value als hij gerevealt wordt
        """
        if self.revealed:
            return

        self.revealed = True
        if revealzero:
            if self.value == 0:
                for cell in self.neighbours:
                    cell.reveal()
        return self.value

    def setneighbours(self, neighbours):
        """
        past de omliggende cellen aan

        :param neighbours: lst
            een lijst van cellen
        """
        self.neighbours = neighbours

    def flag(self):
        """
        'flagged' een cel als hij nog niet geflagged is
        """
        if self.revealed:
            return

        if self.flagged:
            self.flagged = False
        else:
            self.flagged = True

    def zeroarea(self, zeroes=[]):
        """
        calculeert het aantal nullen in een gebied, wordt gebruikt om een goede startplaats uit te rekenen

        :param zeroes: lst
            lijst van cellen met value 0
        :return: lst
            als hij er nog niet in zit dan returnt hij een lst van cellen
        """
        if self in zeroes:
            return
        if self.value == 0:
            zeroes.append(self)
            for x in self.neighbours:
                x.zeroarea(zeroes)

            return zeroes
