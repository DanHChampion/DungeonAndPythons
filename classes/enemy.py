import random
from data.enemies import ALL_ENEMIES
from classes.entity import Entity

class Enemy(Entity):
    def __init__(self,level=1, position=(0, 0)):
        super().__init__(level=level)
        self.character = 'E'
        self.set_random_enemy()
        self.position = position
    
    def set_random_enemy(self):
        # Flatten all enemies from the ALL_ENEMIES dict into a single list
        all_enemies_list = []
        for category_enemies in ALL_ENEMIES.values():
            all_enemies_list.extend(category_enemies.values())
        enemy_data = random.choice(all_enemies_list)
        self.name = enemy_data["name"]
        self.base_stats = {stat: value + (self.level * 2) for stat, value in enemy_data["base_stats"].items()}
        self.current_health = self.base_stats['health']
        self.loot_table = enemy_data["loot_table"]
        self.xp_reward = enemy_data["xp_reward"] * (1.2 ** self.level)
        self.spawn_chance = enemy_data.get("spawn_chance", 1.0)