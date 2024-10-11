class Creature:
    def __init__(self, name, max_life, damage, level, max_stamina, stamina, stamina_regen):
        self.name = name
        self.max_life = max_life
        self.life = self.max_life
        self.damage = damage
        self.level = level
        self.max_stamina = max_stamina
        self.stamina = stamina
        self.stamina_regen = stamina_regen
        self.inventario = []