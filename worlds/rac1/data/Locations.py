from dataclasses import dataclass
from typing import Callable, Optional

from ..Logic import *
from ..constants.pools import RAC1POOL

DEFAULT_LIST = list(
    [RAC1POOL.WEAPONS, RAC1POOL.GADGETS, RAC1POOL.PACKS, RAC1POOL.HELMETS, RAC1POOL.BOOTS, RAC1POOL.EXTRA_ITEMS, RAC1POOL.GOLD_BOLTS, RAC1POOL.INFOBOTS])
ALL_POOLS = list(
    [RAC1POOL.START_PLANET, RAC1POOL.START_ITEM, RAC1POOL.WEAPONS, RAC1POOL.GOLD_WEAPONS, RAC1POOL.GADGETS, RAC1POOL.PACKS, RAC1POOL.HELMETS,
     RAC1POOL.BOOTS, RAC1POOL.EXTRA_ITEMS, RAC1POOL.GOLD_BOLTS, RAC1POOL.INFOBOTS, RAC1POOL.SKILLPOINT])

# noinspection PyCompatibility
@dataclass
class LocationData:
    location_id: Optional[int]
    planet: str
    name: str
    vanilla_item: Optional[str]
    pools: set[str] = frozenset()
    """All of these must be enabled for this spot to be randomized"""
    access_rule: Optional[Callable[[CollectionState, int], bool]] = None


# General
HOVERBOARD_TRICKY = LocationData(
    112, "General", "Hoverboard: Skillpoint: Tricky", Items.TRICKY.name, {RAC1POOL.SKILLPOINT})

# Novalis
NOVALIS_PLUMBER = LocationData(
    1, "Novalis", "Novalis: Plumber", Items.ARIDIA_INFOBOT.name, {RAC1POOL.INFOBOTS})
NOVALIS_MAYOR = LocationData(
    2, "Novalis", "Novalis: Chairman", Items.KERWAN_INFOBOT.name, {RAC1POOL.INFOBOTS})
NOVALIS_VENDOR_PYROCITOR = LocationData(
    3, "Novalis", "Novalis: Vendor - 2,500", Items.PYROCITOR.name, {RAC1POOL.WEAPONS})
NOVALIS_SEWER_GOLD_BOLT = LocationData(
    4, "Novalis", "Novalis: Gold Bolt: Waterworks", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS})
NOVALIS_CAVES_GOLD_BOLT = LocationData(
    5, "Novalis", "Novalis: Gold Bolt: Caves", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, novalis_cave_gb_rule)
NOVALIS_UNDERWATER_CAVES_GOLD_BOLT = LocationData(
    6, "Novalis", "Novalis: Gold Bolt: Amoeboid Caves", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    novalis_underwater_caves_rule)
# Golden Weapon Locations
NOVALIS_GOLD_WEAPON_1 = LocationData(
    100, "Novalis", "Novalis: Golden Weapon 1 - 60,000", Items.GOLD_TESLA_CLAW.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_60k)
NOVALIS_GOLD_WEAPON_2 = LocationData(
    95, "Novalis", "Novalis: Golden Weapon 2 - 20,000", Items.GOLD_BOMB_GLOVE.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_20k)
NOVALIS_GOLD_WEAPON_3 = LocationData(
    101, "Novalis", "Novalis: Golden Weapon 3 - 60,000", Items.GOLD_DEVASTATOR.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_60k)
NOVALIS_GOLD_WEAPON_4 = LocationData(
    96, "Novalis", "Novalis: Golden Weapon 4 - 30,000", Items.GOLD_PYROCITOR.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_30k)
NOVALIS_GOLD_WEAPON_5 = LocationData(
    102, "Novalis", "Novalis: Golden Weapon 5 - 10,000", Items.GOLD_MINE_GLOVE.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_10k)
