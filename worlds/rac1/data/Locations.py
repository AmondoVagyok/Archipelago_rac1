from dataclasses import dataclass
from typing import Callable, Optional

from worlds.rac1.constants.locations.general import RAC1LOCATION
from worlds.rac1.constants.locations.goldbolts import RAC1BOLT
from worlds.rac1.constants.locations.planets import RAC1PLANET
from worlds.rac1.constants.locations.skillpoints import RAC1SKILLPOINT
from worlds.rac1.constants.locations.vendors import RAC1VENDOR
from worlds.rac1.constants.pools import RAC1POOL

from worlds.rac1.Logic import *

DEFAULT_LIST = list(
    [RAC1POOL.WEAPONS, RAC1POOL.GADGETS, RAC1POOL.PACKS, RAC1POOL.HELMETS, RAC1POOL.BOOTS, RAC1POOL.EXTRA_ITEMS,
     RAC1POOL.GOLD_BOLTS, RAC1POOL.INFOBOTS])
ALL_POOLS = list(
    [RAC1POOL.START_PLANET, RAC1POOL.START_ITEM, RAC1POOL.WEAPONS, RAC1POOL.GOLD_WEAPONS, RAC1POOL.GADGETS,
     RAC1POOL.PACKS, RAC1POOL.HELMETS,
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
    112, RAC1PLANET.GENERAL, RAC1SKILLPOINT.GENERAL_TRICKY, Items.TRICKY.name, {RAC1POOL.SKILLPOINT})

# Novalis
NOVALIS_PLUMBER = LocationData(
    1, RAC1PLANET.NOVALIS, RAC1LOCATION.NOVALIS_PLUMBER, Items.ARIDIA_INFOBOT.name, {RAC1POOL.INFOBOTS})
NOVALIS_MAYOR = LocationData(
    2, RAC1PLANET.NOVALIS, RAC1LOCATION.NOVALIS_CHAIRMAN, Items.KERWAN_INFOBOT.name, {RAC1POOL.INFOBOTS})
NOVALIS_VENDOR_PYROCITOR = LocationData(
    3, RAC1PLANET.NOVALIS, RAC1VENDOR.NOVALIS_PYROCITOR, Items.PYROCITOR.name, {RAC1POOL.WEAPONS})
NOVALIS_SEWER_GOLD_BOLT = LocationData(
    4, RAC1PLANET.NOVALIS, RAC1BOLT.NOVALIS_WATERWORKS, Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS})
NOVALIS_CAVES_GOLD_BOLT = LocationData(
    5, RAC1PLANET.NOVALIS, RAC1BOLT.NOVALIS_CAVES, Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, novalis_cave_gb_rule)
NOVALIS_UNDERWATER_CAVES_GOLD_BOLT = LocationData(
    6, RAC1PLANET.NOVALIS, RAC1BOLT.NOVALIS_AMOEBOID, Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    novalis_underwater_caves_rule)
# Golden Weapon Locations
NOVALIS_GOLD_WEAPON_1 = LocationData(
    100, RAC1PLANET.NOVALIS, RAC1VENDOR.NOVALIS_GOLD1, Items.GOLD_TESLA_CLAW.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_60k)
NOVALIS_GOLD_WEAPON_2 = LocationData(
    95, RAC1PLANET.NOVALIS, RAC1VENDOR.NOVALIS_GOLD2, Items.GOLD_BOMB_GLOVE.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_20k)
NOVALIS_GOLD_WEAPON_3 = LocationData(
    101, RAC1PLANET.NOVALIS, RAC1VENDOR.NOVALIS_GOLD3, Items.GOLD_DEVASTATOR.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_60k)
NOVALIS_GOLD_WEAPON_4 = LocationData(
    96, RAC1PLANET.NOVALIS, RAC1VENDOR.NOVALIS_GOLD4, Items.GOLD_PYROCITOR.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_30k)
NOVALIS_GOLD_WEAPON_5 = LocationData(
    102, RAC1PLANET.NOVALIS, RAC1VENDOR.NOVALIS_GOLD5, Items.GOLD_MINE_GLOVE.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_10k)
NOVALIS_GOLD_WEAPON_6 = LocationData(
    97, RAC1PLANET.NOVALIS, RAC1VENDOR.NOVALIS_GOLD6, Items.GOLD_BLASTER.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_20k)
NOVALIS_GOLD_WEAPON_7 = LocationData(
    103, RAC1PLANET.NOVALIS, RAC1VENDOR.NOVALIS_GOLD7, Items.GOLD_MORPH_O_RAY.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_20k)
