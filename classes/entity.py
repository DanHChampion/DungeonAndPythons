
from random import random

class Entity:
    def __init__(self, name='???', level=1):
        self.name = name
        self.level = level
        self.position = (0, 0)  # Default position, can be updated when placed in the dungeon
        self.character = '~'
        self.log_messages: list[str] = []
        self.base_stats = {
            "health": 100,
            "strength": 1,
            "defense": 1,
            "agility": 1,
            "intellect": 1
        }
        self.current_health = self.base_stats['health']

    def draw_health_bar(self, bar_length=20):
        if hasattr(self, 'add_stats'):
            filled_length = int(self.current_health / (self.base_stats['health'] + self.add_stats['health']) * bar_length)
            bar = "#" * filled_length + "-" * (bar_length - filled_length)
            return f"HP : [{bar}] {self.current_health}/{self.base_stats['health']+self.add_stats['health']}"
        filled_length = int(self.current_health / self.base_stats['health'] * bar_length)
        bar = "#" * filled_length + "-" * (bar_length - filled_length)
        return f"HP : [{bar}] {self.current_health}/{self.base_stats['health']}"

    def attack(self, target: Entity):
        # Calculate total damage
        damage = self.base_stats['strength']
        agility = self.base_stats['agility']
        if hasattr(self, 'add_stats'):
            damage += self.add_stats.get('strength', 0)
            agility += self.add_stats.get('agility', 0)
        # Add random variation to damage
        target_defense = target.base_stats['defense']
        target_agility = target.base_stats['agility']
        if hasattr(target, 'add_stats'):
            target_defense += target.add_stats.get('defense', 0)
            target_agility += target.add_stats.get('agility', 0)
        final_damage = max(1, damage - target_defense)
        hit_chance = min(1, max(0, 0.8 + (agility - target_agility) * 0.05))
        if hasattr(self, 'equipment'):
            weapon = self.equipment.get('weapon')
            if weapon and hasattr(weapon, 'accuracy'):
                hit_chance *= weapon.accuracy
        if random() > hit_chance:
            self.log_messages.append(f"{self.name}[{self.level}] misses {target.name}[{target.level}]!")
            return
        target.take_damage(final_damage)
        self.log_messages.append(f"{self.name}[{self.level}] attacks {target.name}[{target.level}] for {final_damage} damage!")
        self.log_messages.append(f"{target.name} has {target.draw_health_bar()} HP left.")

    def take_damage(self, amount: int):
        self.current_health = max(0, self.current_health - amount)
    
    def __str__(self):
        return self.character