NOVALIS_GOLD_WEAPON_6 = LocationData(
    97, "Novalis", "Novalis: Golden Weapon 6 - 20,000", Items.GOLD_BLASTER.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_20k)
NOVALIS_GOLD_WEAPON_7 = LocationData(
    103, "Novalis", "Novalis: Golden Weapon 7 - 20,000", Items.GOLD_MORPH_O_RAY.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_20k)
NOVALIS_GOLD_WEAPON_8 = LocationData(
    98, "Novalis", "Novalis: Golden Weapon 8 - 10,000", Items.GOLD_GLOVE_OF_DOOM.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_10k)
NOVALIS_GOLD_WEAPON_9 = LocationData(
    104, "Novalis", "Novalis: Golden Weapon 9 - 10,000", Items.GOLD_DECOY_GLOVE.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_10k)
NOVALIS_GOLD_WEAPON_10 = LocationData(
    99, "Novalis", "Novalis: Golden Weapon 10 - 10,000", Items.GOLD_SUCK_CANNON.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_10k)
NOVALIS_SKILLPOINT = LocationData(
    105, "Novalis", "Novalis: Skillpoint: Take Aim", Items.TAKE_AIM.name, {RAC1POOL.SKILLPOINT}, has_medium_range_weapon)

# Aridia
ARIDIA_HOVERBOARD = LocationData(
    7, "Aridia", "Aridia: Kill the Sand Sharks", Items.HOVERBOARD.name, {RAC1POOL.EXTRA_ITEMS})
ARIDIA_TRESPASSER = LocationData(
    8, "Aridia", "Aridia: Construction Zone", Items.TRESPASSER.name, {RAC1POOL.GADGETS}, aridia_trespasser_rule)
ARIDIA_SONIC_SUMMONER = LocationData(
    9, "Aridia", "Aridia: Bring Zoomerator to Agent", Items.SONIC_SUMMONER.name, {RAC1POOL.HELMETS}, has_zoomerator)
ARIDIA_TRESPASSER_GOLD_BOLT = LocationData(
    10, "Aridia", "Aridia: Gold Bolt: Construction Zone", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    aridia_trespasser_rule)
ARIDIA_ISLAND_GOLD_BOLT = LocationData(
    11, "Aridia", "Aridia: Gold bolt: Island", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS})
ARIDIA_MAGNEBOOTS_GOLD_BOLT = LocationData(
    12, "Aridia", "Aridia: Gold Bolt: Laser", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, aridia_laser_rule)
ARIDIA_SANDSHARK_GOLD_BOLT = LocationData(
    13, "Aridia", "Aridia: Gold bolt: Sandshark Cave", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, aridia_cave_rule)
ARIDIA_SWING_IT = LocationData(
    106, "Aridia", "Aridia: Skillpoint: Swing it", Items.SWING_IT.name, {RAC1POOL.SKILLPOINT}, has_swingshot)
ARIDIA_TRANSPORTED = LocationData(
    107, "Aridia", "Aridia: Skillpoint: Transported", Items.TRANSPORTED.name, {RAC1POOL.SKILLPOINT},
    has_medium_range_weapon)

# Kerwan
KERWAN_SWINGSHOT = LocationData(
    14, "Kerwan", "Kerwan: Fitness Course", Items.SWINGSHOT.name, {RAC1POOL.GADGETS})
KERWAN_HELIPACK = LocationData(
    15, "Kerwan", "Kerwan: Al's Roboshack", Items.HELI_PACK.name, {RAC1POOL.PACKS})
KERWAN_TRAIN_INFOBOT = LocationData(
    16, "Kerwan", "Kerwan: Ride the Robot Train", Items.EUDORA_INFOBOT.name, {RAC1POOL.INFOBOTS}, kerwan_train_rule)
KERWAN_VENDOR_BLASTER = LocationData(
    17, "Kerwan", "Kerwan: Vendor - 2,500", Items.BLASTER.name, {RAC1POOL.WEAPONS})
