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
        "attack_bonus": 2,
        "durability": 20,
        "value": 5,
        "rarity": "common"
    },
    "rusty_sword": {
        "name": "Rusty Sword",
        "description": "An old iron sword with rust spots.",
        "type": "weapon",
        "subtype": "one_handed",
        "attack_bonus": 4,
        "durability": 30,
        "value": 15,
        "rarity": "common"
    },
    "iron_sword": {
        "name": "Iron Sword",
        "description": "A well-crafted iron blade.",
        "type": "weapon",
        "subtype": "one_handed",
        "attack_bonus": 8,
        "durability": 50,
        "value": 50,
        "rarity": "common"
    },
    "steel_sword": {
        "name": "Steel Sword",
        "description": "A sharp steel blade with excellent balance.",
        "type": "weapon",
        "subtype": "one_handed",
        "attack_bonus": 12,
        "durability": 75,
        "value": 150,
        "rarity": "uncommon"
    },
    "silver_sword": {
        "name": "Silver Sword",
        "description": "A blessed silver blade effective against undead.",
        "type": "weapon",
        "subtype": "one_handed",
        "attack_bonus": 10,
        "special_effect": "extra_damage_undead",
        "durability": 60,
        "value": 200,
        "rarity": "uncommon"
    },
    "enchanted_blade": {
        "name": "Enchanted Blade",
        "description": "A sword humming with magical energy.",
        "type": "weapon",
        "subtype": "one_handed",
        "attack_bonus": 15,
        "special_effect": "magic_damage",
        "durability": 100,
        "value": 500,
        "rarity": "rare"
    },
    
    # Two-handed weapons
    "battle_axe": {
        "name": "Battle Axe",
        "description": "A heavy two-handed axe for devastating attacks.",
        "type": "weapon",
        "subtype": "two_handed",
        "attack_bonus": 15,
        "durability": 60,
        "value": 80,
        "rarity": "common"
    },
    "giant_club": {
        "name": "Giant Club",
        "description": "A massive wooden club that crushes enemies.",
        "type": "weapon",
        "subtype": "two_handed",
        "attack_bonus": 18,
        "durability": 40,
        "value": 60,
        "rarity": "uncommon"
    },
    "warhammer": {
        "name": "Warhammer",
        "description": "A mighty hammer that can shatter armor.",
        "type": "weapon",
        "subtype": "two_handed",
        "attack_bonus": 20,
        "special_effect": "armor_piercing",
        "durability": 80,
        "value": 300,
        "rarity": "rare"
    },
    
    # Magical weapons
    "magic_staff": {
        "name": "Magic Staff",
        "description": "A staff that amplifies magical power.",
        "type": "weapon",
        "subtype": "staff",
        "attack_bonus": 6,
        "magic_bonus": 10,
        "durability": 45,
        "value": 120,
        "rarity": "uncommon"
    },
    "shadow_blade": {
        "name": "Shadow Blade",
        "description": "A blade forged from crystallized shadows.",
        "type": "weapon",
        "subtype": "one_handed",
        "attack_bonus": 16,
        "special_effect": "shadow_strike",
        "durability": 70,
        "value": 800,
        "rarity": "legendary"
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
        "defense_bonus": 1,
        "durability": 10,
        "value": 1,
        "rarity": "common"
    },
    "leather_armor": {
        "name": "Leather Armor",
        "description": "Flexible leather armor that allows good movement.",
        "type": "armor",
        "subtype": "body",
        "defense_bonus": 5,
        "speed_bonus": 1,
        "durability": 40,
        "value": 30,
        "rarity": "common"
    },
    "chainmail": {
        "name": "Chainmail",
        "description": "Interlocking metal rings that provide solid protection.",
        "type": "armor",
        "subtype": "body",
        "defense_bonus": 10,
        "speed_penalty": 1,
        "durability": 70,
        "value": 100,
        "rarity": "common"
    },
    "plate_armor": {
        "name": "Plate Armor",
        "description": "Heavy metal plates that offer excellent protection.",
        "type": "armor",
        "subtype": "body",
        "defense_bonus": 20,
        "speed_penalty": 2,
        "durability": 100,
        "value": 400,
        "rarity": "uncommon"
    },
    "dragon_scale_armor": {
        "name": "Dragon Scale Armor",
        "description": "Armor crafted from actual dragon scales.",
        "type": "armor",
        "subtype": "body",
        "defense_bonus": 45,
        "durability": 150,
        "value": 2000,
        "rarity": "legendary"
    }
}

# ACCESSORIES
ACCESSORIES = {
    "power_ring": {
        "name": "Power Ring",
        "description": "A ring that enhances the wearer's attack.",
        "type": "accessory",
        "subtype": "ring",
        "attack_bonus": 3,
        "value": 150,
        "rarity": "rare"
    },
    "protection_amulet": {
        "name": "Protection Amulet",
        "description": "An amulet that wards off harm.",
        "type": "accessory",
        "subtype": "amulet",
        "defense_bonus": 3,
        "value": 150,
        "rarity": "rare"
    },
    "magic_locket": {
        "name": "Magic Locket",
        "description": "A locket that boosts magical abilities.",
        "type": "accessory",
        "subtype": "amulet",
        "magic_bonus": 5,
        "value": 200,
        "rarity": "rare"
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
        "rarity": "common"
    },
    "mana_potion": {
        "name": "Mana Potion",
        "description": "A blue potion that restores magical energy.",
        "type": "consumable",
        "subtype": "potion",
        "effect": "restore_mana",
        "effect_value": 30,
        "value": 20,
        "rarity": "common"
    },
    "greater_health_potion": {
        "name": "Greater Health Potion",
        "description": "A powerful healing potion with enhanced effects.",
        "type": "consumable",
        "subtype": "potion",
        "effect": "heal",
        "effect_value": 100,
        "value": 75,
        "rarity": "uncommon"
    },
    "antidote": {
        "name": "Antidote",
        "description": "A green liquid that cures poison.",
        "type": "consumable",
        "subtype": "potion",
        "effect": "cure_poison",
        "value": 30,
        "rarity": "common"
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
