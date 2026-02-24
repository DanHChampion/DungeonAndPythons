"""
Item data for Dungeon & Pythons
Organized by type: weapons, armor, accessories, consumables, materials
"""

# WEAPONS
WEAPONS = {
    # One-handed weapons
    "rusty_dagger": {
        "name": "Rusty Dagger",
        "description": "A corroded dagger that's seen better days.",
        "type": "weapon",
        "subtype": "one_handed",
        "base_stats": {
            "strength": 2
        },
        "accuracy": 0.95,
        "drop_chance": 0.5,
    },
    "rusty_sword": {
        "name": "Rusty Sword",
        "description": "An old iron sword with rust spots.",
        "type": "weapon",
        "subtype": "one_handed",
        "base_stats": {
            "strength": 4
        },
        "accuracy": 0.95,
        "drop_chance": 0.5,
    },
    "iron_sword": {
        "name": "Iron Sword",
        "description": "A well-crafted iron blade.",
        "type": "weapon",
        "subtype": "one_handed",
        "base_stats": {
            "strength": 8
        },
        "accuracy": 0.95,
        "drop_chance": 0.5,
    },
    "steel_sword": {
        "name": "Steel Sword",
        "description": "A sharp steel blade with excellent balance.",
        "type": "weapon",
        "subtype": "one_handed",
        "base_stats": {
            "strength": 12
        },
        "durability": 75,
        "drop_chance": 0.25,
    },
    "silver_sword": {
        "name": "Silver Sword",
        "description": "A blessed silver blade effective against undead.",
        "type": "weapon",
        "subtype": "one_handed",
        "base_stats": {
            "strength": 10
        },
        "special_effect": "extra_damage_undead",
        "accuracy": 0.9,
        "drop_chance": 0.25,
    },
    "enchanted_blade": {
        "name": "Enchanted Blade",
        "description": "A sword humming with magical energy.",
        "type": "weapon",
        "subtype": "one_handed",
        "base_stats": {
            "strength": 15
        },
        "accuracy": 0.95,
        "special_effect": "magic_damage",
        "drop_chance": 0.1,
    },
    
    # Two-handed weapons
    "battle_axe": {
        "name": "Battle Axe",
        "description": "A heavy two-handed axe for devastating attacks.",
        "type": "weapon",
        "subtype": "two_handed",
        "base_stats": {
            "strength": 12
        },
        "accuracy": 0.8,
        "drop_chance": 0.5,
    },
    "giant_club": {
        "name": "Giant Club",
        "description": "A massive wooden club that crushes enemies.",
        "type": "weapon",
        "subtype": "two_handed",
        "base_stats": {
            "strength": 18
        },
        "accuracy": 0.8,
        "drop_chance": 0.25,
    },
    "warhammer": {
        "name": "Warhammer",
        "description": "A mighty hammer that can shatter armor.",
        "type": "weapon",
        "subtype": "two_handed",
        "base_stats": {
            "strength": 30
        },
        "accuracy": 0.8,
        "special_effect": "armor_piercing",
        "drop_chance": 0.1,
    },
    
    # Magical weapons
    "magic_staff": {
        "name": "Magic Staff",
        "description": "A staff that amplifies magical power.",
        "type": "weapon",
        "subtype": "staff",
        "base_stats": {
            "strength": 2,
            "intellect": 5
        },
        "accuracy": 0.9,
        "magic_bonus": 10,
        "drop_chance": 0.25,
    },
    "shadow_blade": {
        "name": "Shadow Blade",
        "description": "A blade forged from crystallized shadows.",
        "type": "weapon",
        "subtype": "one_handed",
        "base_stats": {
            "strength": 12,
            "intellect": 16
        },
        "accuracy": 0.9,
        "special_effect": "shadow_strike",
        "drop_chance": 0.05,
    }
}

# ARMOR
ARMOR = {    
    # Body armor
    "tattered_clothes": {
        "name": "Tattered Clothes",
        "description": "Worn and torn clothing that offers little protection.",
        "type": "armor",
        "subtype": "body",
        "base_stats": {
            "defense": 1
        },
        "drop_chance": 0.5
    },
    "leather_armor": {
        "name": "Leather Armor",
        "description": "Flexible leather armor that allows good movement.",
        "type": "armor",
        "subtype": "body",
        "base_stats": {
            "defense": 5
        },
        "drop_chance": 0.5
    },
    "chainmail": {
        "name": "Chainmail",
        "description": "Interlocking metal rings that provide solid protection.",
        "type": "armor",
        "subtype": "body",
        "base_stats": {
            "defense": 10
        },
        "drop_chance": 0.5
    },
    "plate_armor": {
        "name": "Plate Armor",
        "description": "Heavy metal plates that offer excellent protection.",
        "type": "armor",
        "subtype": "body",
        "base_stats": {
            "defense": 20
        },
        "drop_chance": 0.25
    },
    "dragon_scale_armor": {
        "name": "Dragon Scale Armor",
        "description": "Armor crafted from actual dragon scales.",
        "type": "armor",
        "subtype": "body",
        "base_stats": {
            "defense": 45
        },
        "drop_chance": 0.05
    }
}

