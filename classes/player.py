from classes.entity import Entity
from classes.item import Item

class Player(Entity):
    def __init__(self, name: str):
        super().__init__(name=name, max_health=100, level=1)
        self.max_health=100,
        self.inventory: list[Item] = []
        self.log_messages: list[str] = []
        self.character: str = 'O'
        self.xp: int = 0
        self.equipment: dict[str, Item | None] = {
            "weapon": None,
            "armor": None,
            "accessory1": None,
            "accessory2": None
        }
        self.next_level_xp: int = 100

    def show_stats(self):
        self.log_messages.append(f"{self.name} [{self.level}]")
        bar_length = 20
        filled_length = int(self.current_health / self.stats['health'] * bar_length)
        bar = "#" * filled_length + "-" * (bar_length - filled_length)
        self.log_messages.append(f"HP : [{bar}] {self.current_health}/{self.stats['health']}")
        xp_bar_length = 20
        xp_filled_length = int(self.xp / self.next_level_xp * xp_bar_length)
        xp_bar = "#" * xp_filled_length + "-" * (xp_bar_length - xp_filled_length)
        self.log_messages.append(f"XP : [{xp_bar}] {self.xp}/{self.next_level_xp}")
        self.log_messages.append(f"{'Strength':9} : {self.stats['strength']}")
        self.log_messages.append(f"{'Defense':9} : {self.stats['defense']}")
        self.log_messages.append(f"{'Agility':9} : {self.stats['agility']}")
        self.log_messages.append(f"{'Intellect':9} : {self.stats['intellect']}")
        self.log_messages.append(f"{'Equipment':9} :")
        for slot, item in self.equipment.items():
            if item:
                self.log_messages.append(f"  {slot.capitalize():10} : {item.name}")
            else:
                self.log_messages.append(f"  {slot.capitalize():10} : None")
        
        if self.inventory:
            self.log_messages.append(f"Inventory: {'(full!)' if len(self.inventory) > 19 else ''}")
            for idx, item in enumerate(self.inventory, 1):
                self.log_messages.append(f"  {idx:2} : {item.name}[{item.level}] - {item.type.capitalize()}")
        else:
            self.log_messages.append("Inventory: (empty)")

    def take_damage(self, amount: int):
        self.log_messages = []
        self.current_health = max(0, self.current_health - amount)
        if self.current_health == 0:
            self.log_messages.append(f"{self.name} has been defeated!")

    def heal(self, amount: int):
        self.current_health = min(self.max_health, self.current_health + amount)

    def add_to_inventory(self, item: Item):
        self.inventory.append(item)

    def remove_from_inventory(self, item: Item):
        if item in self.inventory:
            self.inventory.remove(item)

    def gain_xp(self, amount: int):
        self.xp += amount
        if self.xp >= self.next_level_xp:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.next_level_xp
        self.next_level_xp = int(self.next_level_xp * 1.2)
        self.max_health += 1
        self.current_health = self.max_health
        self.stats["health"] += 1
        self.stats["strength"] += 1
        self.stats["defense"] += 1
        self.stats["agility"] += 1
        self.stats["intellect"] += 1
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
            self.log_messages.append(f"{self.name} equipped {item.name}!")
            self.show_stats()
        except (ValueError, AttributeError):
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