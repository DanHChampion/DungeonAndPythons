import random
from collections import defaultdict

class Dungeon:
    def __init__(self, player):
        self.current_level = 0
        self.map = [[' ' for _ in range(32)] for _ in range(32)]  # Empty 32x32 map
        self.log_messages = []
        self.player = player # Reference to the player object

    def show_current_level(self):
        print(f"{' ' * (32-len(str(self.current_level))//2)}B{self.current_level}")
        # Placeholder for map display logic
        for row in self.map:
            for cell in row:
                print(cell, end=' ')
            print()

    def move_player(self, direction_string):
        direction_string = direction_string.lower()
        for char in direction_string:
            if char not in "wasd":
                self.log_messages.append("Invalid move command! Use WASD for movement.")
                return
            dx, dy = 0, 0
            if char == 'w':
                dy = -1
            if char == 'a':
                dx = -1
            if char == 's':
                dy = 1
            if char == 'd':
                dx = 1

            new_y = self.player.position[0] + dy
            new_x = self.player.position[1] + dx
            if 0 <= new_y < 32 and 0 <= new_x < 32 and self.map[new_y][new_x] == '■':
                self.map[self.player.position[0]][self.player.position[1]] = '■'
                self.map[new_y][new_x] = self.player.character
                self.player.position = (new_y, new_x)  # Update player position
            elif 0 <= new_y < 32 and 0 <= new_x < 32 and self.map[new_y][new_x] == '»':
                self.map[self.player.position[0]][self.player.position[1]] = '■'
                self.map[new_y][new_x] = self.player.character
                self.log_messages.append(f"You descend to B{self.current_level + 1}!")
                self.generate_level()
                break
            else:
                self.log_messages.append("You can't move there!")
                break
            
        print("\033c", end="")  # Clear console
        self.show_current_level()

    def generate_level(self):
        self.current_level += 1
        self.map = [[' ' for _ in range(32)] for _ in range(32)]  # Empty 32x32 map
        # Number of rooms increases with level
        num_rooms = min(20, self.current_level // 5 + 2)
        room_positions = []
        rooms = []  # Store (x1, y1, x2, y2) for each room
        
        attempts = 0
        while len(room_positions) < num_rooms and attempts < num_rooms * 10:
            room_width = random.randint(3, 6)
            room_height = random.randint(3, 4)
            x = random.randint(1, 32 - room_width - 1)
            y = random.randint(1, 32 - room_height - 1)
            new_room = (x, y, x + room_width - 1, y + room_height - 1)

            # Check for overlap
            overlap = False
            for rx1, ry1, rx2, ry2 in rooms:
                if not (new_room[2] < rx1 or new_room[0] > rx2 or new_room[3] < ry1 or new_room[1] > ry2):
                    overlap = True
                    break
            if not overlap:
                room_positions.append((x + room_width // 2, y + room_height // 2))
                rooms.append(new_room)
                for i in range(y, y + room_height):
                    for j in range(x, x + room_width):
                        self.map[i][j] = '■'  # Mark room floor
            attempts += 1

        # Ensure every room has 1 connection to its closest room
        connections = defaultdict(set)
        for i, center in enumerate(room_positions):
            # Find the closest other room
            min_dist = float('inf')
            closest_j = None
            closest_center = None
            for j, other_center in enumerate(room_positions):
                if i == j:
                    continue
                dist = abs(center[0] - other_center[0]) + abs(center[1] - other_center[1])
                if dist < min_dist:
                    min_dist = dist
                    closest_j = j
                    closest_center = other_center
                if closest_j is not None and closest_j not in connections[i]:
                    # Draw horizontal corridor
                    for x in range(min(center[0], closest_center[0]), max(center[0], closest_center[0]) + 1):
                        self.map[center[1]][x] = '■'
                    # Draw vertical corridor
                    for y in range(min(center[1], closest_center[1]), max(center[1], closest_center[1]) + 1):
                        self.map[y][closest_center[0]] = '■'
                    connections[i].add(closest_j)
                    connections[closest_j].add(i)

        # place 1 stair case in a random valid cell inside a room (not corridor)
        room_cells = []
        for rx1, ry1, rx2, ry2 in rooms:
            for y in range(ry1, ry2 + 1):
                for x in range(rx1, rx2 + 1):
                    if self.map[y][x] == '■':
                        room_cells.append((y, x))
        if room_cells:
            stair_y, stair_x = random.choice(room_cells)
            self.map[stair_y][stair_x] = '»'  # Mark stair case

        # place the player in a random valid cell in a room (not the same as stair)
        player_cells = [(y, x) for (y, x) in room_cells if self.map[y][x] != '»']
        if player_cells:
            player_y, player_x = random.choice(player_cells)
            self.map[player_y][player_x] = self.player.character  # Mark player start
            self.player.position = (player_y, player_x)  # Update player position