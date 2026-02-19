from classes.entity import Entity

class Player(Entity):
    def __init__(self, name):
        super().__init__(name, max_health=100, level=1)
        self.inventory = []
        self.log_messages = []
        self.character = 'O'
        self.xp = 0
        self.next_level_xp = 100

    def get_stats(self):
        self.log_messages = []
        self.log_messages.append(f"Player: {self.name}")
        self.log_messages.append(f"Health: {self.health}")
        self.log_messages.append(f"Inventory: [{'][ '.join(self.inventory) if self.inventory else 'Empty'}]")

    def take_damage(self, amount):
        self.log_messages = []
        self.health = max(0, self.health - amount)
        if self.health == 0:
            self.log_messages.append(f"{self.name} has been defeated!")

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)