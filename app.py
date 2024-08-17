from classes.character import Character
from classes.mob import Monster
from classes.game import Game
import os
from random import randint


mobs_possiveis = ["Aranha", "Esqueleto", "Pato"] # arrumar
character = Character()
mob = Monster(mobs_possiveis[randint(0, 2)]) # deschumbar com dicionario de monstros
# randint = random + int = inteiro

game = Game(character, mob)

# TEM QUE CRIAR OPCOES
# LUTAR (GERA MOB ALEATORIO INICIA A LUTA)
# DESCANSO(CUSTA MOEDAS E RECUPERA VIDA)

while True:
    character.show_stats()
    destiny = str(input("Escolha seu destino: \n [1] Lutar \n [2] Descansar\n")) # colocar numa def mais inteligente
    game.destiny(destiny)




