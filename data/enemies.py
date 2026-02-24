"""
Enemy data for Dungeon & Pythons
Organized by difficulty tiers for different dungeon levels
"""

WEAK_ENEMIES = {
    "rat": {
        "name": "Rat",
        "base_stats": {
            "health": 15,
            "strength": 3,
            "defense": 0,
            "agility": 3,
            "intellect": 1,
        },
        "loot_table": ["health_potion"],
        "xp_reward": 5,
        "spawn_chance": 0.5
    },
    "goblin": {
        "name": "Goblin",
        "base_stats": {
            "health": 25,
            "strength": 6,
            "defense": 1,
            "agility": 6,
            "intellect": 2,
        },
        "loot_table": ["health_potion"],
        "xp_reward": 10,
        "spawn_chance": 0.5
    },
    "skeleton": {
        "name": "Skeleton",
        "base_stats": {
            "health": 30,
            "strength": 8,
            "defense": 2,
            "agility": 4,
            "intellect": 1,
        },
        "loot_table": ["health_potion"],
        "xp_reward": 15,
        "spawn_chance": 0.5
    },
    "cave_spider": {
        "name": "Cave Spider",
        "base_stats": {
            "health": 20,
            "strength": 5,
            "defense": 1,
            "agility": 10,
            "intellect": 1,
        },
        "loot_table": ["health_potion"],
        "xp_reward": 8,
        "spawn_chance": 0.5
    }
}

MEDIUM_ENEMIES = {
    "orc_warrior": {
        "name": "Orc Warrior",
        "base_stats": {
            "health": 60,
            "strength": 12,
            "defense": 4,
            "agility": 5,
            "intellect": 2,
        },
        "loot_table": ["health_potion"],
        "xp_reward": 35,
        "spawn_chance": 0.25
    },
    "dark_mage": {
        "name": "Dark Mage",
        "base_stats": {
            "health": 45,
            "strength": 12,
            "defense": 4,
            "agility": 5,
            "intellect": 2,
        },
        "loot_table": ["health_potion"],
        "xp_reward": 50,
        "spawn_chance": 0.25
    },
    "hobgoblin_captain": {
        "name": "Hobgoblin Captain",
        "base_stats": {
            "health": 75,
            "strength": 12,
            "defense": 4,
            "agility": 5,
            "intellect": 2,
        },
        "loot_table": ["health_potion"],
        "xp_reward": 60,
        "spawn_chance": 0.25
    },
    "giant_centipede": {
        "name": "Giant Centipede",
        "base_stats": {
            "health": 50,
            "strength": 12,
            "defense": 4,
            "agility": 5,
            "intellect": 2,
        },
        "loot_table": ["health_potion"],
        "xp_reward": 40,
        "spawn_chance": 0.25
    },
    "minotaur": {
        "name": "Minotaur",
        "base_stats": {
            "health": 90,
            "strength": 12,
            "defense": 4,
            "agility": 5,
            "intellect": 2,
        },
        "loot_table": ["health_potion"],
        "xp_reward": 100,
        "spawn_chance": 0.25
    }
}
STRONG_ENEMIES = {
    "stone_golem": {
        "name": "Stone Golem",
        "base_stats": {
            "health": 150,
            "strength": 20,
            "defense": 15,
            "agility": 2,
            "intellect": 1,
        },
        "loot_table": ["health_potion"],
        "xp_reward": 200,
        "spawn_chance": 0.1
    },
    "vampire": {
        "name": "Vampire",
        "base_stats": {
            "health": 120,
            "strength": 20,
            "defense": 5,
            "agility": 10,
            "intellect": 10,
        },
        "loot_table": ["health_potion"],
        "xp_reward": 300,
        "spawn_chance": 0.1
    },
    "fire_elemental": {
        "name": "Fire Elemental",
        "base_stats": {
            "health": 100,
            "strength": 20,
            "defense": 15,
            "agility": 2,
            "intellect": 1,
        },
        "loot_table": ["health_potion"],
        "xp_reward": 250,
        "spawn_chance": 0.1
    }
}

# Boss enemies
# BOSS_ENEMIES = [
#     {
#         "name": "Ancient Dragon",
#         "max_health": 500,
#         "level": 30,
#         "attack_power": 60,
#         "defense": 25,
#         "speed": 8,
#         "description": "A colossal dragon with scales like black steel.",
#         "loot_table": ["dragon_scale", "dragon_heart", "ancient_treasure"],
#         "xp_reward": 1000
#     },
#     {
#         "name": "Lich King",
#         "max_health": 300,
#         "level": 28,
#         "attack_power": 55,
#         "defense": 20,
#         "speed": 5,
#         "description": "An undead sorcerer-king of immense power.",
#         "loot_table": ["phylactery", "lich_crown", "necromantic_tome"],
#         "xp_reward": 800
#     },
#     {
#         "name": "Demon Prince",
#         "max_health": 400,
#         "level": 32,
#         "attack_power": 65,
#         "defense": 15,
#         "speed": 12,
#         "description": "A hellish prince from the depths of the abyss.",
#         "loot_table": ["demon_horn", "infernal_essence", "hellfire_gem"],
#         "xp_reward": 1200
#     },
#     {
#         "name": "Kraken",
#         "max_health": 600,
#         "level": 35,
#         "attack_power": 50,
#         "defense": 30,
#         "speed": 4,
#         "description": "A massive sea monster dwelling in flooded chambers.",
#         "loot_table": ["kraken_tentacle", "pearl_of_depths", "leviathan_scale"],
#         "xp_reward": 1500
#     }
# ]

# # Special/Unique enemies
# SPECIAL_ENEMIES = [
#     {
#         "name": "Treasure Mimic",
#         "max_health": 80,
#         "level": 15,
#         "attack_power": 20,
#         "defense": 12,
#         "speed": 3,
#         "description": "A chest that's actually a monster in disguise.",
#         "loot_table": ["mimic_adhesive", "fake_treasure", "real_treasure"],
#         "xp_reward": 150
#     },
#     {
#         "name": "Shadow Assassin",
#         "max_health": 60,
#         "level": 25,
#         "attack_power": 40,
#         "defense": 3,
#         "speed": 15,
#         "description": "A deadly killer that strikes from the shadows.",
#         "loot_table": ["shadow_blade", "assassin_garb", "poison_vial"],
#         "xp_reward": 400
#     },
#     {
#         "name": "Crystal Guardian",
#         "max_health": 200,
#         "level": 20,
#         "attack_power": 15,
#         "defense": 25,
#         "speed": 2,
#         "description": "A magical guardian protecting ancient crystals.",
#         "loot_table": ["power_crystal", "guardian_core", "crystal_shard"],
#         "xp_reward": 300
#     }
# ]

# Combine all enemies into one dictionary
ALL_ENEMIES = {
    "weak": WEAK_ENEMIES,
    "medium": MEDIUM_ENEMIES,
    "strong": STRONG_ENEMIES,
    # "boss": BOSS_ENEMIES,
    # "special": SPECIAL_ENEMIES
}
