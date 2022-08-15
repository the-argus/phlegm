import tkinter.ttk as ttk
from ecs import GameObject


class CooldownButton(ttk.Button, GameObject):
    """A version of button which comes paired with a progressbar."""
    def __init__(self, parent, cooldown, **kwargs):
        """
            parent: Tk root
            cooldown: integer, how long progressbar takes before allowing
                another press
        """
        # remove keyword arguments that relate to cooldown functionality
        self.command = kwargs.pop("command")
        self.cooldown = cooldown

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