NOVALIS_GOLD_WEAPON_8 = LocationData(
    98, RAC1PLANET.NOVALIS, RAC1VENDOR.NOVALIS_GOLD8, Items.GOLD_GLOVE_OF_DOOM.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_10k)
NOVALIS_GOLD_WEAPON_9 = LocationData(
    104, RAC1PLANET.NOVALIS, RAC1VENDOR.NOVALIS_GOLD9, Items.GOLD_DECOY_GLOVE.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_10k)
NOVALIS_GOLD_WEAPON_10 = LocationData(
    99, RAC1PLANET.NOVALIS, RAC1VENDOR.NOVALIS_GOLD10, Items.GOLD_SUCK_CANNON.name, {RAC1POOL.GOLD_WEAPONS},
    novalis_gold_weapon_10k)
NOVALIS_SKILLPOINT = LocationData(
    105, RAC1PLANET.NOVALIS, RAC1SKILLPOINT.NOVALIS_TAKE_AIM, Items.TAKE_AIM.name, {RAC1POOL.SKILLPOINT},
    has_medium_range_weapon)

# Aridia
ARIDIA_HOVERBOARD = LocationData(
    7, RAC1PLANET.ARIDIA, RAC1LOCATION.ARIDIA_HOVERBOARD, Items.HOVERBOARD.name, {RAC1POOL.EXTRA_ITEMS})
ARIDIA_TRESPASSER = LocationData(
    8, RAC1PLANET.ARIDIA, RAC1LOCATION.ARIDIA_TRESPASSER, Items.TRESPASSER.name, {RAC1POOL.GADGETS},
    aridia_trespasser_rule)
ARIDIA_SONIC_SUMMONER = LocationData(
    9, RAC1PLANET.ARIDIA, RAC1LOCATION.ARIDIA_SONIC_SUMMONER, Items.SONIC_SUMMONER.name, {RAC1POOL.HELMETS},
    has_zoomerator)
ARIDIA_TRESPASSER_GOLD_BOLT = LocationData(
    10, RAC1PLANET.ARIDIA, RAC1BOLT.ARIDIA_TRESPASSER, Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    aridia_trespasser_rule)
ARIDIA_ISLAND_GOLD_BOLT = LocationData(
    11, RAC1PLANET.ARIDIA, RAC1BOLT.ARIDIA_ISLAND, Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS})
ARIDIA_MAGNEBOOTS_GOLD_BOLT = LocationData(
    12, RAC1PLANET.ARIDIA, RAC1BOLT.ARIDIA_MAGNEBOOTS, Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, aridia_laser_rule)
ARIDIA_SANDSHARK_GOLD_BOLT = LocationData(
    13, RAC1PLANET.ARIDIA, RAC1BOLT.ARIDIA_SANDSHARK, Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, aridia_cave_rule)
ARIDIA_SWING_IT = LocationData(
    106, RAC1PLANET.ARIDIA, RAC1SKILLPOINT.ARIDIA_SWING_IT, Items.SWING_IT.name, {RAC1POOL.SKILLPOINT}, has_swingshot)
ARIDIA_TRANSPORTED = LocationData(
    107, RAC1PLANET.ARIDIA, RAC1SKILLPOINT.ARIDIA_TRANSPORTED, Items.TRANSPORTED.name, {RAC1POOL.SKILLPOINT},
    has_medium_range_weapon)

# Kerwan
KERWAN_SWINGSHOT = LocationData(
    14, RAC1PLANET.KERWAN, RAC1LOCATION.KERWAN_SWINGSHOT, Items.SWINGSHOT.name, {RAC1POOL.GADGETS})
KERWAN_HELIPACK = LocationData(
    15, RAC1PLANET.KERWAN, RAC1LOCATION.KERWAN_HELIPACK, Items.HELI_PACK.name, {RAC1POOL.PACKS})
KERWAN_TRAIN_INFOBOT = LocationData(
    16, RAC1PLANET.KERWAN, RAC1LOCATION.KERWAN_TRAIN_INFOBOT, Items.EUDORA_INFOBOT.name, {RAC1POOL.INFOBOTS},
    kerwan_train_rule)
KERWAN_VENDOR_BLASTER = LocationData(
    17, RAC1PLANET.KERWAN, RAC1VENDOR.KERWAN_BLASTER, Items.BLASTER.name, {RAC1POOL.WEAPONS})
