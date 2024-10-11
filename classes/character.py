class Character:
  
  def __init__(self):
    self.name = "Guerreiro"
    self.max_life = 10
    self.life = self.max_life
    self.damage = 3
    self.max_xp = 10
    self.xp = 0
    self.level = 1
    self.max_stamina = 3
    self.stamina = 0
    self.stamina_regen = 1
    self.coins = 0
    self.alive = True # vai receber funcao
  
  def show_stats(self):
    print(f"Name: {self.name} // HP: {self.life}/{self.max_life} // Damage: {self.damage} // Level: {self.level} // XP: {self.xp}/{self.max_xp} // Moedas: {self.coins}")
  
  def show_battle_stats(self):
    print(f"Name: {self.name} // HP: {self.life}/{self.max_life} // Damage: {self.damage}")

  def check_if_alive(self):
    if self.life < 0:
      self.alive = False

  def character_attack(self, target):
    target.life -= self.damage
    