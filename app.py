from classes.character import Character
from classes.mob import Monster
from classes.game import Game
import os

game = Game()
character = Character()
mob = Monster("Aranho")

# TEM QUE CRIAR OPCOES
# LUTAR (GERA MOB ALEATORIO INICIA A LUTA)
# DESCANSO(CUSTA MOEDAS E RECUPERA VIDA)

while True:
    character.show_stats()
    mob.monster_attack(character)
    character.show_stats()
    break
    # destiny = str(input("Escolha seu destino: \n [1] Lutar \n [2] Descansar\n"))
    # game.destiny(destiny)



print("game over")
# só para dale
# os.system('clear')




