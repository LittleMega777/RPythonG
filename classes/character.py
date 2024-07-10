class Character:
  def __init__(self):
    self.name = "Guerreiro"
    self.max_life = 10
    self.life = self.max_life
    self.damage = 1
    self.xp = 0
    self.stamina = 3
    self.coins = 0
  
  def show_stats(self):
    print(f"Name: {self.name} // HP: {self.life}/{self.max_life} // Damage: {self.damage} // Level: {self.xp} // Moedas: {self.coins}")
  
  def character_attack(self, target):
    target.life -= self.damage
    