from dinosaurs import Dinosaurs

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        dino1 = Dinosaurs("T-rex", 15)
        dino2 = Dinosaurs("Raptor", 10)
        dino3 = Dinosaurs("Tri-tops", 5)

        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)

        