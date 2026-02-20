"""
Enemy data for Dungeon & Pythons
Organized by difficulty tiers for different dungeon levels
"""

# Weak enemies
WEAK_ENEMIES = {
    "rat": {
        "name": "Rat",
        "max_health": 15,
        "base_stats": {
            "strength": 3,
            "defense": 0,
            "agility": 3,
            "intellect": 1,
        },
        "loot_table": [],
        "exp_reward": 5
    },
    "goblin": {
        "name": "Goblin",
        "max_health": 25,
        "base_stats": {
            "strength": 6,
            "defense": 1,
            "agility": 6,
            "intellect": 2,
        },
        "loot_table": [],
        "exp_reward": 10
    },
    "skeleton": {
        "name": "Skeleton",
        "max_health": 30,
        "base_stats": {
            "strength": 8,
            "defense": 2,
            "agility": 4,
            "intellect": 1,
        },
        "loot_table": [],
        "exp_reward": 15
    },
    "cave_spider": {
        "name": "Cave Spider",
        "max_health": 20,
        "attack_power": 5,
        "base_stats": {
            "strength": 5,
            "defense": 1,
            "agility": 10,
            "intellect": 1,
        },
        "loot_table": [],
        "exp_reward": 8
    }
}

# Medium enemies
MEDIUM_ENEMIES = {
    "orc_warrior": {
        "name": "Orc Warrior",
        "max_health": 60,
        "base_stats": {
            "strength": 12,
            "defense": 4,
            "agility": 5,
            "intellect": 2,
        },
        "loot_table": [],
        "exp_reward": 35
    },
    "dark_mage": {
        "name": "Dark Mage",
        "max_health": 45,
        "base_stats": {
            "strength": 12,
            "defense": 4,
            "agility": 5,
            "intellect": 2,
        },
        "loot_table": [],
        "exp_reward": 50
    },
    "hobgoblin_captain": {
        "name": "Hobgoblin Captain",
        "max_health": 75,
        "base_stats": {
            "strength": 12,
            "defense": 4,
            "agility": 5,
            "intellect": 2,
        },
        "loot_table": [],
        "exp_reward": 60
    },
    "giant_centipede": {
        "name": "Giant Centipede",
        "max_health": 50,
       "base_stats": {
            "strength": 12,
            "defense": 4,
            "agility": 5,
            "intellect": 2,
        },
        "loot_table": [],
        "exp_reward": 40
    },
    "minotaur": {
        "name": "Minotaur",
        "max_health": 90,
        "base_stats": {
            "strength": 12,
            "defense": 4,
            "agility": 5,
            "intellect": 2,
        },
        "loot_table": [],
        "exp_reward": 100
    }
}

# Strong enemies
STRONG_ENEMIES = {
    "stone_golem": {
        "name": "Stone Golem",
        "max_health": 150,
        "base_stats": {
            "strength": 20,
            "defense": 15,
            "agility": 2,
            "intellect": 1,
        },
        "loot_table": [],
        "exp_reward": 200
    },
    "vampire": {
        "name": "Vampire",
        "max_health": 120,
        "base_stats": {
            "strength": 20,
            "defense": 5,
            "agility": 10,
            "intellect": 10,
        },
        "loot_table": [],
        "exp_reward": 300
    },
    "fire_elemental": {
        "name": "Fire Elemental",
        "max_health": 100,
        "base_stats": {
            "strength": 20,
            "defense": 15,
            "agility": 2,
            "intellect": 1,
        },
        "loot_table": [],
        "exp_reward": 250
    }
}

# Boss enemies (levels 26+)
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
#         "exp_reward": 1000
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
#         "exp_reward": 800
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
#         "exp_reward": 1200
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
#         "exp_reward": 1500
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
#         "exp_reward": 150
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
#         "exp_reward": 400
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
#         "exp_reward": 300
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
