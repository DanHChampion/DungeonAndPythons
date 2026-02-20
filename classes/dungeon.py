import random
from classes.enemy import Enemy
from classes.item import Item
from collections import defaultdict
from classes.player import Player
from utils import clear_console

class Dungeon:
    def __init__(self, player: Player):
        self.current_level = -1
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

    def move_player(self, direction_string: str):
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
            if 0 <= new_y < 32 and 0 <= new_x < 32 and (self.map[new_y][new_x] == '■' or isinstance(self.map[new_y][new_x], Item)):
                # Check if the cell contains an Item instance
                if isinstance(self.map[new_y][new_x], Item):
                    if len(self.player.inventory) >= 20:
                        self.log_messages.append("Your inventory is full! Can't pick up the item.")
                        break
                    self.log_messages.append(f"You picked up {self.map[new_y][new_x].name}[{self.map[new_y][new_x].level}]!")
                    self.player.add_to_inventory(self.map[new_y][new_x])
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
            
        clear_console()
        self.show_current_level()

    def scan_surroundings(self):
        y, x = self.player.position
        scan_range = 1
        directions = {
            (-1, 0): "N",
            (1, 0): "S",
            (0, -1): "W",
            (0, 1): "E",
            (-1, -1): "NW",
            (-1, 1): "NE",
            (1, -1): "SW",
            (1, 1): "SE"
        }
        for dy in range(-scan_range, scan_range + 1):
            for dx in range(-scan_range, scan_range + 1):
                scan_y = y + dy
                scan_x = x + dx
                if 0 <= scan_y < 32 and 0 <= scan_x < 32:
                    cell = self.map[scan_y][scan_x]
                    direction = directions.get((dy, dx), "")
                    if cell == '»':
                        self.log_messages.append(f"  {direction:2}: Staircase")
                    elif isinstance(cell, Enemy):
                        self.log_messages.append(f"  {direction:2}: Enemy - {cell.name}[{cell.level}]")
                    elif isinstance(cell, Item):
                        self.log_messages.append(f"  {direction:2}: Item - {cell.name}[{cell.level}]")
                    
        if not self.log_messages:
            self.log_messages.append("Nothing of interest nearby.")

    def drop_item(self, item_idx: str):
        if not item_idx.isdigit():
            self.log_messages.append(f"Invalid item index: {item_idx}")
            return
        item_idx = int(item_idx) - 1
        if not 0 <= item_idx < len(self.player.inventory):
            self.log_messages.append(f"Invalid item index: {item_idx}")
            return
        
        item = self.player.inventory[item_idx]
        y, x = self.player.position
        # Find a free adjacent square (including diagonals)
        found = False
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue
                ny, nx = y + dy, x + dx
                if 0 <= ny < 32 and 0 <= nx < 32 and self.map[ny][nx] == '■':
                    self.map[ny][nx] = item  # Place the item on the map
                    self.player.remove_from_inventory(item)
                    self.log_messages.append(f"You dropped {item.name}[{item.level}] at ({ny},{nx})!")
                    found = True
                    break
            if found:
                break
        if not found:
            self.log_messages.append("No free space next to you to drop the item!")


    def generate_level(self):
        self.current_level += 1
        self.map = [[' ' for _ in range(32)] for _ in range(32)]  # Empty 32x32 map
        # Number of rooms increases with level
        rooms = self.generate_rooms()  # Store (x1, y1, x2, y2) for each room
        room_center = [( (rx1 + rx2) // 2, (ry1 + ry2) // 2) for rx1, ry1, rx2, ry2 in rooms]
        self.connect_rooms(room_center)

        room_cells = []
        for rx1, ry1, rx2, ry2 in rooms:
            for y in range(ry1, ry2 + 1):
                for x in range(rx1, rx2 + 1):
                    if self.map[y][x] == '■':
                        room_cells.append((y, x))            

        self.place_stair(room_cells)
        self.place_player(room_cells)
        self.place_items(room_cells)
        self.place_enemies(room_cells)
        
    def generate_rooms(self):
        rooms = []
        num_rooms = min(20, self.current_level // 5 + 2)
        room_positions = []
        attempts = 0
        while len(room_positions) < num_rooms and attempts < num_rooms * 10:
            room_width = random.randint(3, 6)
            room_height = random.randint(3, 4)
            x = random.randint(1, 32 - room_width - 1)
            y = random.randint(1, 32 - room_height - 1)
            new_room = (x, y, x + room_width - 1, y + room_height - 1)

            # Check for overlap or adjacency (1 cell buffer)
            overlap = False
            for rx1, ry1, rx2, ry2 in rooms:
                # Expand existing room by 1 cell in all directions
                ex_rx1 = rx1 - 1
                ex_ry1 = ry1 - 1
                ex_rx2 = rx2 + 1
                ex_ry2 = ry2 + 1
                # Expand new room by 1 cell in all directions
                ex_nx1 = new_room[0] - 1
                ex_ny1 = new_room[1] - 1
                ex_nx2 = new_room[2] + 1
                ex_ny2 = new_room[3] + 1
                if not (ex_nx2 < ex_rx1 or ex_nx1 > ex_rx2 or ex_ny2 < ex_ry1 or ex_ny1 > ex_ry2):
                    overlap = True
                    break
            if not overlap:
                room_positions.append((x + room_width // 2, y + room_height // 2))
                rooms.append(new_room)
                for i in range(y, y + room_height):
                    for j in range(x, x + room_width):
                        self.map[i][j] = '■'  # Mark room floor
            attempts += 1
        return rooms
    
    def connect_rooms(self, room_centers: list):
        # Ensure every room has 1 connection to its closest room
        connections = defaultdict(set)
        for i, center in enumerate(room_centers):
            # Find the closest other room
            min_dist = float('inf')
            closest_j = None
            closest_center = None
            for j, other_center in enumerate(room_centers):
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

    def place_stair(self, room_cells: list[tuple[int, int]]):
        # Place the stair in a random valid cell inside a room (not corridor)
        stair_y, stair_x = random.choice(room_cells)
        self.map[stair_y][stair_x] = '»'  # Mark stair case

    def place_player(self, room_cells: list[tuple[int, int]]):
        # Place the player in a random valid cell inside a room (not corridor)
        player_cells = [(y, x) for (y, x) in room_cells if self.map[y][x] != '»']
        if player_cells:
            player_y, player_x = random.choice(player_cells)
            self.map[player_y][player_x] = self.player  # Mark player start
            self.player.position = (player_y, player_x)  # Update player position

    def place_items(self, room_cells: list[tuple[int, int]]):
        # Place items in random valid cells in rooms
        item_cells = [(y, x) for (y, x) in room_cells if self.map[y][x] == '■' and self.map[y][x] != '»']
        for _ in range(random.randint(1, 5)):
            if not item_cells:
                break
            item_y, item_x = random.choice(item_cells)
            min_level = max(1, self.current_level // 5)
            max_level = max(min_level, self.current_level // 2)
            random_level = random.randint(min_level, max_level)
            self.map[item_y][item_x] = Item(level=random_level)  # Mark item
            item_cells.remove((item_y, item_x))
    
    def place_enemies(self, room_cells: list[tuple[int, int]]):
        # Place enemies in random valid cells in rooms
        enemy_cells = [(y, x) for (y, x) in room_cells if self.map[y][x] == '■' and self.map[y][x] != '»']
        for _ in range(random.randint(1, 5)):
            if not enemy_cells:
                break
            enemy_y, enemy_x = random.choice(enemy_cells)
            # Ensure valid range for random_level
            min_level = max(1, self.current_level // 5)
            max_level = max(min_level, self.current_level // 2)
            random_level = random.randint(min_level, max_level)
            self.map[enemy_y][enemy_x] = Enemy(level=random_level)  # Mark enemy
            enemy_cells.remove((enemy_y, enemy_x))