from classes.character import Character
from classes.mob import Monster
import importlib

class Game:
  def __init__(self):
    self.possibility = ['lutar','descansar']
#   def __init__(self, character):
#       self.life_to_check = character.life

  def life_check(self, character):
      if character.life >= 0:
          return True
      else:
          return False

  def lutar(self):
      print("lutei")

  def descansar(self):
      print("descansei")

  def display_opts(self):
    options_str =  '\n'.join([f'\t\t [{position+1}] {option} ' for position, option  in  enumerate(self.possibility)])
    print(f'''
        # =============================================== #
          Escolha seu destino: 
{options_str}
        # =============================================== #''')

  def destiny(self, position,*args,**kwargs):
    command = self.possibility[int(position)-1]
    option = getattr(self,command)
    return option(*args,**kwargs)