KERWAN_BELOW_SHIP_GOLD_BOLT = LocationData(
    18, RAC1PLANET.KERWAN, RAC1BOLT.KERWAN_BELOW_SHIP, Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS})
KERWAN_TRAIN_STATION_GOLD_BOLT = LocationData(
    19, RAC1PLANET.KERWAN, RAC1BOLT.KERWAN_TRAIN_STATION, Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    kerwan_train_rule)
KERWAN_LONE_TOWER_GOLD_BOLT = LocationData(
    20, RAC1PLANET.KERWAN, RAC1BOLT.KERWAN_LONE_TOWER, Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    kerwan_course_gb_rule)
KERWAN_STRIKE_A_POSE = LocationData(
    108, RAC1PLANET.KERWAN, RAC1SKILLPOINT.KERWAN_STRIKE_A_POSE, Items.STRIKE_A_POSE.name, {RAC1POOL.SKILLPOINT},
    can_glide)
KERWAN_BLIMPY = LocationData(
    109, RAC1PLANET.KERWAN, RAC1SKILLPOINT.KERWAN_BLIMPY, Items.BLIMPY.name, {RAC1POOL.SKILLPOINT},
    has_long_range_weapon)
KERWAN_QWARKTASTIC = LocationData(
    110, RAC1PLANET.KERWAN, RAC1SKILLPOINT.KERWAN_QWARKTASTIC, Items.QWARKTASTIC.name, {RAC1POOL.SKILLPOINT},
    has_explosive_weapon)

# Eudora
EUDORA_HENCHMAN = LocationData(
    21, RAC1PLANET.EUDORA, "Eudora: Robot Lieutenant", Items.BLARG_INFOBOT.name, {RAC1POOL.INFOBOTS},
    eudora_henchman_rule)
EUDORA_SUCK_CANNON = LocationData(
    22, RAC1PLANET.EUDORA, "Eudora: Explore the Mills", Items.SUCK_CANNON.name, {RAC1POOL.WEAPONS},
    eudora_suck_cannon_rule)
EUDORA_VENDOR_GLOVE_OF_DOOM = LocationData(
    23, RAC1PLANET.EUDORA, "Eudora: Vendor - 7,500", Items.GLOVE_OF_DOOM.name, {RAC1POOL.WEAPONS}, has_7500_bolts)
EUDORA_GOLD_BOLT = LocationData(
    24, RAC1PLANET.EUDORA, "Eudora: Gold Bolt", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, can_heli_high_jump)
EUDORA_ANY_TEN = LocationData(
    111, RAC1PLANET.EUDORA, RAC1SKILLPOINT.EUDORA_ANY_TEN, Items.ANY_TEN.name, {RAC1POOL.SKILLPOINT},
    eudora_skillpoint_rule)

# Rilgar
RILGAR_QUARK_INFOBOT = LocationData(
    25, RAC1PLANET.RILGAR, "Rilgar: Locate Captain Quark", Items.UMBRIS_INFOBOT.name, {RAC1POOL.INFOBOTS},
    rilgar_bouncer_rule)
RILGAR_PLATINUM_ZOOMERATOR = LocationData(
    26, RAC1PLANET.RILGAR, "Rilgar: Win the hoverboard race", Items.ZOOMERATOR.name, {RAC1POOL.EXTRA_ITEMS},
    rilgar_hoverboard_rule)
RILGAR_MINE_GLOVE = LocationData(
    27, RAC1PLANET.RILGAR, "Rilgar: Vendor - 7,500", Items.MINE_GLOVE.name, {RAC1POOL.WEAPONS}, has_7500_bolts)
RILGAR_RYNO = LocationData(
    28, RAC1PLANET.RILGAR, "Rilgar: Shady Salesman - 150,000", Items.RYNO.name, {RAC1POOL.WEAPONS}, rilgar_ryno_rule)
RILGAR_MAZE_GOLD_BOLT = LocationData(
    29, RAC1PLANET.RILGAR, "Rilgar: Gold Bolt: Maze", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, can_improved_jump)
RILGAR_WATERWORKS_GOLD_BOLT = LocationData(
    30, RAC1PLANET.RILGAR, "Rilgar: Gold Bolt: Sewer Cave", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    rilgar_underwater_bolt_rule)
RILGAR_CLUCK_CLUCK = LocationData(
    113, RAC1PLANET.RILGAR, RAC1SKILLPOINT.RILGAR_CLUCK_CLUCK, Items.CLUCK_CLUCK.name, {RAC1POOL.SKILLPOINT}, has_morph)
