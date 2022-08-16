import tkinter as tk
from tkinter import font
from game import Game


def main():
    # create the window
    main_window = tk.Tk()

    # customize widget settings before making any
    default_family = f'"{font.families()[0]}"'
    def_font = font.nametofont("TkDefaultFont")
    def_font.config(size=19, family=default_family)

    # embed the game in the window
    game = Game(main_window)

    # open floating window
    main_window.attributes("-type", "dialog")

    # update loop
    while True:
        try:
            game.update_idletasks()
            game.update()
        except tk.TclError:
            # loop ended because application was destroyed, probably
            # could also be an actual tcl error i guess
            break


if __name__ == "__main__":
    main()
