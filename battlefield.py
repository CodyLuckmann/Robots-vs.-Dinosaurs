from fleet import Fleet


from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to Robots vs. Dinosaurs!!")

    def battle(self):
        #if length of fleet list is greater than 0 and the length of herd list greater than 0
        while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
        #choose opponents
            dino_index = self.show_dino_opponent_options()
            robot_index = self.show_robo_opponent_options()
        #if opponents health >0 keep battling
            while (self.herd.dinosaurs[dino_index].health) > 0 and (self.fleet.robots[robot_index].health) > 0:
                self.dino_turn(self.herd.dinosaurs[dino_index])
                if len(self.fleet.robots) > 0 :
                    self.robo_turn(self.fleet.robots[robot_index])
                    #if defending dino health <= 0 remove from list
                if (self.herd.dinosaurs[dino_index].health <= 0):
                    self.herd.dinosaurs.pop(dino_index)
                # if defending robos health <= 0 remove from list
                if (self.fleet.robots[robot_index].health <= 0):
                    self.fleet.robots.pop(robot_index)
                    #if statement to break out of the loop when either the robot or dino lists hit 0
                if (len(self.herd.dinosaurs) == 0 or len(self.fleet.robots) == 0):
                    break
                    

        
    def dino_turn(self, dinosaur):
        robot_index = self.show_robo_opponent_options()
        dinosaur.attack(self.fleet.robots[robot_index])

    def robo_turn(self, robot):
        dino_index = self.show_dino_opponent_options()
        robot.attack(self.herd.dinosaurs[dino_index])

    def show_dino_opponent_options(self):
        # create a (for) loop over the list and then print instance variables
        counter = 0
        for dinosaur in self.herd.dinosaurs:
            print(f'{counter}) {dinosaur.name}')
            counter +=1
        index = input("Choose a dinosaur: ")
        return int(index)

    def show_robo_opponent_options(self):
        counter = 0
        for robot in self.fleet.robots:
            print(f'{counter}) {robot.name}')
            counter +=1
        index = input("Choose a robot: ")
        return int(index)

    def display_winner(self):
        if len(self.fleet.robots) == 0:
            print("The Dinosaurs are the winners!")
        elif len(self.herd.dinosaurs) == 0:
            print("The Robots are the winners!")
            
