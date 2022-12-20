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
        print("welcome all to the battle of champions!\nWhere only one will survive!\nSit back and enjoy this battle!")
        

    def battle_phase(self):
        while self.robot.is_alive() and self.dinosaur.is_alive():
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)

    
    def display_winner(self):
        if self.dinosaur.health >= 0:
            print(f"robo")
        elif self.robot.health >= 0:
            print(f'dino')
            pass