# ACCESSORIES
ACCESSORIES = {
    "power_ring": {
        "name": "Power Ring",
        "description": "A ring that enhances the wearer's attack.",
        "type": "accessory",
        "subtype": "ring",
        "base_stats": {
            "strength": 1
        },
        "drop_chance": 0.1
    },
    "protection_amulet": {
        "name": "Protection Amulet",
        "description": "An amulet that wards off harm.",
        "type": "accessory",
        "subtype": "amulet",
        "base_stats": {
            "defense": 3
        },
        "drop_chance": 0.1
    },
    "magic_locket": {
        "name": "Magic Locket",
        "description": "A locket that boosts magical abilities.",
        "type": "accessory",
        "subtype": "amulet",
        "base_stats": {
            "intellect": 5
        },
        "drop_chance": 0.1
    }
}

# CONSUMABLES
CONSUMABLES = {
    "health_potion": {
        "name": "Health Potion",
        "description": "A red potion that restores health when consumed.",
        "type": "consumable",
        "subtype": "potion",
        "effect": "heal",
        "effect_value": 50,
        "value": 25,
        "drop_chance": 0.5
    },
    "greater_health_potion": {
        "name": "Greater Health Potion",
        "description": "A powerful healing potion with enhanced effects.",
        "type": "consumable",
        "subtype": "potion",
        "effect": "heal",
        "effect_value": 100,
        "drop_chance": 0.25
    }
}

# # MATERIALS AND CRAFTING ITEMS
# MATERIALS = {
#     "copper_coin": {
#         "name": "Copper Coin",
#         "description": "A basic copper coin used as currency.",
#         "type": "material",
#         "subtype": "currency",
#         "value": 1,
#         "rarity": "common"
#     },
#     "silver_coin": {
#         "name": "Silver Coin",
#         "description": "A valuable silver coin.",
#         "type": "material",
#         "subtype": "currency",
#         "value": 10,
#         "rarity": "common"
#     },
#     "gold_coin": {
#         "name": "Gold Coin",
#         "description": "A precious gold coin.",
#         "type": "material",
#         "subtype": "currency",
#         "value": 100,
#         "rarity": "uncommon"
#     },
#     "platinum_coin": {
#         "name": "Platinum Coin",
#         "description": "An extremely valuable platinum coin.",
#         "type": "material",
#         "subtype": "currency",
#         "value": 1000,
#         "rarity": "rare"
#     },
    
#     # Crafting materials
#     "spider_silk": {
#         "name": "Spider Silk",
#         "description": "Strong silk thread from a giant spider.",
#         "type": "material",
#         "subtype": "crafting",
#         "value": 8,
#         "rarity": "common"
#     },
#     "venom_sac": {
#         "name": "Venom Sac",
#         "description": "A poison gland from a venomous creature.",
#         "type": "material",
#         "subtype": "crafting",
#         "value": 15,
#         "rarity": "uncommon"
#     },
#     "dragon_scale": {
#         "name": "Dragon Scale",
#         "description": "An incredibly tough scale from an ancient dragon.",
#         "type": "material",
#         "subtype": "crafting",
#         "value": 500,
#         "rarity": "legendary"
#     },
#     "mana_crystal": {
#         "name": "Mana Crystal",
#         "description": "A crystallized form of pure magical energy.",
#         "type": "material",
#         "subtype": "crafting",
#         "value": 100,
#         "rarity": "rare"
#     },
#     "bone": {
#         "name": "Bone",
#         "description": "A sturdy bone that could be used for crafting.",
#         "type": "material",
#         "subtype": "crafting",
#         "value": 3,
#         "rarity": "common"
#     },
#     "leather_hide": {
#         "name": "Leather Hide",
#         "description": "A piece of treated leather suitable for armor.",
#         "type": "material",
#         "subtype": "crafting",
#         "value": 12,
#         "rarity": "common"
#     },
#     "iron_ore": {
#         "name": "Iron Ore",
#         "description": "Raw iron that can be smelted into metal.",
#         "type": "material",
#         "subtype": "crafting",
#         "value": 5,
#         "rarity": "common"
#     },
#     "gem_ruby": {
#         "name": "Ruby",
#         "description": "A precious red gemstone.",
#         "type": "material",
#         "subtype": "gem",
#         "value": 200,
#         "rarity": "rare"
#     },
#     "gem_emerald": {
#         "name": "Emerald",
#         "description": "A precious green gemstone.",
#         "type": "material",
#         "subtype": "gem",
#         "value": 250,
#         "rarity": "rare"
#     },
#     "gem_diamond": {
#         "name": "Diamond",
#         "description": "The hardest and most precious gemstone.",
#         "type": "material",
#         "subtype": "gem",
#         "value": 500,
#         "rarity": "legendary"
#     }
# }

# Combine all items into one dictionary
ALL_ITEMS = {
    "weapons": WEAPONS,
    "armor": ARMOR,
    "accessories": ACCESSORIES,
    "consumables": CONSUMABLES,
    # "materials": MATERIALS,
}

# Item rarity colors for display
RARITY_COLORS = {
    "common": "white",
    "uncommon": "green", 
    "rare": "blue",
    "epic": "purple",
    "legendary": "orange",
    "unique": "red"
}
