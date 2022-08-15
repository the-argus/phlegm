import tkinter as tk
from tkinter import font
from widgets import CooldownButton


class Game:
    def __init__(self, main_window, canvas):
        self.canvas = canvas
        self.slime = 1
        self.slime_button = CooldownButton(
                main_window,
                text="collect slime",
                width=50,
                command=self.get_slime,
                cooldown=10)
        self.slime_text = main.create_text(30, 10)
        self.update_slime()
        canvas.insert(self.slime_text, 50, "")

    def get_slime(self):
        self.slime += 1
        self.update_slime()

    def update_slime(self):
        self.canvas.itemconfig(self.slime_text, text=f"slime: {self.slime}")


main_window = tk.Tk()
default_family = f"\"{font.families()[0]}\""
def_font = font.nametofont("TkDefaultFont")
def_font.config(size=19, family=default_family)
# main_window.option_add('*Font', f"{default_family} 19")
main = tk.Canvas(main_window,
                 width=100,
                 height=100)
main.pack()
game = Game(main_window, main)

kill = tk.Button(main_window,
                 text='kill...',
                 width=100,
                 command=main_window.destroy)
# add all the buttons
kill.pack(padx=5, pady=5)
game.slime_button.pack(padx=5, pady=5)

# open floating window
main_window.attributes('-type', 'dialog')
main_window.mainloop()
