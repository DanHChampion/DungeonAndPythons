class Entity:
    def __init__(self, name, max_health=100, level=1):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.level = level
        self.position = (0, 0)  # Default position, can be updated when placed in the dungeon
        self.character = '~'