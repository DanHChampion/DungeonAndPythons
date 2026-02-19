from classes.entity import Entity

class Enemy(Entity):
    def __init__(self, name):
        super().__init__(name, max_health=50, level=1)