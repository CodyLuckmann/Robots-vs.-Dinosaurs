from weapons import Weapon


class Robots:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.weapon = Weapon("Sword", 5)

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        

        



