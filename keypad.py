#! /usr/bin/env python

import tkinter as tk
from typing import Optional
from functools import partial
from time import perf_counter
from threading import Timer
import conf


class Keypad:
    """pole tlačítek aplikace"""
    def __init__(self, window: tk.Tk,
                 pocet_tlacitek: int, strana: int, radek: int,
                 promenna_casu: tk.StringVar):
        self.window = window
        self.cas = promenna_casu
        self.pocet = pocet_tlacitek
        self.delka_strany = strana
        self.radek = radek
        self.sloupec = 1
        self.keys = []

        for i in range(1, self.pocet+1):
            if (len(range(1, self.pocet+1)) <= 10):
                t = tk.Button(self.window,
                              text=str(i),
                              background="#FFFFFF",
                              activebackground="#FFFFFF",
                              command=lambda i=i:   # type: ignore
                              self.stisk(i, None))
                self.window.bind(f"{i}",
                                 partial(self.stisk,
                                         i))
                self.window.bind(f"<KP_{i}>",
                                 partial(self.stisk,
                                         i))
            else:
                t = tk.Button(self.window,
                              text="",
                              background="#FFFFFF",
                              activebackground="#FFFFFF",
                              command=partial(self.stisk,
                                              i))
            t.grid(row=self.radek,
                   column=self.sloupec)
            self.keys.append(t)

            self.sloupec += 1
            if (self.sloupec > self.delka_strany):
                self.sloupec = 1
                self.radek -= 1

    def stisk(self, cislo_klavesy: int, event: Optional[tk.EventType]) -> None:
        self.stisknute_tlacitko = cislo_klavesy
        if (self.stisknute_tlacitko == conf.zbarvene_tlacitko+1
           and conf.zmacknuto is False):
            self.posledni_cas = perf_counter()-conf.start_cas
            conf.posledni_cas = int(round(self.posledni_cas, 3)*1000)
            self.cas.set(f"Poslední čas: {conf.posledni_cas} ms")
            self.prebarvit(conf.zbarvene_tlacitko, "#00FF00", False)
            conf.zmacknuto = True
            Timer(1,
                  lambda:
                      self.prebarvit(conf.zbarvene_tlacitko,
                                     "#FFFFFF",
                                     True)
                  ).start()

    def prebarvit(self, klavesa: int, barva: str, konec: bool) -> None:
        self.cislo_klavesy = klavesa
        self.barva = barva
        self.keys[self.cislo_klavesy].config(background=str(self.barva),
                                             activebackground=str(self.barva))
        if (konec is True):
            conf.spusteno = False
