class GameObject:
    all = []  # list of all gameobjects

    def __init__(self):
        self.tags = {}
        GameObject.all.append(self)
