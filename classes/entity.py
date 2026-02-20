class Entity:
    def __init__(self, name='???', max_health=100, level=1):
        self.name = name
        self.current_health = max_health
        self.level = level
        self.position = (0, 0)  # Default position, can be updated when placed in the dungeon
        self.character = '~'
        self.stats = {
            "health": max_health,
            "strength": 1,
            "defense": 1,
            "agility": 1,
            "intellect": 1
        }
    
    def __str__(self):
        return self.character