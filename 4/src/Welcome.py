class Welcome:
    def __init__(self, welcome="Cześć", name="Bezimienny"):
        self.welcomeText = welcome
        self.name = name

    def welcome(self, welcome, name):
        return welcome + " " + name + "!"