KERWAN_BELOW_SHIP_GOLD_BOLT = LocationData(
    18, "Kerwan", "Kerwan: Gold Bolt: Underpass", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS})
KERWAN_TRAIN_STATION_GOLD_BOLT = LocationData(
    19, "Kerwan", "Kerwan: Gold Bolt: Train Station", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, kerwan_train_rule)
KERWAN_LONE_TOWER_GOLD_BOLT = LocationData(
    20, "Kerwan", "Kerwan: Gold Bolt: Fitness Course Tower", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    kerwan_course_gb_rule)
KERWAN_STRIKE_A_POSE = LocationData(
    108, "Kerwan", "Kerwan: Skillpoint: Strike A Pose", Items.STRIKE_A_POSE.name, {RAC1POOL.SKILLPOINT}, can_glide)
KERWAN_BLIMPY = LocationData(
    109, "Kerwan", "Kerwan: Skillpoint: Blimpy", Items.BLIMPY.name, {RAC1POOL.SKILLPOINT}, has_long_range_weapon)
KERWAN_QWARKTASTIC = LocationData(
    110, "Kerwan", "Kerwan: Skillpoint: Qwarktastic", Items.QWARKTASTIC.name, {RAC1POOL.SKILLPOINT}, has_explosive_weapon)

# Eudora
EUDORA_HENCHMAN = LocationData(
    21, "Eudora", "Eudora: Robot Lieutenant", Items.BLARG_INFOBOT.name, {RAC1POOL.INFOBOTS}, eudora_henchman_rule)
EUDORA_SUCK_CANNON = LocationData(
    22, "Eudora", "Eudora: Explore the Mills", Items.SUCK_CANNON.name, {RAC1POOL.WEAPONS}, eudora_suck_cannon_rule)
EUDORA_VENDOR_GLOVE_OF_DOOM = LocationData(
    23, "Eudora", "Eudora: Vendor - 7,500", Items.GLOVE_OF_DOOM.name, {RAC1POOL.WEAPONS}, has_7500_bolts)
EUDORA_GOLD_BOLT = LocationData(
    24, "Eudora", "Eudora: Gold Bolt", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, can_heli_high_jump)
EUDORA_ANY_TEN = LocationData(
    111, "Eudora", "Eudora: Skillpoint: Any Ten", Items.ANY_TEN.name, {RAC1POOL.SKILLPOINT}, eudora_skillpoint_rule)

# Rilgar
RILGAR_QUARK_INFOBOT = LocationData(
    25, "Rilgar", "Rilgar: Locate Captain Quark", Items.UMBRIS_INFOBOT.name, {RAC1POOL.INFOBOTS}, rilgar_bouncer_rule)
RILGAR_PLATINUM_ZOOMERATOR = LocationData(
    26, "Rilgar", "Rilgar: Win the hoverboard race", Items.ZOOMERATOR.name, {RAC1POOL.EXTRA_ITEMS}, rilgar_hoverboard_rule)
RILGAR_MINE_GLOVE = LocationData(
    27, "Rilgar", "Rilgar: Vendor - 7,500", Items.MINE_GLOVE.name, {RAC1POOL.WEAPONS}, has_7500_bolts)
RILGAR_RYNO = LocationData(
    28, "Rilgar", "Rilgar: Shady Salesman - 150,000", Items.RYNO.name, {RAC1POOL.WEAPONS}, rilgar_ryno_rule)
RILGAR_MAZE_GOLD_BOLT = LocationData(
    29, "Rilgar", "Rilgar: Gold Bolt: Maze", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, can_improved_jump)
RILGAR_WATERWORKS_GOLD_BOLT = LocationData(
    30, "Rilgar", "Rilgar: Gold Bolt: Sewer Cave", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, rilgar_underwater_bolt_rule)
RILGAR_CLUCK_CLUCK = LocationData(
    113, "Rilgar", "Rilgar: Skillpoint: Cluck Cluck", Items.CLUCK_CLUCK.name, {RAC1POOL.SKILLPOINT}, has_morph)
