from classes.character import Character
from classes.mob import Monster

class Game:
  def __init__(self):
      self.possibility = {
          "1":self.battle,
          "2":self.sleep
      }
  def battle(self):
      ...
      

  def sleep(self):
      print("descansei")

  def destiny(self, command):
      return self.possibility[command]()