from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self) -> None:
        self.robot = Robot("Jaegar")
        self.dinosaur = Dinosaur("Spinosaurus",)
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    
    def display_welcome(self):
        print(" ")
        print("welcome all to the battle of champions!\nWhere only one will survive!\nSit back and enjoy this battle!")
    
    def battle_phase(self):
        self.dinosaur.attack
        self.robot.attack
    
    def display_winner(self):
        pass