RILGAR_SPEEDY = LocationData(
    114, "Rilgar", "Rilgar: Skillpoint: Speedy", Items.SPEEDY.name, {RAC1POOL.SKILLPOINT}, rilgar_hoverboard_rule)

# Blarg
BLARG_HYDRODISPLACER = LocationData(
    31, "Blarg", "Blarg: Outside as Clank", Items.HYDRODISPLACER.name, {RAC1POOL.GADGETS}, has_trespasser)
BLARG_EXPLOSION_INFOBOT = LocationData(
    32, "Blarg", "Blarg: Destroy the Warship", Items.RILGAR_INFOBOT.name, {RAC1POOL.INFOBOTS})
BLARG_GRINDBOOTS = LocationData(
    33, "Blarg", "Blarg: Explore the Space Station", Items.GRINDBOOTS.name, {RAC1POOL.BOOTS}, has_swingshot)
BLARG_VENDOR_TAUNTER = LocationData(
    34, "Blarg", "Blarg: Vendor - 2,500", Items.TAUNTER.name, {RAC1POOL.WEAPONS})
BLARG_OUTSIDE_GOLD_BOLT = LocationData(
    35, "Blarg", "Blarg: Gold Bolt: Outside", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, blarg_outside_gold_bolt_rule)
BLARG_SWARMER_GOLD_BOLT = LocationData(
    36, "Blarg", "Blarg: Gold Bolt: Cages", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, has_swingshot)
BLARG_GIRL_TROUBLE = LocationData(
    115, "Blarg", "Blarg: Skillpoint: Girl Trouble", Items.GIRL_TROUBLE.name, {RAC1POOL.SKILLPOINT}, has_swingshot)

# Umbris
UMBRIS_SNAGGLEBEAST_INFOBOT = LocationData(
    37, "Umbris", "Umbris: Defeat the Snagglebeast", Items.BATALIA_INFOBOT.name, {RAC1POOL.INFOBOTS},
    umbris_snagglebeast_rule)
UMBRIS_PRESSURE_PUZZLE_GOLD_BOLT = LocationData(
    38, "Umbris", "Umbris: Gold Bolt: Lighthouse puzzle", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    umbris_pressure_bolt_rule)
UMBRIS_JUMP_DOWN_GOLD_BOLT = LocationData(
    39, "Umbris", "Umbris: Gold bolt: Jumping Down", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, umbris_jump_bolt_rule)

# Batalia
BATALIA_VENDOR_DEVASTATOR = LocationData(
    40, "Batalia", "Batalia: Vendor - 10,000", Items.DEVASTATOR.name, {RAC1POOL.WEAPONS}, has_10k_bolts)
BATALIA_GRINDRAIL_INFOBOT = LocationData(
    41, "Batalia", "Batalia: Ride the grindrail", Items.GASPAR_INFOBOT.name, {RAC1POOL.INFOBOTS}, has_grindboots)
BATALIA_COMMANDER_INFOBOT = LocationData(
    42, "Batalia", "Batalia: Commando", Items.ORXON_INFOBOT.name, {RAC1POOL.INFOBOTS})
BATALIA_METAL_DETECTOR = LocationData(
    43, "Batalia", "Batalia: Shoot down the Bombers", Items.METAL_DETECTOR.name, {RAC1POOL.GADGETS}, has_magneboots)
BATALIA_CLIFFSIDE_GOLD_BOLT = LocationData(
    44, "Batalia", "Batalia: Gold Bolt: Cliffside", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, can_improved_jump)
BATALIA_TRESPASSER_GOLD_BOLT = LocationData(
    45, "Batalia", "Batalia: Gold Bolt: House Roof", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS})
BATALIA_JUMPER = LocationData(
    116, "Batalia", "Batalia: Skillpoint: Jumper", Items.JUMPER.name, {RAC1POOL.SKILLPOINT}, has_grindboots)