RILGAR_SPEEDY = LocationData(
    114, RAC1PLANET.RILGAR, RAC1SKILLPOINT.RILGAR_SPEEDY, Items.SPEEDY.name, {RAC1POOL.SKILLPOINT},
    rilgar_hoverboard_rule)

# Blarg
BLARG_HYDRODISPLACER = LocationData(
    31, RAC1PLANET.BLARG, "Blarg: Outside as Clank", Items.HYDRODISPLACER.name, {RAC1POOL.GADGETS}, has_trespasser)
BLARG_EXPLOSION_INFOBOT = LocationData(
    32, RAC1PLANET.BLARG, "Blarg: Destroy the Warship", Items.RILGAR_INFOBOT.name, {RAC1POOL.INFOBOTS})
BLARG_GRINDBOOTS = LocationData(
    33, RAC1PLANET.BLARG, "Blarg: Explore the Space Station", Items.GRINDBOOTS.name, {RAC1POOL.BOOTS}, has_swingshot)
BLARG_VENDOR_TAUNTER = LocationData(
    34, RAC1PLANET.BLARG, "Blarg: Vendor - 2,500", Items.TAUNTER.name, {RAC1POOL.WEAPONS})
BLARG_OUTSIDE_GOLD_BOLT = LocationData(
    35, RAC1PLANET.BLARG, "Blarg: Gold Bolt: Outside", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    blarg_outside_gold_bolt_rule)
BLARG_SWARMER_GOLD_BOLT = LocationData(
    36, RAC1PLANET.BLARG, "Blarg: Gold Bolt: Cages", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, has_swingshot)
BLARG_GIRL_TROUBLE = LocationData(
    115, RAC1PLANET.BLARG, RAC1SKILLPOINT.BLARG_GIRL_TROUBLE, Items.GIRL_TROUBLE.name, {RAC1POOL.SKILLPOINT},
    has_swingshot)

# Umbris
UMBRIS_SNAGGLEBEAST_INFOBOT = LocationData(
    37, RAC1PLANET.UMBRIS, "Umbris: Defeat the Snagglebeast", Items.BATALIA_INFOBOT.name, {RAC1POOL.INFOBOTS},
    umbris_snagglebeast_rule)
UMBRIS_PRESSURE_PUZZLE_GOLD_BOLT = LocationData(
    38, RAC1PLANET.UMBRIS, "Umbris: Gold Bolt: Lighthouse puzzle", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    umbris_pressure_bolt_rule)
UMBRIS_JUMP_DOWN_GOLD_BOLT = LocationData(
    39, RAC1PLANET.UMBRIS, "Umbris: Gold bolt: Jumping Down", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    umbris_jump_bolt_rule)

# Batalia
BATALIA_VENDOR_DEVASTATOR = LocationData(
    40, RAC1PLANET.BATALIA, "Batalia: Vendor - 10,000", Items.DEVASTATOR.name, {RAC1POOL.WEAPONS}, has_10k_bolts)
BATALIA_GRINDRAIL_INFOBOT = LocationData(
    41, RAC1PLANET.BATALIA, "Batalia: Ride the grindrail", Items.GASPAR_INFOBOT.name, {RAC1POOL.INFOBOTS},
    has_grindboots)
BATALIA_COMMANDER_INFOBOT = LocationData(
    42, RAC1PLANET.BATALIA, "Batalia: Commando", Items.ORXON_INFOBOT.name, {RAC1POOL.INFOBOTS})
BATALIA_METAL_DETECTOR = LocationData(
    43, RAC1PLANET.BATALIA, "Batalia: Shoot down the Bombers", Items.METAL_DETECTOR.name, {RAC1POOL.GADGETS},
    has_magneboots)
BATALIA_CLIFFSIDE_GOLD_BOLT = LocationData(
    44, RAC1PLANET.BATALIA, "Batalia: Gold Bolt: Cliffside", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    can_improved_jump)
BATALIA_TRESPASSER_GOLD_BOLT = LocationData(
    45, RAC1PLANET.BATALIA, "Batalia: Gold Bolt: House Roof", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS})
BATALIA_JUMPER = LocationData(
    116, RAC1PLANET.BATALIA, RAC1SKILLPOINT.BATALIA_JUMPER, Items.JUMPER.name, {RAC1POOL.SKILLPOINT}, has_grindboots)
