from tkinter import *


class MinesweeperWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x700")
        self.window = self.createmainmenu()
        self.root.mainloop()

    def switchwindow(self, window):
        pass

    def createmainmenu(self):
        menu = Frame(self.root, width=500, height=700, bg="gray")
        menu.place(x=0, y=0)
        L = Label(menu, text="Welcome to MineSweeper", bg="darkgray")
        L.place(relx=.5, rely=.1, anchor='center')

        return menu


    def creategame(self):
        pass

    def create2playergame(self):
        pass

    def create1psettings(self):
        pass

    def create2psettings(self):
        pass

m = MinesweeperWindow()