from weapons import Weapon


class Robots:
    def __init__(self, name):
        self.name = name
        self.health = 50
        weapon = Weapon("Sword", 5)

    def attack(self, dinosaur):
        pass

robot1 = Robots("R2D2")
robot2 = Robots("C3PO")
robot3 = Robots("BB8")