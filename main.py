from classes.game import Game
from utils import clear_console

if __name__ == "__main__":
    clear_console()
    print("Welcome to Dungeon & Pythons!")
    input("Press Enter to start the game...")
    player_name = input("Enter your character's name: ") or "Hero"
    clear_console()
    game = Game()
    game.start(player_name)
    while True:
        command = input(">> ")
        if command.lower() == "exit":
            game.stop()
            break
        game.parse_command(command)