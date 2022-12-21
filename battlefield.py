from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self) -> None:
        self.robot = Robot("Jaegar")
        self.dinosaur = Dinosaur("Spinosaurus",)
    
    def run_game(self):
        self.display_welcome()
        print(" ")
        self.battle_phase()
        print("")
        self.display_winner()
    
    def display_welcome(self):
        print(" ")
        print("Welcome all to the battle of the ages!\nWhere technology takes on a prehistoric giant!\nSit back and enjoy this battle!")
        

    def battle_phase(self):
        while self.robot.is_alive() and self.dinosaur.is_alive():
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)

    
    def display_winner(self):
        if self.dinosaur.health >= 0:
            print(f"With that final blow {self.robot.name} claims this victory!\nSending {self.dinosaur.name} back into extinction!!")
            print(" ")
        elif self.robot.health >= 0:
            print(f'With that final blow {self.dinosaur.name} wins!/nProving technology is not always ontop!')
            print(" ")
            pass
