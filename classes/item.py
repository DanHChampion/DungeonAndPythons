import random
from data.items import ALL_ITEMS

class Item:
    def __init__(self, level=1):
        self.name = "???"
        self.description = "No description available."
        self.type = "generic"  # Can be "weapon", "armor", "accessory", etc.
        self.character = 'I'
        self.level = level
        self.set_random_item()
    
    def set_random_item(self):
        # Flatten all items from the ALL_ITEMS dict into a single list
        all_items_list = []
        for category_items in ALL_ITEMS.values():
            all_items_list.extend(category_items.values())
        item_data = random.choice(all_items_list)
        self.name = item_data["name"]
        self.description = item_data["description"]
        self.type = item_data["type"]
        
    
    def __str__(self):
        return self.character
    
