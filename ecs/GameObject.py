class GameObject:
    all = []  # list of all gameobjects

    # lists for each component/tag
    updaters = []
    drawers = []

    @classmethod
    def sort_all(cls):
        for obj in cls.all:
            obj.sort()
        # all of the objects are sorted, empty the list
        cls.all = []

    def __init__(self):
        self.tags = {}
        GameObject.all.append(self)

    def sort(self):
        """Move a tagged object into the list with objects of its type"""
        if "update" in self.tags:
            GameObject.updaters.append(self)
        if "draw" in self.tags:
            GameObject.drawers.append(self)

    def kill(self):
        """Remove this object from all the lists."""
        if "update" in self.tags:
            GameObject.updaters.remove(self)
        if "draw" in self.tags:
            GameObject.drawers.remove(self)
