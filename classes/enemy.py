import random
from data.enemies import ALL_ENEMIES
from classes.entity import Entity

class Enemy(Entity):
    def __init__(self,level=1):
        super().__init__(level=level)
        self.character = 'E'
        self.set_random_enemy()
    
    def set_random_enemy(self):
        # Flatten all enemies from the ALL_ENEMIES dict into a single list
        all_enemies_list = []
        for category_enemies in ALL_ENEMIES.values():
            all_enemies_list.extend(category_enemies.values())
        enemy_data = random.choice(all_enemies_list)
        self.name = enemy_data["name"]
        self.max_health = enemy_data["max_health"]
        self.current_health = self.max_health