BATALIA_ACCURACY_COUNTS = LocationData(
    117, "Batalia", "Batalia: Skillpoint: Accuracy Counts", Items.ACCURACY_COUNTS.name, {RAC1POOL.SKILLPOINT},
    has_magneboots)
BATALIA_EAT_LEAD = LocationData(
    118, "Batalia", "Batalia: Skillpoint: Eat Lead", Items.EAT_LEAD.name, {RAC1POOL.SKILLPOINT}, has_sonic)

# Gaspar
GASPAR_VENDOR_WALLOPER = LocationData(
    46, "Gaspar", "Gaspar: Vendor - 7,500", Items.WALLOPER.name, {RAC1POOL.WEAPONS}, has_7500_bolts)
GASPAR_PILOT_HELMET = LocationData(
    47, "Gaspar", "Gaspar: Get the pilot helmet", Items.PILOTS_HELMET.name, {RAC1POOL.HELMETS})
GASPAR_SWINGSHOT_GOLD_BOLT = (LocationData(
    48, "Gaspar", "Gaspar: Gold Bolt: Destroy the Bombers", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, has_swingshot))
GASPAR_VOLCANO_GOLD_BOLT = LocationData(
    49, "Gaspar", "Gaspar: Gold Bolt: Volcano", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, can_improved_jump)
GASPAR_DESTROYED = LocationData(
    119, "Gaspar", "Gaspar: Skillpoint: Destroyed", Items.DESTROYED.name, {RAC1POOL.SKILLPOINT}, gaspar_skillpoint_rule)
GASPAR_GUNNER = LocationData(
    120, "Gaspar", "Gaspar: Skillpoint: Gunner", Items.GUNNER.name, {RAC1POOL.SKILLPOINT})

# Orxon
ORXON_VENDOR_VISIBOMB = LocationData(
    50, "Orxon", "Orxon: Vendor - 15,000", Items.VISIBOMB.name, {RAC1POOL.WEAPONS}, orxon_visibomb_rule)
ORXON_CLANK_INFOBOT = LocationData(
    51, "Orxon", "Orxon: Clank: Traverse the Wilderness", Items.POKITARU_INFOBOT.name, {RAC1POOL.INFOBOTS})
ORXON_RATCHET_INFOBOT = LocationData(
    52, "Orxon", "Orxon: Chase the Infobot", Items.HOVEN_INFOBOT.name, {RAC1POOL.INFOBOTS}, orxon_ratchet_infobot_rule)
ORXON_CLANK_MAGNEBOOTS = LocationData(
    53, "Orxon", "Orxon: Clank: Search the Labs", Items.MAGNEBOOTS.name, {RAC1POOL.BOOTS})
ORXON_PREMIUM_NANOTECH = LocationData(
    54, "Orxon", "Orxon: Buy the premium nanotech - 4,000", Items.PREMIUM_NANOTECH.name, {RAC1POOL.EXTRA_ITEMS},
    orxon_nanotech_rule)
ORXON_ULTRA_NANOTECH = LocationData(
    55, "Orxon", "Orxon: Buy the ultra nanotech - 30,000", Items.ULTRA_NANOTECH.name, {RAC1POOL.EXTRA_ITEMS},
    orxon_ultra_nanotech_rule)
ORXON_CLANK_GOLD_BOLT = LocationData(
    56, "Orxon", "Orxon: Gold Bolt: Return to the Clank section", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, has_o2_mask)
ORXON_VISIBOMB_GOLD_BOLT = LocationData(
    57, "Orxon", "Orxon: Gold Bolt: Long Tunnel", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, orxon_visibomb_bolt_rule)
ORXON_SNIPER = LocationData(
    121, "Orxon", "Orxon: Skillpoint: Sniper", Items.SNIPER.name, {RAC1POOL.SKILLPOINT}, orxon_sniper_rule)
