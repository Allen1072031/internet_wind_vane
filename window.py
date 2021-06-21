import threading
import time
import tkinter as tk

import api
from api import variable
from PIL import Image, ImageTk


class Window(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Internet Wind Vane")
        self.master.geometry("800x600")
        self.master.maxsize(800, 600)
        self.master.minsize(800, 600)

        self.options_frame = None
        self.genBT = None

        self.wordcloud_frame = None
        self.wordcloud_image = None

        self.image_temp = None

        self.variables = {}

        self.base_frame()

        self.message_bar = tk.Label(self.master, text="Internet Wind Vane")
        self.message_bar.grid(row=0, column=0, columnspan=3)

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
        self.wordcloud_frame = tk.Frame(self.master, width=800, height=600, background="bisque")
        self.wordcloud_frame.grid_propagate(True)
        self.wordcloud_frame["borderwidth"] = 2
        self.wordcloud_frame["relief"] = "sunken"
        self.wordcloud_frame.grid(row=wordcloud_row_frame, column=0, sticky="news", columnspan=3)

    def dcard_frame(self):
        self.base_frame()

        def dcard_func():
            self.place_wordcloud(
                api="dcard",
                data_from=self.variables["data_from"].get(),
                forum=self.variables["forum"].get()
            )

        self.genBT = tk.Button(self.options_frame, text="Generate Word Cloud", command=dcard_func)
        self.genBT.grid(row=3, column=0, sticky="news")

        options_list = ["all", "forum"]

        self.variables["data_from"] = tk.StringVar()
        self.variables["data_from"].set(options_list[0])
        tk.Label(self.options_frame, text="資料範圍").grid(row=1, column=0)
        tk.OptionMenu(self.options_frame, self.variables["data_from"], *options_list).grid(row=1, column=1, sticky="news")

        options_list = ["", "yzu"]
        self.variables["forum"] = tk.StringVar()
        self.variables["forum"].set(options_list[0])
        tk.Label(self.options_frame, text="看板").grid(row=2, column=0)
        tk.OptionMenu(self.options_frame, self.variables["forum"], *options_list).grid(row=2, column=1, sticky="news")

        self.wordcloud_image = tk.Label(self.wordcloud_frame)
        self.wordcloud_image.grid()

    def news_frame(self):
        self.base_frame()

        def news_func():
            self.place_wordcloud(
                api="news",
            )

        self.genBT = tk.Button(self.options_frame, text="Generate Word Cloud", command=news_func)
        self.genBT.grid(row=0, column=0, sticky="news")

        self.wordcloud_image = tk.Label(self.wordcloud_frame)
        self.wordcloud_image.grid()

    def ptt_frame(self):
        self.base_frame()
        tk.Label(self.options_frame, text="username").grid(row=0, column=0, sticky="n")
        self.variables["ptt_username"] = tk.StringVar()
        tk.Entry(self.options_frame, textvariable=self.variables["ptt_username"]).grid(row=0, column=1, sticky="n")

        tk.Label(self.options_frame, text="password").grid(row=1, column=0, sticky="n")
        self.variables["ptt_password"] = tk.StringVar()
        tk.Entry(self.options_frame, textvariable=self.variables["ptt_password"], show="*").grid(row=1, column=1, sticky="n")

        def ptt_func():
            self.place_wordcloud(
                api="ptt",
                ptt_username=self.variables["ptt_username"].get(),
                ptt_password=self.variables["ptt_password"].get()
            )

        self.genBT = tk.Button(self.options_frame, text="Generate Word Cloud", command=ptt_func)
        self.genBT.grid(row=2, column=0, sticky="news")

        self.wordcloud_image = tk.Label(self.wordcloud_frame)
        self.wordcloud_image.grid()

    def place_wordcloud(self, **kwargs):
        api_thread = threading.Thread(target=self.place_wordcloud_thread, daemon=True, kwargs=kwargs)
        progress_thread = threading.Thread(target=self.progress_bar, daemon=True)

        api_thread.start()
        progress_thread.start()

    def progress_bar(self):
        variable.progress_init()
        time_count = 0
        time_out = 300
        while variable.crawl_processing != variable.crawl_end and time_count != time_out:
            self.message_bar["text"] = f"processing {variable.crawl_processing}/{variable.crawl_end}..."
            time.sleep(1)
            time_count += 1

    def place_wordcloud_thread(self, **kwargs):
        self.genBT["state"] = "disabled"
        if kwargs["api"] == "dcard":
            self.newsBT["state"] = "disabled"
            self.pttBT["state"] = "disabled"
        elif kwargs["api"] == "news":
            self.dcardBT["state"] = "disabled"
            self.pttBT["state"] = "disabled"
        elif kwargs["api"] == "ptt":
            self.dcardBT["state"] = "disabled"
            self.newsBT["state"] = "disabled"

        self.message_bar["text"] = "Loading data..."
        api.gen_wordcloud(api.get_data(**kwargs))

        self.message_bar["text"] = "Generate cloud word..."
        self.image_temp = ImageTk.PhotoImage(Image.open('image/cloud.png'))
        self.wordcloud_image["image"] = self.image_temp

        self.message_bar["text"] = "Finish"

        self.dcardBT["state"] = "normal"
        self.newsBT["state"] = "normal"
        self.pttBT["state"] = "normal"
        self.genBT["state"] = "normal"