BATALIA_ACCURACY_COUNTS = LocationData(
    117, RAC1PLANET.BATALIA, RAC1SKILLPOINT.BATALIA_ACCURACY_COUNTS, Items.ACCURACY_COUNTS.name, {RAC1POOL.SKILLPOINT},
    has_magneboots)
BATALIA_EAT_LEAD = LocationData(
    118, RAC1PLANET.BATALIA, RAC1SKILLPOINT.BATALIA_EAT_LEAD, Items.EAT_LEAD.name, {RAC1POOL.SKILLPOINT}, has_sonic)

# Gaspar
GASPAR_VENDOR_WALLOPER = LocationData(
    46, RAC1PLANET.GASPAR, "Gaspar: Vendor - 7,500", Items.WALLOPER.name, {RAC1POOL.WEAPONS}, has_7500_bolts)
GASPAR_PILOT_HELMET = LocationData(
    47, RAC1PLANET.GASPAR, "Gaspar: Get the pilot helmet", Items.PILOTS_HELMET.name, {RAC1POOL.HELMETS})
GASPAR_SWINGSHOT_GOLD_BOLT = (LocationData(
    48, RAC1PLANET.GASPAR, "Gaspar: Gold Bolt: Destroy the Bombers", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    has_swingshot))
GASPAR_VOLCANO_GOLD_BOLT = LocationData(
    49, RAC1PLANET.GASPAR, "Gaspar: Gold Bolt: Volcano", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS}, can_improved_jump)
GASPAR_DESTROYED = LocationData(
    119, RAC1PLANET.GASPAR, RAC1SKILLPOINT.GASPAR_DESTROYED, Items.DESTROYED.name, {RAC1POOL.SKILLPOINT},
    gaspar_skillpoint_rule)
GASPAR_GUNNER = LocationData(
    120, RAC1PLANET.GASPAR, RAC1SKILLPOINT.GASPAR_GUNNER, Items.GUNNER.name, {RAC1POOL.SKILLPOINT})

# Orxon
ORXON_VENDOR_VISIBOMB = LocationData(
    50, RAC1PLANET.ORXON, "Orxon: Vendor - 15,000", Items.VISIBOMB.name, {RAC1POOL.WEAPONS}, orxon_visibomb_rule)
ORXON_CLANK_INFOBOT = LocationData(
    51, RAC1PLANET.ORXON, "Orxon: Clank: Traverse the Wilderness", Items.POKITARU_INFOBOT.name, {RAC1POOL.INFOBOTS})
ORXON_RATCHET_INFOBOT = LocationData(
    52, RAC1PLANET.ORXON, "Orxon: Chase the Infobot", Items.HOVEN_INFOBOT.name, {RAC1POOL.INFOBOTS},
    orxon_ratchet_infobot_rule)
ORXON_CLANK_MAGNEBOOTS = LocationData(
    53, RAC1PLANET.ORXON, "Orxon: Clank: Search the Labs", Items.MAGNEBOOTS.name, {RAC1POOL.BOOTS})
ORXON_PREMIUM_NANOTECH = LocationData(
    54, RAC1PLANET.ORXON, "Orxon: Buy the premium nanotech - 4,000", Items.PREMIUM_NANOTECH.name,
    {RAC1POOL.EXTRA_ITEMS},
    orxon_nanotech_rule)
ORXON_ULTRA_NANOTECH = LocationData(
    55, RAC1PLANET.ORXON, "Orxon: Buy the ultra nanotech - 30,000", Items.ULTRA_NANOTECH.name, {RAC1POOL.EXTRA_ITEMS},
    orxon_ultra_nanotech_rule)
ORXON_CLANK_GOLD_BOLT = LocationData(
    56, RAC1PLANET.ORXON, "Orxon: Gold Bolt: Return to the Clank section", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    has_o2_mask)
ORXON_VISIBOMB_GOLD_BOLT = LocationData(
    57, RAC1PLANET.ORXON, "Orxon: Gold Bolt: Long Tunnel", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    orxon_visibomb_bolt_rule)
ORXON_SNIPER = LocationData(
    121, RAC1PLANET.ORXON, RAC1SKILLPOINT.ORXON_SNIPER, Items.SNIPER.name, {RAC1POOL.SKILLPOINT}, orxon_sniper_rule)
ORXON_HEY_OVER_HERE = LocationData(
    122, RAC1PLANET.ORXON, RAC1SKILLPOINT.ORXON_HEY_OVER_HERE, Items.HEY_OVER_HERE.name, {RAC1POOL.SKILLPOINT},
    orxon_hey_over_here_rule)

