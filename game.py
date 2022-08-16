import tkinter as tk
from widgets import CooldownButton
from ecs import GameObject


class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.canvas = tk.Canvas(master, width=100, height=100)
        self.slime = 1
        self.slime_button = CooldownButton(
            master, text="collect slime", width=50, command=self.get_slime, cooldown=10
        )

        self.kill = tk.Button(master, text="kill...", width=100, command=master.destroy)

        # pack buttons
        self.kill.pack(padx=5, pady=5)
        self.slime_button.pack(padx=5, pady=5)
        self.slime_text = self.canvas.create_text(30, 10)
        self.update_slime()
        self.canvas.insert(self.slime_text, 50, "")
        self.canvas.pack()

        GameObject.sort_all()

    def get_slime(self):
        self.slime += 1
        self.update_slime()

    def update_slime(self):
        self.canvas.itemconfig(self.slime_text, text=f"slime: {self.slime}")

    def update(self):
        super().update()
        for object in GameObject.updaters:
            object.update()
