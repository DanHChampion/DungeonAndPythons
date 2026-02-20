from classes.player import Player
from classes.dungeon import Dungeon
from utils import clear_console

class Game:
    def __init__(self):
        self.is_running = False
        self.player = None

    def start(self, player_name="Hero"):
        self.is_running = True
        self.player = Player(player_name)
        self.dungeon = Dungeon(self.player)
        self.dungeon.generate_level()
        self.dungeon.show_current_level()

    def stop(self):
        self.is_running = False

    def parse_command(self, command):
        clear_console()
        self.dungeon.show_current_level()
        if command.lower() == "help":
            print(f">> {command}")
            print("Available commands: help, stats, clear, exit, test, equip <item>, unequip <type>, wasd (move)")
            return
        elif command.lower() == "clear":
            clear_console()
            self.dungeon.show_current_level()
        elif command.lower() == "stats":
            self.player.show_stats()
        elif command.lower() == "scan":
            self.dungeon.scan_surroundings()
        elif command.lower() == "test":
            self.dungeon.generate_level()
            clear_console()
            self.dungeon.show_current_level()
        elif command.lower().startswith("equip "):
            item_idx = command[6:].strip()
            self.player.equip_item(item_idx)
        elif command.lower().startswith("unequip "):
            item_type = command[8:].strip().lower()
            self.player.unequip_item(item_type)
        elif command.lower().startswith("drop "):
            item_idx = command[5:].strip()
            self.dungeon.drop_item(item_idx)
        elif all(c in "wasd" for c in command.lower()):
            self.dungeon.move_player(command.lower())
        else:
            print(f">> {command}")
            print("Invalid command. Use 'help' to see available commands.")
            return
        print(f">> {command}")
        for message in self.dungeon.log_messages:
            print(message)
        for message in self.player.log_messages:
            print(message)
        self.dungeon.log_messages = []
        self.player.log_messages = []
        
        