
class Dinosaur:
    def __init__(self, name,):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, robot,):
        robot.health -= self.attack_power 
        print(f"{robot.name} is attacked with a remaining {robot.health} health!")
      
       
    def is_alive(self):
        return self.health > 0
