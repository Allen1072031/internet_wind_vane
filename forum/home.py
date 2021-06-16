import tkinter as tk
from forum import dcard

class Window(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Internet Wind Vane")
        self.master.geometry("512x384")

        self.windows = []

        self.dcardBT = tk.Button(self.master, text="Dcard", command=lambda: self.windows.append(dcard.Window()))
        self.dcardBT.grid()

    def dcard_window(self):
        self.dcard = dcard.Window()
        # self.mainloop()
    #
    # def __del__(self):
    #     if not self.dcard:
    #         self.dcard.__del__()

