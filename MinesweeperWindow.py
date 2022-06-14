from tkinter import *
from minesweeper import MineSweeper


class MinesweeperWindow:

    def __init__(self):
        self.frames = {"1psettings": self.create1psettings,
                       "2psettings": self.create2psettings,
                       "1pgame": self.create1pgame,
                       "2pgame": self.create2pgame,
                       "mainmenu": self.createmainmenu,
                       "controls": self.createcontrols}

        self.root = Tk()
        self.root.geometry("500x700")
        self.window = self.createmainmenu()
        self.root.mainloop()

    def switchwindow(self, window, *args):
        self.window.destroy()
        self.window = self.frames[window]()

    def createmainmenu(self):
        f = Frame(self.root, width=500, height=700, bg="gray")
        f.place(x=0, y=0)
        Label(f, text="Welcome to MineSweeper", bg="darkgray", font=("Times", 30)).place(relx=.5, rely=.1,
                                                                                         anchor='center')
        Button(f, text="Controls", bg="darkgray", font=("Times", 20),
               command=lambda: self.switchwindow("controls")).place(relx=.5, rely=.6, anchor='center')
        Button(f, text="Play on your own", bg="darkgray", font=("Times", 20),
               command=lambda: self.switchwindow("1psettings")).place(relx=.5, rely=.7, anchor='center')
        Button(f, text="play versus AI", bg="darkgray", font=("Times", 20),
               command=lambda: self.switchwindow("2psettings")).place(relx=.5, rely=.8, anchor='center')
        Button(f, text="quit", bg="darkgray", font=("Times", 10), command=self.root.destroy).place(relx=.05, rely=.97,
                                                                                                   anchor='center')

        return f

    def create1pgame(self):
        board = MineSweeper(10, 10, 20)

        self.createboard(board)

    def createboard(self, board):
        userboard = board.getuserboard()
        for row in board:
            for value in row:


    def create2pgame(self):
        pass

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

        Button(f, text="Start the game!", bg="darkgray", font=("Times", 30), command=lambda: self.switchwindow("1pgame")).place(relx=.5, rely=.9,
                                                                                   anchor='center')
        Button(f, text="Back", bg="darkgray", font=("Times", 10), command=lambda: self.switchwindow("mainmenu")).place(
            relx=.05, rely=.97, anchor='center')

        return f

    def create2psettings(self):
        f = self.create1psettings()

        Label(f, text="Algorithm:", bg="darkgray", font=("Times", 20)).place(relx=.05, rely=.35, anchor='w')
        options = ["simple algorithm"]
        s = StringVar()
        s.set(options[0])
        o2 = OptionMenu(f, s, *options)
        o2.config(bg="darkgray", fg="black", font=("Times", 15), highlightthickness=0)
        o2.place(relx=.05, rely=.41, anchor='w')

        return f

    def createcontrols(self):
        f = Frame(self.root, width=500, height=700, bg="gray")
        f.place(x=0, y=0)

        Label(f, text="Controls", bg="darkgray", font=("Times", 30)).place(relx=.5, rely=.05, anchor='center')

        Button(f, text="Back", bg="darkgray", font=("Times", 10), command=lambda: self.switchwindow("mainmenu")).place(
            relx=.05, rely=.97, anchor='center')

        return f

m = MinesweeperWindow()