ORXON_HEY_OVER_HERE = LocationData(
    122, "Orxon", "Orxon: Skillpoint: Hey Over Here", Items.HEY_OVER_HERE.name, {RAC1POOL.SKILLPOINT},
    orxon_hey_over_here_rule)

# Pokitaru
POKITARU_VENDOR_DECOY_GLOVE = LocationData(
    58, "Pokitaru", "Pokitaru: Vendor - 7,500", Items.DECOY_GLOVE.name, {RAC1POOL.WEAPONS}, has_7500_bolts)
POKITARU_O2_MASK = LocationData(
    59, "Pokitaru", "Pokitaru: Pilot the Ship", Items.O2_MASK.name, {RAC1POOL.HELMETS}, pokitaru_ship_rule)
POKITARU_SEWER_PERSUADER = LocationData(
    60, "Pokitaru", "Pokitaru: Trade Raritanium", Items.PERSUADER.name, {RAC1POOL.EXTRA_ITEMS}, pokitaru_persuader_rule)
POKITARU_THRUSTER_PACK = LocationData(
    61, "Pokitaru", "Pokitaru: Bob's Shop", Items.THRUSTER_PACK.name, {RAC1POOL.PACKS})
POKITARU_GOLD_BOLT = LocationData(
    62, "Pokitaru", "Pokitaru: Gold Bolt: Waterfalls", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, pokitaru_gold_bolt_rule)
POKITARU_ALIEN_INVASION = LocationData(  # Todo: Pokitaru Logic
    123, "Pokitaru", "Pokitaru: Skillpoint: Alien Invasion", Items.ALIEN_INVASION.name, {RAC1POOL.SKILLPOINT})
POKITARU_BURIED_TREASURE = LocationData(
    124, "Pokitaru", "Pokitaru: Skillpoint: Buried Treasure", Items.BURIED_TREASURE.name, {RAC1POOL.SKILLPOINT})

# Hoven
HOVEN_VENDOR_DRONE_DEVICE = LocationData(
    63, "Hoven", "Hoven: Vendor - 7,500", Items.DRONE_DEVICE.name, {RAC1POOL.WEAPONS}, has_7500_bolts)
HOVEN_TURRET_INFOBOT = LocationData(
    64, "Hoven", "Hoven: Destroy the Planet-buster", Items.GEMLIK_INFOBOT.name, {RAC1POOL.INFOBOTS}, hoven_infobot_rule)
HOVEN_HYDRO_PACK = LocationData(
    65, "Hoven", "Hoven: Edwina's Shop", Items.HYDRO_PACK.name, {RAC1POOL.PACKS}, has_hydrodisplacer)
HOVEN_RARITANIUM = LocationData(
    66, "Hoven", "Hoven: Talk to the Miner", Items.RARITANIUM.name, {RAC1POOL.EXTRA_ITEMS}, hoven_raritanium_rule)
HOVEN_WATER_GOLD_BOLT = LocationData(
    67, "Hoven", "Hoven: Gold Bolt: in the Water Cave", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, has_hydrodisplacer)
HOVEN_WALLJUMP_GOLD_BOLT = LocationData(
    68, "Hoven", "Hoven: Gold Bolt: Moving wall jump", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS})
HOVEN_PEST_CONTROL = LocationData(
    125, "Hoven", "Hoven: Skillpoint: Pest Control", Items.PEST_CONTROL.name, {RAC1POOL.SKILLPOINT})  # Todo: Hoven Logic
HOVEN_WHIRLYBIRDS = LocationData(
    126, "Hoven", "Hoven: Skillpoint: Whirlybirds", Items.WHIRLYBIRDS.name, {RAC1POOL.SKILLPOINT})  # Todo: Hoven Logic

