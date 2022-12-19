
class Dinosaur:
    def __init__(self, name,):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, robot, attack_power):
        robot.health -= attack_power 
        print(f"{robot.name}{robot.health}")
