from robots import Robots

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet(Robots)

    def create_fleet(self, robot):
        robot1 = Robots("R2D2")
        robot2 = Robots("C3PO")
        robot3 = Robots("BB8")
        
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
        