# Gemlik
GEMLIK_QUARK_FIGHT = LocationData(
    69, "Gemlik", "Gemlik: Defeat Captain Quark", Items.OLTANIS_INFOBOT.name, {RAC1POOL.INFOBOTS}, gemlik_quark_rule)
GEMLIK_GOLD_BOLT = LocationData(
    70, "Gemlik", "Gemlik: Gold Bolt: Visibomb Hidden Tower", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, gemlik_bolt_rule)
GEMLIK_SITTING_DUCKS = LocationData(  # Todo: Gemlik logic
    127, "Gemlik", "Gemlik: Skillpoint: Sitting Ducks", Items.SITTING_DUCKS.name, {RAC1POOL.SKILLPOINT})

# Oltanis
OLTANIS_VENDOR_TESLA_CLAW = LocationData(
    71, "Oltanis", "Oltanis: Vendor - 40,000", Items.TESLA_CLAW.name, {RAC1POOL.WEAPONS}, has_40k_bolts)
OLTANIS_INFOBOT = LocationData(
    72, "Oltanis", "Oltanis: Grindrail path: Scrap Merchant", Items.QUARTU_INFOBOT.name, {RAC1POOL.INFOBOTS}, has_grindboots)
OLTANIS_PDA = LocationData(
    73, "Oltanis", "Oltanis: Magneboot path: Buy the PDA from Steve", Items.PDA.name, {RAC1POOL.GADGETS}, has_magneboots)
OLTANIS_MORPH_O_RAY = LocationData(
    74, "Oltanis", "Oltanis: Swingshot path: Search the city", Items.MORPH_O_RAY.name, {RAC1POOL.WEAPONS}, has_swingshot)
OLTANIS_MAIN_GOLD_BOLT = LocationData(
    75, "Oltanis", "Oltanis: Gold Bolt: Grindrail path: Swingshot Upper Ledge", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    oltanis_main_bolt_rule)
OLTANIS_MAGNET_GOLD_BOLT_1 = LocationData(
    76, "Oltanis", "Oltanis: Gold Bolt: Magneboot path: Ledge near Bomber", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    has_magneboots)
OLTANIS_MAGNET_GOLD_BOLT_2 = LocationData(
    77, "Oltanis", "Oltanis: Gold Bolt: Magneboot path: Ledge hang", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    has_magneboots)
OLTANIS_FINAL_GOLD_BOLT = LocationData(
    78, "Oltanis", "Oltanis: Gold Bolt: All Objectives", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    oltanis_final_bolt_rule)
OLTANIS_SHATTERED_GLASS = LocationData(  # Todo: Oltanis Logic
    128, "Oltanis", "Oltanis: Skillpoint: Shattered Glass", Items.SHATTERED_GLASS.name, {RAC1POOL.SKILLPOINT})
OLTANIS_BLAST_EM = LocationData(
    129, "Oltanis", "Oltanis: Skillpoint: Blast Em", Items.BLAST_EM.name, {RAC1POOL.SKILLPOINT})  # Todo: Oltanis Logic

# Quartu
QUARTU_GIANT_CLANK_INFOBOT = LocationData(
    79, "Quartu", "Quartu: Giant Clank Fight", Items.KALEBO_INFOBOT.name, {RAC1POOL.INFOBOTS}, has_swingshot)
QUARTU_BOLT_GRABBER = LocationData(
    80, "Quartu", "Quartu: Water Path", Items.BOLT_GRABBER.name, {RAC1POOL.EXTRA_ITEMS}, quartu_bolt_grabber_rule)
QUARTU_INFILTRATE_INFOBOT = LocationData(
    81, "Quartu", "Quartu: Clank's mother", Items.FLEET_INFOBOT.name, {RAC1POOL.INFOBOTS}, quartu_infiltrate_rule)
QUARTU_MOM_GOLD_BOLT = LocationData(
    82, "Quartu", "Quartu: Gold Bolt: Behind Clank's mother", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    quartu_infiltrate_rule)
