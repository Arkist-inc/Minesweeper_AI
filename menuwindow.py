from tkinter import *
from minesweeper import MineSweeper


class MenuWindow:
    """"
    Het MenuWindow is het hart van de operatie, het stuurt de tkinter window aan en geeft alles weer
    """
    def __init__(self):
        self.frames = {"1psettings": self.create1psettings,
                       "1pgame": self.create1pgame,
                       "mainmenu": self.createmainmenu,
                       "controls": self.createcontrols}

        self.root = Tk()
        self.root.configure(bg="gray")

        self.zoom = 6
        self.images = {"0": PhotoImage(file="sprites/0.png").zoom(self.zoom, self.zoom),
                       "1": PhotoImage(file="sprites/1.png").zoom(self.zoom, self.zoom),
                       "2": PhotoImage(file="sprites/2.png").zoom(self.zoom, self.zoom),
                       "3": PhotoImage(file="sprites/3.png").zoom(self.zoom, self.zoom),
                       "4": PhotoImage(file="sprites/4.png").zoom(self.zoom, self.zoom),
                       "5": PhotoImage(file="sprites/5.png").zoom(self.zoom, self.zoom),
                       "6": PhotoImage(file="sprites/6.png").zoom(self.zoom, self.zoom),
                       "7": PhotoImage(file="sprites/7.png").zoom(self.zoom, self.zoom),
                       "8": PhotoImage(file="sprites/8.png").zoom(self.zoom, self.zoom),
                       "-1": PhotoImage(file="sprites/-1.png").zoom(self.zoom, self.zoom),
                       "flag": PhotoImage(file="sprites/flag.png").zoom(self.zoom, self.zoom),
                       "explosion": PhotoImage(file="sprites/explosion.png").zoom(self.zoom, self.zoom),
                       "closed": PhotoImage(file="sprites/closed.png").zoom(self.zoom, self.zoom),
                       "cross": PhotoImage(file="sprites/cross.png").zoom(self.zoom, self.zoom)}

        self.root.geometry("500x700")
        self.window = self.createmainmenu()
        self.root.mainloop()

    def switchwindow(self, window, *args):
        """
        switched van 1 window naar een andere

        :param window: Frame
            window waar naar geswitched moet worden
        :param args:
            overige argumenten
        """
        self.window.destroy()

        if window == "1pgame":
            self.window = self.create1pgame(*args)
            return
        self.window = self.frames[window]()

    def createmainmenu(self):
        """
        creërt het main menu

        :return: Frame
            de frame van de main menu
        """
        f = Frame(self.root, width=500, height=700, bg="gray")
        f.place(x=0, y=0)
        Label(f, text="Welcome to MineSweeper", bg="darkgray", font=("Times", 30)).place(relx=.5, rely=.1,
                                                                                         anchor='center')
        Button(f, text="Controls", bg="darkgray", font=("Times", 20),
               command=lambda: self.switchwindow("controls")).place(relx=.5, rely=.6, anchor='center')
        Button(f, text="Play on your own", bg="darkgray", font=("Times", 20),
               command=lambda: self.switchwindow("1psettings")).place(relx=.5, rely=.7, anchor='center')
        # oud idee
        # Button(f, text="play versus AI", bg="darkgray", font=("Times", 20),
        #        command=lambda: self.switchwindow("2psettings")).place(relx=.5, rely=.8, anchor='center')
        Button(f, text="quit", bg="darkgray", font=("Times", 10), command=self.root.destroy).place(relx=.05, rely=.97,
                                                                                                   anchor='center')

        return f

    def creategameover(self):
        """
        creeërt het het game over scherm

        :return: Frame
            de frame van het game over scherm
        """

        f = Frame(self.window, width=250, height=350, bg="gray", borderwidth=3, relief="groove")
        Label(f, text="GAME OVER", bg="darkgray", font=("Times", 25)).place(relx=.5, rely=.15, anchor='center')
        b = Label(f, text="go back to main menu", bg="darkgray", font=("Times", 13))
        b.bind("<Button-1>", lambda event, f=f: (self.switchwindow("mainmenu"), f.destroy()))
        b.place(relx=.5, rely=.9, anchor='center')

        Label(f, text=f"Time: {self.ms.timer.get()}s", font=("Times", 25), bg="darkgray").place(relx=.5, rely=.3, anchor='center')
        Label(f, text=f"bombs left: {self.ms.bombcountervar.get()}", font=("Times", 25), bg="darkgray").place(relx=.5, rely=.42, anchor='center')

        self.updateboard()

        f.place(relx=.5, rely=.5, anchor='center')

    def createwin(self):
        """
        creërt het het winst scherm

        :return: Frame
            de frame van het winst scherm
        """
        f = Frame(self.window, width=250, height=350, bg="gray", borderwidth=3, relief="groove")
        Label(f, text="YOU WIN!!!", bg="darkgray", font=("Times", 25)).place(relx=.5, rely=.15, anchor='center')
        b = Label(f, text="go back to main menu", bg="darkgray", font=("Times", 13))
        b.bind("<Button-1>", lambda event, f=f: (self.switchwindow("mainmenu"), f.destroy()))
        b.place(relx=.5, rely=.9, anchor='center')

        Label(f, text=f"Time: {self.ms.timer.get()}s", font=("Times", 25), bg="darkgray").place(relx=.5, rely=.3, anchor='center')

        self.updateboard()

        f.place(relx=.5, rely=.5, anchor='center')

    def create1pgame(self, difficulty, algorithm):
        """
        creërt een single player game met een bepaald algoritme, keuze uit [Human, Simple]

        :param difficulty: str
            de moeilijkheidsgraad van de minesweeper game
        :param algorithm: str
            naam van het algoritme dat gebruikt moet worden
        :return: Frame
            van het bord met de juist instellingen
        """
        difficulties = {"Easy": (10, 10, 10),
                        "Medium": (10, 10, 20),
                        "Hard": (20, 20, 50),
                        "UltraHard": (20, 20, 60),
                        "DEATH": (30, 30, 100)}

        self.ms = MineSweeper(*difficulties[difficulty], method=algorithm)

        return self.createboard()

    def createboard(self):
        """
        Creërt een minesweeper bord

        :return: Frame
            frame van een minesweeper bord
        """
        f = Frame(self.root, width=self.ms.x * 8 * self.zoom, height=self.ms.y * 8 * self.zoom + 100, bg="gray")
        f.place(relx=.5, rely=0, anchor='n')

        yaxis = -1
        self.butboard = []
        boardframe = Canvas(f, width = self.ms.x * 8 * self.zoom, height=self.ms.y * 8 * self.zoom, bg="gray")
        for row in self.ms.board:
            butrow = []
            yaxis += 1
            xaxis = -1
            for cell in row:
                xaxis += 1
                if cell.revealed:
                    Label(boardframe, image=self.images[str(cell.value)], width=8 * self.zoom, height=8 * self.zoom, borderwidth=0).place(x=cell.x * 8 * self.zoom, y=cell.y * 8 * self.zoom)
                else:
                    but = Label(boardframe, image=self.images["closed"], borderwidth=0)
                    but.place(x=cell.x * 8 * self.zoom, y=cell.y * 8 * self.zoom)

                    if self.ms.method == "Human":
                        but.bind("<Button-1>", lambda event, x=xaxis, y=yaxis: self.play(x, y, False))
                        but.bind("<Button-2>", lambda event, x=xaxis, y=yaxis: self.play(x, y, True))
                        but.bind("<Button-3>", lambda event, x=xaxis, y=yaxis: self.play(x, y, True))
                    butrow.append(but)

            self.butboard.append(butrow)

        boardframe.place(relx=0.5, rely=.15, anchor='n')

        self.bombcounter = StringVar(value=f"{self.ms.bombcountervar}")
        Label(f, textvariable=self.ms.bombcountervar, borderwidth=0, font=("times", 30), bg="gray").place(relx=.1, rely=.1, anchor='center')

        # self.timer = StringVar(value=f"{self.ms.timer}")
        Label(f, textvariable=self.ms.timer, borderwidth=0, font=("times", 30), bg="gray").place(relx=.9, rely=.1, anchor='center')

        if self.ms.method == "Human":
            start = self.ms.calculatestartingpoint()
            l = Label(boardframe, image=self.images["cross"], borderwidth=0)
            l.place(x=start[0] * 8 * self.zoom, y=start[1] * 8 * self.zoom)
            l.bind("<Button-1>", lambda event, x=start[0], y=start[1]: (self.play(x, y, False), l.destroy()))

        if not self.ms.method == "Human":
            self.root.after(1, self.continueslyupdateboard)

        self.drawnboard = [[(y.revealed, y.flagged) for y in x] for x in self.ms.getuserboard()]

        return f

    def play(self, x=0, y=0, flag=False):
        """
        de buttons komen bij deze functie uit om input te geven aan het minesweeper object en om game eindes
        te regelen

        :param x: int
            x coordinaat van de cell
        :param y: int
            y coordinaat van de cell
        :param flag: bool
            of het cell een vlag is of niet
        """
        guess = self.ms.input(x, y, flag)
        if guess == 1:
            self.updateboard()

        elif guess == 0:
            self.disablebuttons()
            self.creategameover()
            return

        elif guess == 2:
            self.disablebuttons()
            self.createwin()

        if flag:
            self.ms.updatebombcounter()

    # oud idee
    # def create2pgame(self):
    #     pass

    def create1psettings(self):
        f = Frame(self.root, width=500, height=700, bg="gray")
        f.place(x=0, y=0)

        Label(f, text="Settings", bg="darkgray", font=("Times", 30)).place(relx=.5, rely=.05, anchor='center')

        Label(f, text="Difficulty:", bg="darkgray", font=("Times", 20)).place(relx=.05, rely=.2, anchor='w')
        options = ["Easy", "Medium", "Hard", "UltraHard", "DEATH"]
        s = StringVar()
        s.set(options[0])
        o = OptionMenu(f, s, *options)
        o.config(bg="darkgray", fg="black", font=("Times", 15), highlightthickness=0)
        o.place(relx=.05, rely=.26, anchor='w')


        Label(f, text="Algorithm:", bg="darkgray", font=("Times", 20)).place(relx=.05, rely=.4, anchor='w')
        algorithms = ["Human", "Simple"]
        algorithm = StringVar()
        algorithm.set(algorithms[0])
        option = OptionMenu(f, algorithm, *algorithms)
        option.config(bg="darkgray", fg="black", font=("Times", 15), highlightthickness=0)
        option.place(relx=.05, rely=.46, anchor='w')


        Button(f, text="Start the game!", bg="darkgray", font=("Times", 30), command=lambda: self.switchwindow("1pgame", s.get(), algorithm.get())).place(relx=.5, rely=.9, anchor='center')
        Button(f, text="Back", bg="darkgray", font=("Times", 10), command=lambda: self.switchwindow("mainmenu")).place(
            relx=.05, rely=.97, anchor='center')

        return f

    # oud idee
    # def create2psettings(self):
    #     f = self.create1psettings()
    #
    #     Label(f, text="Algorithm:", bg="darkgray", font=("Times", 20)).place(relx=.05, rely=.35, anchor='w')
    #     options = ["simple algorithm"]
    #     s = StringVar()
    #     s.set(options[0])
    #     o2 = OptionMenu(f, s, *options)
    #     o2.config(bg="darkgray", fg="black", font=("Times", 15), highlightthickness=0)
    #     o2.place(relx=.05, rely=.41, anchor='w')
    #
    #     return f

    def createcontrols(self):
        """
        creërt de controls tab voor de applicatie
        :return: Frame
            frame van de control pagina
        """
        f = Frame(self.root, width=500, height=700, bg="gray")
        f.place(x=0, y=0)

        Label(f, text="Controls", bg="darkgray", font=("Times", 30)).place(relx=.5, rely=.05, anchor='center')

        Button(f, text="Back", bg="darkgray", font=("Times", 10), command=lambda: self.switchwindow("mainmenu")).place(
            relx=.05, rely=.97, anchor='center')

        return f

    def updateboard(self):
        """
        update het minesweeper bord op basis van welke vlakken er zijn veranderd
        """
        if not self.ms.gamestate:
            return

        board = self.ms.getuserboard()
        for y in range(self.ms.y):
            for x in range(self.ms.x):
                if self.drawnboard[y][x][0] != board[y][x].revealed:
                    self.butboard[y][x].configure(image=self.images[str(board[y][x].value)])
                    continue

                if board[y][x].flagged:
                    temp = self.butboard[y][x]
                    temp.configure(image=self.images["flag"])
                    temp.bind("<Button-3>", lambda event, x=x, y=y : self.play(x, y, True))
                else:
                    self.butboard[y][x].configure(image=self.images["closed"])

    def disablebuttons(self):
        """
        disabled alle buttons van minesweeper zodat je niet meer kan spelen als de game over is
        """
        for row in self.butboard:
            for but in row:
                but.unbind('<Button 1>')
                but.unbind('<Button 2>')
                but.unbind('<Button 3>')

    def continueslyupdateboard(self):
        """
        zorgt ervoor dat het bord heel de teid wordt geupdate
        """
        self.updateboard()
        guess = self.ms.input()
        if guess == 0:
            self.createwin()
            return
        elif guess == 2:
            self.creategameover()
            return
        self.root.after(100, self.continueslyupdateboard)