# Pokitaru
POKITARU_VENDOR_DECOY_GLOVE = LocationData(
    58, RAC1PLANET.POKITARU, "Pokitaru: Vendor - 7,500", Items.DECOY_GLOVE.name, {RAC1POOL.WEAPONS}, has_7500_bolts)
POKITARU_O2_MASK = LocationData(
    59, RAC1PLANET.POKITARU, "Pokitaru: Pilot the Ship", Items.O2_MASK.name, {RAC1POOL.HELMETS}, pokitaru_ship_rule)
POKITARU_SEWER_PERSUADER = LocationData(
    60, RAC1PLANET.POKITARU, "Pokitaru: Trade Raritanium", Items.PERSUADER.name, {RAC1POOL.EXTRA_ITEMS},
    pokitaru_persuader_rule)
POKITARU_THRUSTER_PACK = LocationData(
    61, RAC1PLANET.POKITARU, "Pokitaru: Bob's Shop", Items.THRUSTER_PACK.name, {RAC1POOL.PACKS})
POKITARU_GOLD_BOLT = LocationData(
    62, RAC1PLANET.POKITARU, "Pokitaru: Gold Bolt: Waterfalls", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    pokitaru_gold_bolt_rule)
POKITARU_ALIEN_INVASION = LocationData(  # Todo: Pokitaru Logic
    123, RAC1PLANET.POKITARU, RAC1SKILLPOINT.POKITARU_ALIEN_INVASION, Items.ALIEN_INVASION.name, {RAC1POOL.SKILLPOINT})
POKITARU_BURIED_TREASURE = LocationData(
    124, RAC1PLANET.POKITARU, RAC1SKILLPOINT.POKITARU_BURIED_TREASURE, Items.BURIED_TREASURE.name,
    {RAC1POOL.SKILLPOINT})

# Hoven
HOVEN_VENDOR_DRONE_DEVICE = LocationData(
    63, RAC1PLANET.HOVEN, "Hoven: Vendor - 7,500", Items.DRONE_DEVICE.name, {RAC1POOL.WEAPONS}, has_7500_bolts)
HOVEN_TURRET_INFOBOT = LocationData(
    64, RAC1PLANET.HOVEN, "Hoven: Destroy the Planet-buster", Items.GEMLIK_INFOBOT.name, {RAC1POOL.INFOBOTS},
    hoven_infobot_rule)
HOVEN_HYDRO_PACK = LocationData(
    65, RAC1PLANET.HOVEN, "Hoven: Edwina's Shop", Items.HYDRO_PACK.name, {RAC1POOL.PACKS}, has_hydrodisplacer)
HOVEN_RARITANIUM = LocationData(
    66, RAC1PLANET.HOVEN, "Hoven: Talk to the Miner", Items.RARITANIUM.name, {RAC1POOL.EXTRA_ITEMS},
    hoven_raritanium_rule)
HOVEN_WATER_GOLD_BOLT = LocationData(
    67, RAC1PLANET.HOVEN, "Hoven: Gold Bolt: in the Water Cave", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    has_hydrodisplacer)
HOVEN_WALLJUMP_GOLD_BOLT = LocationData(
    68, RAC1PLANET.HOVEN, "Hoven: Gold Bolt: Moving wall jump", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS})
HOVEN_PEST_CONTROL = LocationData(
    125, RAC1PLANET.HOVEN, RAC1SKILLPOINT.HOVEN_PEST_CONTROL, Items.PEST_CONTROL.name,
    {RAC1POOL.SKILLPOINT})  # Todo: Hoven Logic
HOVEN_WHIRLYBIRDS = LocationData(
    126, RAC1PLANET.HOVEN, RAC1SKILLPOINT.HOVEN_WHIRLYBIRDS, Items.WHIRLYBIRDS.name,
    {RAC1POOL.SKILLPOINT})  # Todo: Hoven Logic

# Gemlik
GEMLIK_QUARK_FIGHT = LocationData(
    69, RAC1PLANET.GEMLIK, "Gemlik: Defeat Captain Quark", Items.OLTANIS_INFOBOT.name, {RAC1POOL.INFOBOTS},
    gemlik_quark_rule)
GEMLIK_GOLD_BOLT = LocationData(
    70, RAC1PLANET.GEMLIK, "Gemlik: Gold Bolt: Visibomb Hidden Tower", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    gemlik_bolt_rule)
