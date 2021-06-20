import logging
import threading
import tkinter as tk
from time import sleep

import api
from PIL import Image, ImageTk


class Window(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Internet Wind Vane")
        # self.master.geometry("800x600")

        self.options_frame = None

        self.wordcloud_frame = None
        self.wordcloud_image = None

        self.image_temp = None

        self.base_frame()

        def set_button_position(container, widget, row, column):
            widget.grid(row=row, column=column, sticky="new")
            # container.grid_rowconfigure(row, weight=1)
            container.grid_columnconfigure(column, weight=1)

        row_BT = 1

        self.dcardBT = tk.Button(self.master, text="Dcard", command=self.dcard_frame)
        set_button_position(self.master, self.dcardBT, row_BT, 0)

        self.newsBT = tk.Button(self.master, text="News", command=self.news_frame)
        set_button_position(self.master, self.newsBT, row_BT, 1)

        self.pttBT = tk.Button(self.master, text="Ptt", command=self.ptt_frame)
        set_button_position(self.master, self.pttBT, row_BT, 2)

    def base_frame(self):

        # make options frame
        options_row_frame = 2
        self.options_frame = tk.Frame(self.master, width=0, height=0, background="bisque")
        self.options_frame.grid_propagate(True)
        self.options_frame["borderwidth"] = 2
        self.options_frame["relief"] = "sunken"
        self.options_frame.grid(row=options_row_frame, column=0, sticky="news", columnspan=3)

        # make word cloud frame
        wordcloud_row_frame = 3
        self.wordcloud_frame = tk.Frame(self.master, width=400, height=200, background="bisque")
        self.wordcloud_frame.grid_propagate(False)
        self.wordcloud_frame["borderwidth"] = 2
        self.wordcloud_frame["relief"] = "sunken"
        self.wordcloud_frame.grid(row=wordcloud_row_frame, column=0, sticky="news", columnspan=3)

    def dcard_frame(self):
        self.base_frame()
        tk.Label(self.options_frame, text="dcard").grid(row=0, column=0, sticky="n")

        tk.Button(self.options_frame, text="Dcard Data", command=self.place_wordcloud)\
            .grid(row=0, column=1, sticky="new")

        self.wordcloud_image = tk.Label(self.wordcloud_frame)
        self.wordcloud_image.grid()

    def news_frame(self):
        self.base_frame()
        tk.Label(self.options_frame, text="news api").grid(row=0, column=0, sticky="n")

        # self.master.grid_rowconfigure(1, weight=1)

    def ptt_frame(self):
        self.base_frame()
        tk.Label(self.options_frame, text="ptt").grid(row=0, column=0, sticky="n")

        # self.master.grid_rowconfigure(1, weight=1)

    def place_wordcloud(self):
        t = threading.Thread(target=self.place_wordcloud_thread, daemon=True)
        t.start()

    def place_wordcloud_thread(self):
        logging.debug("generating...")
        api.gen_wordcloud(api.get_data("dcard"))
        # self.images.append())
        self.image_temp = ImageTk.PhotoImage(Image.open('image/cloud.png'))
        self.wordcloud_image["image"] = self.image_temp
        logging.debug("place image ok")
