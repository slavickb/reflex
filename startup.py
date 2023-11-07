#! /usr/bin/env python

import tkinter as tk
from functools import partial
import conf


class StartApp:
    """Startovní okno aplikace"""
    def __init__(self):
        self.start_window = tk.Tk()
        self.start_window.title("Startup")
        self.popis = tk.Label(self.start_window,
                              text="Vítejte v programu na testování vašich reflexů!\n"
                              "Máme pro vás několik testů:"
                              ).grid(row=1,
                                     columnspan=3,
                                     column=1)
        self.moznost1 = tk.Button(self.start_window,
                                  text="Pouze rychlost odezvy!",
                                  command=lambda:
                                      self.volba(1)
                                  ).grid(row=2,
                                         column=1)
        self.moznost2 = tk.Button(self.start_window,
                                  text="Numerická klávesnice!",
                                  command=lambda:
                                      self.volba(2)
                                  ).grid(row=2,
                                         column=2)
        self.moznost3 = tk.Button(self.start_window,
                                  text="Myš!",
                                  command=lambda:
                                      self.volba(3)
                                  ).grid(row=2,
                                         column=3)

        self.start_window.bind("<Escape>",
                               partial(self.volba,
                                       None))
        for i in range(1, 4):
            self.start_window.bind(str(i),
                                   partial(self.volba,
                                           i))
            self.start_window.bind(f"KP_{str(i)}",
                                   partial(self.volba,
                                           i))

    def volba(self, volba, event=None):
        conf.start_volba = volba
        self.start_window.destroy()
