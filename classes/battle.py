from classes import character
from classes.mob import Mob
from classes.character import Character
from random import randint

class Battle:

    mobs_possiveis = ["Aranha", "Esqueleto", "Pato"] # arrumar
    
    mob = Mob(mobs_possiveis[randint(0, 2)]) # deschumbar com dicionario de monstros\

    def __init__(self, character:Character):
        
        self.mob = Mob()
        self.character = character