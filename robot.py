from weapon import Weapon

class Robot:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Plasmacaster", 25)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        
        print(f"{self.name} attacks using ,\n damaging {dinosaur.name} health to {dinosaur.health}")

    def is_alive(self):
        return self.health > 0

        
 
        
