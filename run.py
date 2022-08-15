import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font


class GameObject:
    def __init__(self):
        self.tags = {}


class CooldownButton(ttk.Button, GameObject):
    """A version of button which comes paired with a progressbar."""
    def __init__(self, parent, **kwargs):
        """
            parent: Tk root
            cooldown: integer, how long progressbar takes before allowing
                another press
        """
        # remove keyword arguments that relate to cooldown functionality
        self.command = kwargs.pop("command")
        self.cooldown = int(kwargs.pop("cooldown"))

        # replace cooldown with our custom press method
        kwargs["command"] = self.press

        # complete initialization of button
        super().__init__(parent, **kwargs)
        GameObject.__init__(self)

        # internal variable declaration
        self._timer = 0

        # initialize component(s)
        self.tags["update"] = self.update

    def press(self):
        """Callback when button is pressed."""
        if self._timer > 0:
            return
        self.command()
        self._timer = self.cooldown

    def update(self):
        """Callback every frame."""
        if self._timer > 0:
            self._timer -= 1


class Game:
    def __init__(self, main_window, canvas):
        self.canvas = canvas
        self.slime = 1
        self.slime_button = tk.Button(
                main_window,
                text="collect slime",
                width=50,
                command=self.get_slime)
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
