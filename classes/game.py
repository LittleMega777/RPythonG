from classes.character import Character
from classes.mob import Monster

class Game:
  def __init__(self):
      self.possibility = {
          "1":self.lutar,
          "2":self.descansar
      }
  def lutar(self):
      print("lutei")

  def descansar(self):
      print("descansei")

  def destiny(self, command):
      return self.possibility[command]()