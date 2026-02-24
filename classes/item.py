import random
from data.items import ALL_ITEMS

class Item:
    def __init__(self, name="???", level=1):
        self.name = name
        self.description = "No description available."
        self.type = "generic"  # Can be "weapon", "armor", "accessory", etc.
        self.character = 'I'
        self.level = level
        if name == "???":
            self.set_random_item()
        else:
            self.set_item(name)
    
    def set_random_item(self):
        # Flatten all items from the ALL_ITEMS dict into a single list
        all_items_list = []
        for category_items in ALL_ITEMS.values():
            all_items_list.extend(category_items.keys())
        item_name = random.choice(all_items_list)
        self.set_item(item_name)

    def set_item(self, name: str):
        for category_items in ALL_ITEMS.values():
            if name in category_items:
                item_data = category_items[name]
                self.name = item_data["name"]
                self.description = item_data["description"]
                self.type = item_data["type"]
                self.base_stats = item_data.get("base_stats", {})
                self.effect = item_data.get("effect", None)
                self.effect_value = item_data.get("effect_value", 0)
                self.drop_chance = item_data.get("drop_chance", 0.5)
                break  
    
    def __str__(self):
        return self.character
    
