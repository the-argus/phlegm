import tkinter as tk


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
kill.pack()
game.slime_button.pack()

# open floating window
main_window.attributes('-type', 'dialog')
main_window.mainloop()
