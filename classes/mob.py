class Monster():
  
  def __init__(self, name):
    self.name = name
    self.max_life = 10
    self.life = self.max_life
    self.damage = 1
    self.max_stamina = 6
    self.stamina = 0
    self.stamina_regen = 1
    self.alive = True

  def show_monster_stats(self):
    print(f"Name: {self.name} // HP: {self.life}/{self.max_life} // Damage: {self.damage}")

  def show_battle_stats(self):
    print(f"Name: {self.name} // HP: {self.life}/{self.max_life} // Damage: {self.damage}")  

  def check_if_alive(self):
    if self.life < 0:
      self.alive = False

  ## criar status de stamina por um sleep para contar como stamina
  def monster_attack(self, target):
    target.life -= self.damage
    