GEMLIK_SITTING_DUCKS = LocationData(  # Todo: Gemlik logic
    127, RAC1PLANET.GEMLIK, RAC1SKILLPOINT.GEMLIK_SITTING_DUCKS, Items.SITTING_DUCKS.name, {RAC1POOL.SKILLPOINT})

# Oltanis
OLTANIS_VENDOR_TESLA_CLAW = LocationData(
    71, RAC1PLANET.OLTANIS, "Oltanis: Vendor - 40,000", Items.TESLA_CLAW.name, {RAC1POOL.WEAPONS}, has_40k_bolts)
OLTANIS_INFOBOT = LocationData(
    72, RAC1PLANET.OLTANIS, "Oltanis: Grindrail path: Scrap Merchant", Items.QUARTU_INFOBOT.name, {RAC1POOL.INFOBOTS},
    has_grindboots)
OLTANIS_PDA = LocationData(
    73, RAC1PLANET.OLTANIS, "Oltanis: Magneboot path: Buy the PDA from Steve", Items.PDA.name, {RAC1POOL.GADGETS},
    has_magneboots)
OLTANIS_MORPH_O_RAY = LocationData(
    74, RAC1PLANET.OLTANIS, "Oltanis: Swingshot path: Search the city", Items.MORPH_O_RAY.name, {RAC1POOL.WEAPONS},
    has_swingshot)
OLTANIS_MAIN_GOLD_BOLT = LocationData(
    75, RAC1PLANET.OLTANIS, "Oltanis: Gold Bolt: Grindrail path: Swingshot Upper Ledge", Items.GOLD_BOLT.name,
    {RAC1POOL.GOLD_BOLTS},
    oltanis_main_bolt_rule)
OLTANIS_MAGNET_GOLD_BOLT_1 = LocationData(
    76, RAC1PLANET.OLTANIS, "Oltanis: Gold Bolt: Magneboot path: Ledge near Bomber", Items.GOLD_BOLT.name,
    {RAC1POOL.GOLD_BOLTS},
    has_magneboots)
OLTANIS_MAGNET_GOLD_BOLT_2 = LocationData(
    77, RAC1PLANET.OLTANIS, "Oltanis: Gold Bolt: Magneboot path: Ledge hang", Items.GOLD_BOLT.name,
    {RAC1POOL.GOLD_BOLTS},
    has_magneboots)
OLTANIS_FINAL_GOLD_BOLT = LocationData(
    78, RAC1PLANET.OLTANIS, "Oltanis: Gold Bolt: All Objectives", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    oltanis_final_bolt_rule)
OLTANIS_SHATTERED_GLASS = LocationData(  # Todo: Oltanis Logic
    128, RAC1PLANET.OLTANIS, RAC1SKILLPOINT.OLTANIS_SHATTERED_GLASS, Items.SHATTERED_GLASS.name, {RAC1POOL.SKILLPOINT})
OLTANIS_BLAST_EM = LocationData(
    129, RAC1PLANET.OLTANIS, RAC1SKILLPOINT.OLTANIS_BLAST_EM, Items.BLAST_EM.name,
    {RAC1POOL.SKILLPOINT})  # Todo: Oltanis Logic

# Quartu
QUARTU_GIANT_CLANK_INFOBOT = LocationData(
    79, RAC1PLANET.QUARTU, "Quartu: Giant Clank Fight", Items.KALEBO_INFOBOT.name, {RAC1POOL.INFOBOTS}, has_swingshot)
QUARTU_BOLT_GRABBER = LocationData(
    80, RAC1PLANET.QUARTU, "Quartu: Water Path", Items.BOLT_GRABBER.name, {RAC1POOL.EXTRA_ITEMS},
    quartu_bolt_grabber_rule)
QUARTU_INFILTRATE_INFOBOT = LocationData(
    81, RAC1PLANET.QUARTU, "Quartu: Clank's mother", Items.FLEET_INFOBOT.name, {RAC1POOL.INFOBOTS},
    quartu_infiltrate_rule)
QUARTU_MOM_GOLD_BOLT = LocationData(
    82, RAC1PLANET.QUARTU, "Quartu: Gold Bolt: Behind Clank's mother", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    quartu_infiltrate_rule)
QUARTU_CODEBOT_GOLD_BOLT = LocationData(
    83, RAC1PLANET.QUARTU, "Quartu: Gold Bolt: Codebot door", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    quartu_codebot_rule)

