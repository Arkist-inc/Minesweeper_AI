from random import randint
from cell import Cell

class MineSweeper:
    def __init__(self, x, y, bombs):
        self.x = x
        self.y = y
        self.bombcount = bombs

        self.board = self.generateboard()
        self.placebombs()
        self.placenumbers()

    def generateboard(self):
        eboard = [[Cell(i, j, 0) for i in range(0, self.x)]for j in range(0, self.y)]

        return eboard

    def placebombs(self):
        bombpositions = [[i, j] for j in range(0, self.y) for i in range(0, self.x)]
        for i in range(0, self.bombcount):
            pos = bombpositions[randint(0, len(bombpositions))]
            # print("Placing a bomb at: ", pos)
            self.placebomb(pos[0], pos[1])

    def placebomb(self, x, y):
        if x <= self.x and y <= self.y:
            self.board[y][x].setvalue(-1)

    def placenumbers(self):
        for row in self.board:
            for cell in row:
                if cell.value == -1:
                    continue

                surroundings = self.surroundingcells(cell=cell)
                cell.setvalue(self.countbombs(surroundings))

    def surroundingcells(self, pos=None, cell=None):
        if cell:
            x = cell.x
            y = cell.y
        else:
            x = pos[0]
            y = pos[1]

        xs = [x - 1, x, x + 1]
        ys = [y - 1, y, y + 1]

        surroundings = []

        for i in xs:
            if not 0 <= i < self.x:
                continue
            for j in ys:
                if not 0 <= j < self.y or (i == x and j == y):
                    continue

                # print("appending cell:", j, i)
                surroundings.append(self.board[j][i])

        return surroundings

    def countbombs(self, lst):
        bombcount = 0
        for cell in lst:
            if cell.value == -1:
                bombcount += 1

        return bombcount

    def printboard(self):
        for row in self.board:
            for cell in row:
                print(cell.value, end='')
            print('\n')
