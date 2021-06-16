import tkinter as tk
import requests

class Window(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Internet Wind Vane - Dcard")
        self.master.geometry("512x384")

        test = tk.Label(self.master, text="test")
        test.grid()