# Kalebo III
KALEBO_HOLOGUISE = LocationData(
    84, RAC1PLANET.KALEBO_III, "Kalebo III: Win the hoverboard race", Items.HOLOGUISE.name, {RAC1POOL.GADGETS},
    kalebo_hologuise_rule)
KALEBO_MAP_O_MATIC = LocationData(
    85, RAC1PLANET.KALEBO_III, "Kalebo III: Grindrail: Helpdesk", Items.MAP_O_MATIC.name, {RAC1POOL.EXTRA_ITEMS},
    has_grindboots)
KALEBO_GRIND_GOLD_BOLT = LocationData(
    86, RAC1PLANET.KALEBO_III, "Kalebo III: Gold Bolt: On the Grindrail", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    has_grindboots)
KALEBO_BREAK_ROOM_GOLD_BOLT = LocationData(
    87, RAC1PLANET.KALEBO_III, "Kalebo III: Gold Bolt: Employee break room", Items.GOLD_BOLT.name,
    {RAC1POOL.GOLD_BOLTS},
    has_grindboots)
KALEBO_HEAVY_TRAFFIC = LocationData(
    130, RAC1PLANET.KALEBO_III, RAC1SKILLPOINT.KALEBO_HEAVY_TRAFFIC, Items.HEAVY_TRAFFIC.name, {RAC1POOL.SKILLPOINT},
    has_grindboots)
KALEBO_MAGICIAN = LocationData(
    131, RAC1PLANET.KALEBO_III, RAC1SKILLPOINT.KALEBO_MAGICIAN, Items.MAGICIAN.name,
    {RAC1POOL.SKILLPOINT})  # Todo: Kalebo Logic

# Drek's Fleet
FLEET_INFOBOT = LocationData(
    88, RAC1PLANET.FLEET, "Drek's Fleet: Flagship", Items.VELDIN_INFOBOT.name, {RAC1POOL.INFOBOTS}, fleet_infobot_rule)
FLEET_CODEBOT = LocationData(
    89, RAC1PLANET.FLEET, "Drek's Fleet: Water section", Items.CODEBOT.name, {RAC1POOL.EXTRA_ITEMS}, fleet_water_rule)
FLEET_WATER_GOLD_BOLT = LocationData(
    90, RAC1PLANET.FLEET, "Drek's Fleet: Gold Bolt: Water section", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    fleet_water_rule)
FLEET_ROBOT_GOLD_BOLT = (LocationData(
    91, RAC1PLANET.FLEET, "Drek's Fleet: Gold Bolt: Sidepath with robot guards", Items.GOLD_BOLT.name,
    {RAC1POOL.GOLD_BOLTS},
    fleet_second_bolt_rule))
FLEET_SNEAKY = LocationData(
    132, RAC1PLANET.FLEET, RAC1SKILLPOINT.FLEET_SNEAKY, Items.SNEAKY.name, {RAC1POOL.SKILLPOINT})  # Todo: Fleet Logic
FLEET_CAREFUL_CRUISE = LocationData(  # Todo: Fleet Logic
    133, RAC1PLANET.FLEET, RAC1SKILLPOINT.FLEET_CAREFUL_CRUISE, Items.CAREFUL_CRUISE.name, {RAC1POOL.SKILLPOINT})

# Veldin
VELDIN_TAUNTER_GOLD_BOLT = LocationData(
    92, RAC1PLANET.VELDIN, "Veldin: Gold Bolt: Taunter the horny toad", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    veldin_taunter_bolt_rule)
VELDIN_HALFWAY_GOLD_BOLT = LocationData(
    93, RAC1PLANET.VELDIN, "Veldin: Gold Bolt: Platforms", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    veldin_halfway_bolt_rule)
VELDIN_GRIND_GOLD_BOLT = LocationData(
    94, RAC1PLANET.VELDIN, "Veldin: Gold Bolt: Grindrail", Items.GOLD_BOLT.name, {RAC1POOL.GOLD_BOLTS},
    veldin_grind_bolt_rule)
VELDIN_GOING_COMMANDO = LocationData(
    134, RAC1PLANET.VELDIN, RAC1SKILLPOINT.VELDIN_GOING_COMMANDO, Items.GOING_COMMANDO.name, {RAC1POOL.SKILLPOINT},
    veldin_global_rule)
VELDIN_DREK = LocationData(None, RAC1PLANET.VELDIN, "Veldin: Defeat Chairman Drek", None,
                           access_rule=veldin_defeat_drek_rule)
