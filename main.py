from classes.game import Game

if __name__ == "__main__":
    game = Game()
    game.start()
    while True:
        command = input(">> ")
        if command.lower() == "exit":
            game.stop()
            break
        game.parse_command(command)