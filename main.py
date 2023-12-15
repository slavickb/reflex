#! /usr/bin/env python

import tkinter as tk
from typing import Optional
from random import randint, choice
from math import ceil
from time import perf_counter
from threading import Timer
import conf
import startup
import keypad


class MainApp:
    """Hlavní třída aplikace"""
    def __init__(self, volba: int) -> None:
        self.window = tk.Tk()

        self.volba = volba

        self.window.bind("<Escape>",
                         lambda event: self.konec(None))

        if (self.volba == 1):
            self.Reflex(self.window)
        elif (self.volba == 2):
            self.Numpad(self.window)
        elif (self.volba == 3):
            self.Aimlab(self.window)

    def konec(self, event: Optional[tk.EventType]) -> None:
        if (conf.spusteno is False):
            self.window.destroy()
            startup.StartApp()
            tk.mainloop()
            if (conf.start_volba is not None):
                MainApp(conf.start_volba)
                tk.mainloop()

    class Reflex:
        """Základní měření odezvy"""
        def __init__(self, window: tk.Tk):
            self.window = window
            self.window.title("Reflex!")

            self.pocet_tlacitek = 1
            self.tlacitka_strana = ceil(self.pocet_tlacitek**0.5)
            self.start_radek = int(3
                                   + (self.pocet_tlacitek/self.tlacitka_strana)
                                   )

            self.cas_ukazatel_data = tk.StringVar(self.window,
                                                  "Poslední čas: "
                                                  f"{conf.posledni_cas} ms")
            self.text_okna = tk.Label(self.window,
                                      text="Můžete stisknout číslo 1 "
                                      "či kliknout na tlačítko myší\n"
                                      "Mezerníkem spustíte hru!")
            self.text_okna.grid(row=1,
                                columnspan=self.tlacitka_strana,
                                column=1)
            self.cas_ukazatel = tk.Label(self.window,
                                         textvariable=self.cas_ukazatel_data)
            self.cas_ukazatel.grid(row=2,
                                   columnspan=self.tlacitka_strana,
                                   column=1)

            self.k = keypad.Keypad(self.window,
                                   self.pocet_tlacitek,
                                   self.tlacitka_strana,
                                   self.start_radek,
                                   self.cas_ukazatel_data)

            self.window.bind("<space>",
                             lambda event: self.jadro(None))

        def jadro(self, event: Optional[tk.EventType]) -> None:
            if (conf.spusteno is False):
                conf.spusteno = True
                Timer((randint(1415, 6900)/1000),
                      self.hra
                      ).start()

        def hra(self) -> None:
            conf.zmacknuto = False
            self.vybrane_tlacitko = choice(range(len(self.k.keys)))
            conf.zbarvene_tlacitko = self.vybrane_tlacitko
            self.k.prebarvit(conf.zbarvene_tlacitko,
                             "#FF0000",
                             False)
            conf.start_cas = perf_counter()

    class Numpad(Reflex):
        """hra s numerickou klávesnicí"""
        def __init__(self, window: tk.Tk) -> None:
            self.window = window
            self.window.title("Numpad!")

            self.pocet_tlacitek = 9
            self.tlacitka_strana = ceil(self.pocet_tlacitek**0.5)
            self.start_radek = int(3
                                   + (self.pocet_tlacitek/self.tlacitka_strana)
                                   )

            self.cas_ukazatel_data = tk.StringVar(self.window,
                                                  f"Poslední čas: "
                                                  f"{conf.posledni_cas} ms")
            self.text_okna = tk.Label(self.window,
                                      text="Můžete klikat na tlačítka myší "
                                      "či mačkat příslušná tlačítka "
                                      "na klávesnici\n"
                                      "Mezerníkem spustíte hru")
            self.text_okna.grid(row=1,
                                columnspan=self.tlacitka_strana,
                                column=1)
            self.cas_ukazatel = tk.Label(self.window,
                                         textvariable=self.cas_ukazatel_data)
            self.cas_ukazatel.grid(row=2,
                                   columnspan=self.tlacitka_strana,
                                   column=1)

            self.k = keypad.Keypad(self.window,
                                   self.pocet_tlacitek,
                                   self.tlacitka_strana,
                                   self.start_radek,
                                   self.cas_ukazatel_data)

            self.window.bind("<space>",
                             lambda event: self.jadro(None))

    class Aimlab(Numpad):
        """Aimlab :)"""
        def __init__(self, window: tk.Tk) -> None:
            self.window = window
            self.window.title("Aimlab!")

            self.pocet_tlacitek = 900
            self.tlacitka_strana = ceil((self.pocet_tlacitek**0.5)*1.5)
            self.start_radek = int(3
                                   + (self.pocet_tlacitek/self.tlacitka_strana)
                                   )

            self.cas_ukazatel_data = tk.StringVar(self.window,
                                                  f"Poslední čas: "
                                                  f"{conf.posledni_cas} ms")
            self.text_okna = tk.Label(self.window,
                                      text="Jak přesní jste s myší? ;)\n"
                                      "Mezerníkem spustíte hru")
            self.text_okna.grid(row=1,
                                columnspan=self.tlacitka_strana,
                                column=1)
            self.cas_ukazatel = tk.Label(self.window,
                                         textvariable=self.cas_ukazatel_data)
            self.cas_ukazatel.grid(row=2,
                                   columnspan=self.tlacitka_strana,
                                   column=1)

            self.k = keypad.Keypad(self.window,
                                   self.pocet_tlacitek,
                                   self.tlacitka_strana,
                                   self.start_radek,
                                   self.cas_ukazatel_data)

            self.window.bind("<space>",
                             lambda event: self.jadro(None))


startup.StartApp()
tk.mainloop()

if (conf.start_volba is not None):
    MainApp(conf.start_volba)
    tk.mainloop()
