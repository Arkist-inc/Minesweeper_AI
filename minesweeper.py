from random import randint
from cell import Cell
from threading import Thread
import time
from tkinter import StringVar


class MineSweeper:
    """
    De MineSweeper class is het hart van het programma,
    Het maakt een bord aan, er kan input gegeven worden,
    kortom, je kunt een volledige minesweeper game spelen
    """
    def __init__(self, x, y, bombs, method="human", delay=0):
        """
        init functie van MineSweeper Class

        :param x: int
            hoeveel vakjes er op de x axis komen
        :param y:
            hoeveel vakjes er op de y axis komen
        :param bombs:
            hoeveel bommen er worden gesplaatst
        :param method:
            Welke methode er wordt gebruikt om het bord op te lossen
            kan gekozen worden uit [human, simple]
        :param delay:
            Hoelange pauze het algoritme neemt voor elke zet
        """

        self.x = x
        self.y = y
        self.bombcount = bombs
        self.method = method
        self.gamestate = True
        self.board = self.generateboard()
        self.timer = StringVar(value="0")
        self.bombcountervar = StringVar(value=str(self.bombcount))
        self.delay = delay

        self.placebombs()
        self.placenumbers()
        self.setneighbours()

        # AI variable
        self.cells = set()
        self.lastcells = set()
        self.bomblist = set()
        # self.clicklist = set()

        Thread(target=self.incrementcounter).start()

    def input(self, x=0, y=0, flag=False, revealzero=True):
        """
        :param x: int
            het x coördinaat van de cel die aangeklikt moet worden
        :param y: int
            het y coördinaat van de cel die aangeklikt moet worden
        :param flag: bool
            of de cel die aangeklikt moet worden een vlag moet krijgen of niet,
            True voor een vlag
            False voor geen vlag
        :param revealzero: bool
            of de cel die aangeklikt wordt als hij een waarde heeft van 0 (er zitten geen bommen omheen) de cellen
            eromheen moet weergeven
        :return: int
            returnt of je hebt verloren, gewonnen of dat het spel nog gaande is
        """
        if self.method == 'Simple':
            return self.simpleguess()

        # print(x, y, flag)

        if flag:
            self.board[y][x].flag()
            return 1

        if self.board[y][x].reveal(revealzero) == -1:
            self.gameover()
            print("You lost")
            return 0

        if self.checkwin():
            print("YOU WIN!!!")
            return 2

        return 1

    def gameover(self):
        """
        als de game over is revealt deze functie alle cellen
        """
        self.gamestate = False
        for row in self.board:
            for cell in row:
                cell.reveal()

    def checkwin(self):
        """
        Checkt of alle cellen die geen bommen zijn zijn gerevealed
        """
        for row in self.board:
            for cell in row:
                if not cell.revealed and not cell.value == -1:
                    return 0
        self.gamestate = False
        return 1

    def generateboard(self):
        """
        Maakt de cellen van het bordt aan

        :return:
            een 2 dimensionale list met de cellen
        """
        eboard = [[Cell(i, j, value=0) for i in range(0, self.x)]for j in range(0, self.y)]

        return eboard

    def placebombs(self):
        """
        Plaatst de bommen in het bord

        :return:
            niets
        """
        bombpositions = [[i, j] for j in range(0, self.y) for i in range(0, self.x)]
        for i in range(0, self.bombcount):
            r = randint(0, len(bombpositions) - 1)
            pos = bombpositions[r]
            bombpositions.remove(bombpositions[r])
            self.placebomb(pos[0], pos[1])

    def placebomb(self, x, y):
        """
        Plaatst een cel op het bord

        :param x: int
            x coördinaat van het cel
        :param y: int
            y coördinaat van het cel
        """
        if x <= self.x and y <= self.y:
            self.board[y][x].setvalue(-1)

    def placenumbers(self):
        """
        wijst de juiste nummers aan de cellen op basis van de bommen die eromheenliggen
        """
        for row in self.board:
            for cell in row:
                if cell.value == -1:
                    continue

                surroundings = self.surroundingcells(cell=cell)
                cell.setvalue(self.countbombs(surroundings))

    def setneighbours(self):
        """
        Wijst de juist buurmannen aan aan een cel
        """
        for row in self.board:
            for cell in row:
                cell.setneighbours(self.surroundingcells(cell=cell))

    def surroundingcells(self, pos=None, cell=None):
        """
        Kijkt welke cellen erom een cel heen liggen

        :param pos: list[2]
            de positie van een cel
        :param cell: Cell
            een cell
        :return:
        """
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

    def getuserboard(self):
        """
        haalt het gebruikersbord op en returnt het

        :return: list
            het bord van minesweeper
        """
        userboard = []
        for row in self.board:
            userrow = []
            for cell in row:
                userrow.append(cell)
            userboard.append(userrow)

        return userboard

    def calculatestartingpoint(self):
        """
        rekent het beste startpunt uit voor een minesweeper game

        :return: Cell
            returnt de Cell dat de beste startpositie is
        """
        potential = []

        for row in self.board:
            for cell in row:
                if cell in [y for x in potential for y in x]:
                    continue
                if cell.value != 0:
                    continue
                potential.append(cell.zeroarea(zeroes=[]))

        big = [None, 0]
        for x in potential:
            if len(x) > big[1]:
                big[1] = len(x)
                big[0] = x

        choice = big[0][randint(0, len(big))]
        return choice.x, choice.y



    def countbombs(self, lst):
        """
        telt hoeveel bommen er in een lijst van cellen zit

        :param lst: list
            lijst van cellen
        :return: int
            aantal bommen in de lijst
        """
        bombcount = 0
        for cell in lst:
            if cell.value == -1:
                bombcount += 1

        return bombcount

    def printboard(self):
        """
        Print het bord op een leesbare manier uit
        """
        for row in self.board:
            for cell in row:
                print(cell.value, end='')
            print('\n')

    def printuserboard(self):
        """
        Print het bord dat de gebruiker ziet op een leesbare manier uit
        """
        for row in self.getuserboard():
            print(row)

    def incrementcounter(self):
        """
        Increments de timer van de minesweeper game
        """
        if self.gamestate:
            self.timer.set(f"{round(float(self.timer.get()) + 0.1, 1)}")
            time.sleep(0.1)
            self.incrementcounter()
        else:
            return

    def countflag(self):
        """
        telt alle vlaggen op

        :return: int
            amount of flags
        """
        i = 0
        for row in self.board:
            for cell in row:
                if cell.flagged:
                    i += 1

        return i

    def updatebombcounter(self):
        """
        Updates de bomb counter van de minesweeper game
        """
        self.bombcountervar.set(str(self.bombcount - self.countflag()))

    def simpleguess(self):
        """
        Minesweeper Algorithm gebasseerd op het algoritme beschreven in pagina 20 van
        https://dash.harvard.edu/bitstream/handle/1/14398552/BECERRA-SENIORTHESIS-2015.pdf


        :return: int
            gebasseerd op een winst of een verlies
        """
        self.updatebombcounter()
        # if self.bomblist:
        #     bomb = self.bomblist.pop()
        #     return [True, bomb.x, bomb.y]
        #
        # if self.clicklist:
        #     print(self.clicklist)
        #     click = self.clicklist.pop()
        #     return [False, click.x, click.y]

        if self.gamestate:
            if not self.cells:
                startingpoint = self.calculatestartingpoint()
                self.cells.add(self.board[startingpoint[1]][startingpoint[0]])

            if self.cells == self.lastcells:
                rand = self.randomguess()
                # print("adding", rand.x, rand.y)
                self.cells.add(rand)

            self.lastcells = self.cells.copy()

            for c in self.cells.copy():
                if c in self.bomblist:
                    self.cells.remove(c)
                    continue

                if self.input(c.x, c.y, False, False) == 0:
                    return

                if not self.gamestate:
                    if self.checkwin():
                        return 2
                    return 0

                if self.isAFN(c):
                    # print("AFN on", c.x, c.y)
                    for x in c.neighbours:
                        if not x.revealed:
                            self.cells.add(x)
                    self.cells.remove(c)
                    break

                elif self.isAMN(c):
                    # print("AMN")
                    for x in c.neighbours:
                        if not x.revealed:
                            self.bomblist.add(x)
                            self.input(x.x, x.y, True, False)
                    self.cells.remove(c)

                # if self.clicklist:
                #     print(self.clicklist)
                #     guess = self.clicklist.pop()
                #     return [False, guess.x, guess.y]
                #
                # if self.bomblist:
                #     print(self.bomblist)
                #     guess = self.bomblist.pop()
                #     return [True, guess.x, guess.y]

            # randomguess = self.randomguess()
            # self.cells.append(randomguess)

    def randomguess(self):
        """
        kiest een willekeurige cell op het bord

        :return: Cell
            willekeurige cel op het bord
        """
        guesses = []
        for row in self.board:
            for cell in row:
                if not cell.revealed:
                    guesses.append(cell)

        # print([[x.x, x.y] for x in guesses])
        return guesses[randint(0, len(guesses) - 1)]

    def isAFN(self, cell):
        """
        All Free Neighbours kijkt of het aantal bommen voldaan is, dus als een cel de value heeft van 1 en er ligt 1 bom
        omheen dan is deze conditie voldaan

        :param cell: Cell
            Welke cell er naar gekeken moet worden
        :return:
            of de conditie is voldaan
        """
        # all free neighbours
        bombs = 0
        for x in cell.neighbours:
            if x.flagged:
                bombs += 1

        return True if bombs == cell.value else False

    def isAMN(self, cell):
        """All Marked Neighbours kijkt of het aantal dichte cellen + aantal vlaggen gelijk is aan de waarde van de cel

        :param cell: Cell
            welke cell er naar gekeken moet worden
        :return:
            of de conditie is voldaan
        """
        # all marked neighbours
        cells = 0
        for x in cell.neighbours:
            if not x.revealed or x.flagged:
                cells += 1

        return True if cells == cell.value else False
