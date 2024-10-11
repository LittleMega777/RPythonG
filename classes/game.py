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

    def print_stamina_bar(self, current_stamina, max_stamina):
        bar_length = 30 # Length of the bar in characters
        filled_length = int(bar_length * current_stamina // max_stamina)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f'|{bar}| {current_stamina}/{max_stamina}')
    
    def destiny(self, command):
        return self.possibility[command]()

    def battle(self):
        self.character.show_battle_stats()
        self.monster.show_battle_stats()

        while self.character.life > 0 and self.monster.life > 0:
            time.sleep(1)
            self.character.stamina += 1
            self.monster.stamina += 1
            print(f"Guerreiro Stamina:")
            self.print_stamina_bar(self.character.stamina, self.character.max_stamina)
            print(f"Monster Stamina:")
            self.print_stamina_bar(self.monster.stamina, self.monster.max_stamina)
            
            if self.monster.stamina >= self.monster.max_stamina:
                print(f"{self.monster.name} deu {self.monster.damage} de dano")
                self.monster.monster_attack(self.character)
                self.monster.stamina = 0
                self.character.show_battle_stats()
                time.sleep(1)
                
            if self.character.stamina >= self.character.max_stamina:
                print(f"{self.character.name} deu {self.character.damage} de dano")
                self.character.character_attack(self.monster)
                self.character.stamina = 0
                self.monster.show_battle_stats()
                time.sleep(1)
        print("========================= fim da luta ============================")
            
    def sleep(self): # ta para chegar ai
        print("descansei")