QUARTU_CODEBOT_GOLD_BOLT = LocationData(
    83, "Quartu", "Quartu: Gold Bolt: Codebot door", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, quartu_codebot_rule)

# Kalebo III
KALEBO_HOLOGUISE = LocationData(
    84, "Kalebo III", "Kalebo III: Win the hoverboard race", Items.HOLOGUISE.name, {RAC1POOL.GADGETS}, kalebo_hologuise_rule)
KALEBO_MAP_O_MATIC = LocationData(
    85, "Kalebo III", "Kalebo III: Grindrail: Helpdesk", Items.MAP_O_MATIC.name, {RAC1POOL.EXTRA_ITEMS}, has_grindboots)
KALEBO_GRIND_GOLD_BOLT = LocationData(
    86, "Kalebo III", "Kalebo III: Gold Bolt: On the Grindrail", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, has_grindboots)
KALEBO_BREAK_ROOM_GOLD_BOLT = LocationData(
    87, "Kalebo III", "Kalebo III: Gold Bolt: Employee break room", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    has_grindboots)
KALEBO_HEAVY_TRAFFIC = LocationData(
    130, "Kalebo III", "Kalebo III: Skillpoint: Heavy Traffic", Items.HEAVY_TRAFFIC.name, {RAC1POOL.SKILLPOINT},
    has_grindboots)
KALEBO_MAGICIAN = LocationData(
    131, "Kalebo III", "Kalebo III: Skillpoint: Magician", Items.MAGICIAN.name, {RAC1POOL.SKILLPOINT})  # Todo: Kalebo Logic

# Drek's Fleet
FLEET_INFOBOT = LocationData(
    88, "Drek's Fleet", "Drek's Fleet: Flagship", Items.VELDIN_INFOBOT.name, {RAC1POOL.INFOBOTS}, fleet_infobot_rule)
FLEET_CODEBOT = LocationData(
    89, "Drek's Fleet", "Drek's Fleet: Water section", Items.CODEBOT.name, {RAC1POOL.EXTRA_ITEMS}, fleet_water_rule)
FLEET_WATER_GOLD_BOLT = LocationData(
    90, "Drek's Fleet", "Drek's Fleet: Gold Bolt: Water section", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    fleet_water_rule)
FLEET_ROBOT_GOLD_BOLT = (LocationData(
    91, "Drek's Fleet", "Drek's Fleet: Gold Bolt: Sidepath with robot guards", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    fleet_second_bolt_rule))
FLEET_SNEAKY = LocationData(
    132, "Fleet", "Fleet: Skillpoint: Sneaky", Items.SNEAKY.name, {RAC1POOL.SKILLPOINT})  # Todo: Fleet Logic
FLEET_CAREFUL_CRUISE = LocationData(  # Todo: Fleet Logic
    133, "Fleet", "Fleet: Skillpoint: Careful Cruise", Items.CAREFUL_CRUISE.name, {RAC1POOL.SKILLPOINT})

# Veldin
VELDIN_TAUNTER_GOLD_BOLT = LocationData(
    92, "Veldin", "Veldin: Gold Bolt: Taunter the horny toad", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    veldin_taunter_bolt_rule)
VELDIN_HALFWAY_GOLD_BOLT = LocationData(
    93, "Veldin", "Veldin: Gold Bolt: Platforms", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, veldin_halfway_bolt_rule)
VELDIN_GRIND_GOLD_BOLT = LocationData(
    94, "Veldin", "Veldin: Gold Bolt: Grindrail", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, veldin_grind_bolt_rule)
VELDIN_GOING_COMMANDO = LocationData(
    134, "Veldin", "Veldin: Skillpoint: Going Commando", Items.GOING_COMMANDO.name, {RAC1POOL.SKILLPOINT},
    veldin_global_rule)
VELDIN_DREK = LocationData(None, "Veldin", "Veldin: Defeat Chairman Drek", None, access_rule=veldin_defeat_drek_rule)
