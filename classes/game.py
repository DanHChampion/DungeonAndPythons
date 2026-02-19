from classes.player import Player
from classes.dungeon import Dungeon

class Game:
    def __init__(self):
        self.is_running = False
        self.player = None

    def start(self):
        self.is_running = True
        self.player = Player("Hero")
        self.dungeon = Dungeon(self.player)
        self.dungeon.generate_level()
        self.dungeon.show_current_level()
        print("Game started!")

    def stop(self):
        self.is_running = False
        print("Game stopped!")

    def parse_command(self, command):
        print("\033c", end="")  # Clear console
        self.dungeon.show_current_level()
        if command.lower() == "help":
            print(f">> {command}")
            print("Available commands: help, stats, clear, exit")
            return
        elif command.lower() == "clear":
            print("\033c", end="")  # Clear console
            self.dungeon.show_current_level()
        elif command.lower() == "stats":
            self.player.get_stats()
        elif command.lower() == "test":
            self.dungeon.generate_level()
            self.dungeon.show_current_level()
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
        
        