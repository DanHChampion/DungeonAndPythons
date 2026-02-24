from classes.entity import Entity
from classes.item import Item

class Player(Entity):
    def __init__(self, name: str):
        super().__init__(name=name, level=1)
        self.inventory: list[Item] = []
        self.character: str = 'O'
        self.xp: int = 0
        self.equipment: dict[str, Item | None] = {
            "weapon": None,
            "armor": None,
            "accessory1": None,
            "accessory2": None
        }
        self.next_level_xp: int = 100
        self.calculate_stats()
        self.add_stats = {
            "health": 0,
            "strength": 0,
            "defense": 0,
            "agility": 0,
            "intellect": 0
        }

    def calculate_stats(self):
        # Base stats from level
        self.base_stats["health"] = 100 + (self.level - 1) * 5
        self.base_stats["strength"] = 5 + (self.level - 1) * 2
        self.base_stats["defense"] = 5 + (self.level - 1) * 2
        self.base_stats["agility"] = 5 + (self.level - 1) * 2
        self.base_stats["intellect"] = 5 + (self.level - 1) * 2
        self.add_stats = {
            "health": 0,
            "strength": 0,
            "defense": 0,
            "agility": 0,
            "intellect": 0
        }
        # Add stats from equipped items
        for slot, item in self.equipment.items():
            if item:
                for stat, value in item.base_stats.items():
                    self.add_stats[stat] += value*item.level

    def show_stats(self):
        self.calculate_stats()
        self.log_messages.append(f"{self.name} [{self.level}]")
        bar_length = 20
        filled_length = int(self.current_health / (self.base_stats['health'] + self.add_stats['health']) * bar_length)
        bar = "#" * filled_length + "-" * (bar_length - filled_length)
        self.log_messages.append(f"HP : [{bar}] {self.current_health}/{self.base_stats['health']+self.add_stats['health']}")
        xp_bar_length = 20
        xp_filled_length = int(self.xp / self.next_level_xp * xp_bar_length)
        xp_bar = "#" * xp_filled_length + "-" * (xp_bar_length - xp_filled_length)
        self.log_messages.append(f"XP : [{xp_bar}] {round(self.xp)}/{self.next_level_xp}")
        self.log_messages.append(f"{'Strength':9} : {self.base_stats['strength']} + {self.add_stats['strength']} ({self.base_stats['strength'] + self.add_stats['strength']})")
        self.log_messages.append(f"{'Defense':9} : {self.base_stats['defense']} + {self.add_stats['defense']} ({self.base_stats['defense'] + self.add_stats['defense']})")
        self.log_messages.append(f"{'Agility':9} : {self.base_stats['agility']} + {self.add_stats['agility']} ({self.base_stats['agility'] + self.add_stats['agility']})")
        self.log_messages.append(f"{'Intellect':9} : {self.base_stats['intellect']} + {self.add_stats['intellect']} ({self.base_stats['intellect'] + self.add_stats['intellect']})")
        self.log_messages.append(f"{'Equipment':9} :")
        for slot, item in self.equipment.items():
            if item:
                self.log_messages.append(f"  {slot.capitalize():10} : {item.name}[{item.level}]")
            else:
                self.log_messages.append(f"  {slot.capitalize():10} : None")
        
        if self.inventory:
            self.log_messages.append(f"Inventory: {'(full!)' if len(self.inventory) > 19 else ''}")
            for idx, item in enumerate(self.inventory, 1):
                self.log_messages.append(f"  {idx:2} : {item.name}[{item.level}] - {item.type.capitalize()}")
        else:
            self.log_messages.append("Inventory: (empty)")

    def heal(self, amount: int):
        self.current_health = min(self.base_stats['health'] + self.add_stats['health'], self.current_health + amount)

    def add_to_inventory(self, item: Item):
        self.inventory.append(item)

    def remove_from_inventory(self, item: Item):
        if item in self.inventory:
            self.inventory.remove(item)

    def gain_xp(self, amount: int):
        self.xp += amount
        while self.xp >= self.next_level_xp:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.calculate_stats()
        self.xp -= self.next_level_xp
        self.next_level_xp = int(self.next_level_xp * 1.2)
        self.current_health = self.base_stats['health'] + self.add_stats['health']
        self.log_messages.append(self.current_health)
        self.log_messages.append(f"{self.name} leveled up to level {self.level}!")

    def equip_item(self, item_idx: str):
        try:
            idx = int(item_idx) - 1
            if not (0 <= idx < len(self.inventory)):
                self.log_messages.append(f"Invalid item index: {item_idx}")
                return
            item = self.inventory[idx]
            slot = item.type

            # Handle accessories with two slots
            if slot == "accessory":
                # Find first empty accessory slot
                empty_slot = None
                for acc_slot in ["accessory1", "accessory2"]:
                    if self.equipment[acc_slot] is None:
                        empty_slot = acc_slot
                        break
                if empty_slot:
                    self.equipment[empty_slot] = item
                    self.inventory.pop(idx)
                    self.log_messages.append(f"{self.name} equipped {item.name}[{item.level}]!")
                else:
                    # Both slots full, unequip accessory2 by default
                    self.unequip_item("accessory2")
                    # After unequipping, accessory2 is empty
                    self.equipment["accessory2"] = item
                    self.inventory.pop(idx)
                    self.log_messages.append(f"{self.name} equipped {item.name}[{item.level}]!")
                return

            # Handle other equipment slots
            if slot not in self.equipment:
                self.log_messages.append(f"{item.name} cannot be equipped.")
                return
            if self.equipment[slot]:
                self.unequip_item(slot)
            self.equipment[slot] = item
            self.inventory.pop(idx)
            self.log_messages.append(f"{self.name} equipped {item.name}[{item.level}]!")
        except (ValueError):
            self.log_messages.append(f"Invalid item index: {item_idx}")

    def unequip_item(self, item_type: str):
        if not item_type in self.equipment:
            self.log_messages.append(f"Invalid equipment slot: {item_type}")
            return
        if item_type in self.equipment and self.equipment[item_type]:
            item = self.equipment[item_type]
            self.add_to_inventory(item)
            self.equipment[item_type] = None
            self.log_messages.append(f"{self.name} unequipped {item.name}!")
        else:
            self.log_messages.append(f"No item equipped in {item_type} slot.")

    def use_item(self, item_idx: str):
        try:
            idx = int(item_idx) - 1
            if not (0 <= idx < len(self.inventory)):
                self.log_messages.append(f"Invalid item index: {item_idx}")
                return
            item = self.inventory[idx]
            # For simplicity, let's say using an item just heals the player for now
            if item.type == "consumable" and hasattr(item, 'effect') and hasattr(item, 'effect_value'):
                if item.effect == "heal":
                    heal_amount = item.effect_value
                    self.heal(heal_amount)
                    self.inventory.pop(idx)
                    self.log_messages.append(f"{self.name} used {item.name} and healed for {heal_amount} HP!")
            else:
                self.log_messages.append(f"{item.name} cannot be used.")
        except ValueError:
            self.log_messages.append(f"Invalid item index: {item_idx}")

    def destroy_item(self, item_idx: str):
        try:
            # Parse input into list of unique, sorted (descending) indexes
            idx_list = sorted(
                {int(idx.strip()) - 1 for idx in item_idx.split(',') if idx.strip().isdigit()},
                reverse=True
            )
            if not idx_list:
                self.log_messages.append(f"Invalid item index: {item_idx}")
                return
            # Check all indexes are valid before removing
            if any(idx < 0 or idx >= len(self.inventory) for idx in idx_list):
                self.log_messages.append(f"Invalid item index: {item_idx}")
                return
            for idx in idx_list:
                item = self.inventory[idx]
                self.inventory.pop(idx)
                self.log_messages.append(f"{self.name} destroyed {item.name}[{item.level}]!")
        except ValueError:
            self.log_messages.append(f"Invalid item index: {item_idx}")
