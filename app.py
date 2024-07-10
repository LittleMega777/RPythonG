from classes.character import Character
from classes.mob import Monster
from classes.game import Game
import os

character = Character()
mob = Monster("Aranho")
game = Game()

# TEM QUE CRIAR OPCOES
# LUTAR (GERA MOB ALEATORIO INICIA A LUTA)
# DESCANSO(CUSTA MOEDAS E RECUPERA VIDA)

while game.life_check(character):
    character.show_stats()
    mob.monster_attack(character)
    # destiny = str(input("Escolha seu destino: \n [1] Lutar \n [2] Descansar\n"))
    game.display_opts()
    destiny = input(' *** Aguardando input ** :')
    game.destiny(destiny)

print("game over")
# só para dale
# os.system('clear')




