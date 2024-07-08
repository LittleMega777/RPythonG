class Game:
  def lutar(self):
      print("lutei")

  def descansar(self):
      print("descansei")

  def destiny(self, command):
      possibility = {
          "1":self.lutar,
          "2":self.descansar
      }
      return possibility[command]()