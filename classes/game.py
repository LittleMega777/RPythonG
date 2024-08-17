from classes.character import Character
from classes.mob import Monster
import time

class Game:
    
    def __init__(self, character, monster):
        self.character = character
        self.monster = monster
        self.possibility = {
            "1":self.battle,
            "2":self.sleep
        }
    
    def destiny(self, command):
        return self.possibility[command]()

    def battle(self):
        while self.character.life > 0 and self.monster.life > 0:
            time.sleep(1)
            self.character.stamina += 1
            self.monster.stamina += 1
            if self.monster.stamina >= self.monster.max_stamina:
                print(f"{self.monster.name} deu {self.monster.damage} de dano")
                self.monster.monster_attack(self.character)
                self.monster.stamina = 0

            if self.character.stamina >= self.character.max_stamina:
                print(f"{self.character.name} deu {self.character.damage} de dano")
                self.character.character_attack(self.monster)
                self.character.stamina = 0
        print("fim da luta")
            
    def sleep(self): # ta para chegar ai
        print("descansei")