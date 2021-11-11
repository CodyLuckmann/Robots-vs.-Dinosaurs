from weapons import Weapon
class Robots:
    def __init__(self, name):
        self.name = name
        self.health = 50
        weapon = Weapon("Sword", 5)
        