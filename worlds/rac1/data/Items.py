from dataclasses import dataclass
from typing import Mapping, Sequence

from BaseClasses import Item, ItemClassification
from worlds.rac1 import Options
from worlds.rac1.constants.items import RAC1ITEM
from worlds.rac1.constants.pools import RAC1POOL
from worlds.rac1.constants.progressive_orders import RAC1ORDER


@dataclass
class ItemData(Item):
    item_id: int
    name: str
    pool: str
    classification: ItemClassification
    quantity: int = 1


HELI_PACK = ItemData(2, RAC1ITEM.HELI_PACK, RAC1POOL.PACKS, ItemClassification.progression)
THRUSTER_PACK = ItemData(3, RAC1ITEM.THRUSTER_PACK, RAC1POOL.PACKS, ItemClassification.progression)
HYDRO_PACK = ItemData(4, RAC1ITEM.HYDRO_PACK, RAC1POOL.PACKS, ItemClassification.progression)
SONIC_SUMMONER = ItemData(5, RAC1ITEM.SONIC_SUMMONER, RAC1POOL.HELMETS, ItemClassification.progression)
O2_MASK = ItemData(6, RAC1ITEM.O2_MASK, RAC1POOL.HELMETS, ItemClassification.progression)
PILOTS_HELMET = ItemData(7, RAC1ITEM.PILOTS_HELMET, RAC1POOL.HELMETS, ItemClassification.progression)
# WRENCH = ItemData(8, RAC1ITEM.WRENCH, "?")
SUCK_CANNON = ItemData(9, RAC1ITEM.SUCK_CANNON, RAC1POOL.WEAPONS, ItemClassification.progression)
BOMB_GLOVE = ItemData(10, RAC1ITEM.BOMB_GLOVE, RAC1POOL.WEAPONS, ItemClassification.progression)
DEVASTATOR = ItemData(11, RAC1ITEM.DEVASTATOR, RAC1POOL.WEAPONS, ItemClassification.progression)
SWINGSHOT = ItemData(12, RAC1ITEM.SWINGSHOT, RAC1POOL.GADGETS, ItemClassification.progression)
VISIBOMB = ItemData(13, RAC1ITEM.VISIBOMB_GUN, RAC1POOL.WEAPONS, ItemClassification.progression)
TAUNTER = ItemData(14, RAC1ITEM.TAUNTER, RAC1POOL.WEAPONS, ItemClassification.progression)
BLASTER = ItemData(15, RAC1ITEM.BLASTER, RAC1POOL.WEAPONS, ItemClassification.progression)
PYROCITOR = ItemData(16, RAC1ITEM.PYROCITOR, RAC1POOL.WEAPONS, ItemClassification.progression)
MINE_GLOVE = ItemData(17, RAC1ITEM.MINE_GLOVE, RAC1POOL.WEAPONS, ItemClassification.progression)
WALLOPER = ItemData(18, RAC1ITEM.WALLOPER, RAC1POOL.WEAPONS, ItemClassification.useful)
TESLA_CLAW = ItemData(19, RAC1ITEM.TESLA_CLAW, RAC1POOL.WEAPONS, ItemClassification.progression)
GLOVE_OF_DOOM = ItemData(20, RAC1ITEM.GLOVE_OF_DOOM, RAC1POOL.WEAPONS, ItemClassification.useful)
MORPH_O_RAY = ItemData(21, RAC1ITEM.MORP_O_RAY, RAC1POOL.WEAPONS, ItemClassification.progression)
HYDRODISPLACER = ItemData(22, RAC1ITEM.HYDRODISPLACER, RAC1POOL.GADGETS, ItemClassification.progression)
RYNO = ItemData(23, RAC1ITEM.RYNO, RAC1POOL.WEAPONS, ItemClassification.progression)
DRONE_DEVICE = ItemData(24, RAC1ITEM.DRONE_DEVICE, RAC1POOL.WEAPONS, ItemClassification.useful)
DECOY_GLOVE = ItemData(25, RAC1ITEM.DECOY_GLOVE, RAC1POOL.WEAPONS, ItemClassification.useful)
TRESPASSER = ItemData(26, RAC1ITEM.TRESPASSER, RAC1POOL.GADGETS, ItemClassification.progression)
METAL_DETECTOR = ItemData(27, RAC1ITEM.METAL_DETECTOR, RAC1POOL.GADGETS, ItemClassification.progression)
MAGNEBOOTS = ItemData(28, RAC1ITEM.MAGNEBOOTS, RAC1POOL.BOOTS, ItemClassification.progression)
GRINDBOOTS = ItemData(29, RAC1ITEM.GRINDBOOTS, RAC1POOL.BOOTS, ItemClassification.progression)
HOVERBOARD = ItemData(30, RAC1ITEM.HOVERBOARD, RAC1POOL.EXTRA_ITEMS, ItemClassification.progression)
HOLOGUISE = ItemData(31, RAC1ITEM.HOLOGUISE, RAC1POOL.GADGETS, ItemClassification.progression)
PDA = ItemData(32, RAC1ITEM.PDA, RAC1POOL.GADGETS, ItemClassification.useful)
MAP_O_MATIC = ItemData(33, RAC1ITEM.MAP_O_MATIC, RAC1POOL.EXTRA_ITEMS, ItemClassification.filler)
BOLT_GRABBER = ItemData(34, RAC1ITEM.BOLT_GRABBER, RAC1POOL.EXTRA_ITEMS, ItemClassification.useful)
PERSUADER = ItemData(35, RAC1ITEM.PERSUADER, RAC1POOL.EXTRA_ITEMS, ItemClassification.useful)

ZOOMERATOR = ItemData(48, RAC1ITEM.ZOOMERATOR, RAC1POOL.EXTRA_ITEMS, ItemClassification.progression)
RARITANIUM = ItemData(49, RAC1ITEM.RARITARIUM, RAC1POOL.EXTRA_ITEMS, ItemClassification.progression)
CODEBOT = ItemData(50, RAC1ITEM.CODEBOT, RAC1POOL.EXTRA_ITEMS, ItemClassification.progression)
PREMIUM_NANOTECH = ItemData(52, RAC1ITEM.PREMIUM_NANOTECH, RAC1POOL.EXTRA_ITEMS, ItemClassification.useful)
ULTRA_NANOTECH = ItemData(53, RAC1ITEM.ULTRA_NANOTECH, RAC1POOL.EXTRA_ITEMS, ItemClassification.useful)

GOLD_SUCK_CANNON = ItemData(309, RAC1ITEM.GOLD_SUCK_CANNON, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
GOLD_BOMB_GLOVE = ItemData(310, RAC1ITEM.GOLD_BOMB_GLOVE, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
GOLD_DEVASTATOR = ItemData(311, RAC1ITEM.GOLD_DEVASTATOR, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
GOLD_BLASTER = ItemData(315, RAC1ITEM.GOLD_BLASTER, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
GOLD_PYROCITOR = ItemData(316, RAC1ITEM.GOLD_PYROCITOR, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
GOLD_MINE_GLOVE = ItemData(317, RAC1ITEM.GOLD_MINE_GLOVE, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
GOLD_TESLA_CLAW = ItemData(319, RAC1ITEM.GOLD_TESLA_CLAW, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
GOLD_GLOVE_OF_DOOM = ItemData(320, RAC1ITEM.GOLD_GLOVE_OF_DOOM, RAC1POOL.GOLD_WEAPONS, ItemClassification.useful)
GOLD_MORPH_O_RAY = ItemData(321, RAC1ITEM.GOLD_MORP_O_RAY, RAC1POOL.GOLD_WEAPONS, ItemClassification.progression)
GOLD_DECOY_GLOVE = ItemData(325, RAC1ITEM.GOLD_DECOY_GLOVE, RAC1POOL.GOLD_WEAPONS, ItemClassification.useful)

PROGRESSIVE_PACK = ItemData(80, RAC1ITEM.PROGRESSIVE_PACK, RAC1POOL.PACKS, ItemClassification.progression)
PROGRESSIVE_HELMET = ItemData(81, RAC1ITEM.PROGRESSIVE_HELMET, RAC1POOL.HELMETS, ItemClassification.progression)
PROGRESSIVE_SUCK = ItemData(82, RAC1ITEM.PROGRESSIVE_SUCK, RAC1POOL.WEAPONS, ItemClassification.progression)
PROGRESSIVE_BOMB = ItemData(83, RAC1ITEM.PROGRESSIVE_BOMB, RAC1POOL.WEAPONS, ItemClassification.progression)
PROGRESSIVE_DEVASTATOR = ItemData(84, RAC1ITEM.PROGRESSIVE_DEVASTATOR, RAC1POOL.WEAPONS, ItemClassification.progression)
PROGRESSIVE_BLASTER = ItemData(85, RAC1ITEM.PROGRESSIVE_BLASTER, RAC1POOL.WEAPONS, ItemClassification.progression)
PROGRESSIVE_PYROCITOR = ItemData(86, RAC1ITEM.PROGRESSIVE_PYROCITOR, RAC1POOL.WEAPONS, ItemClassification.progression)
PROGRESSIVE_MINE = ItemData(87, RAC1ITEM.PROGRESSIVE_MINE, RAC1POOL.WEAPONS, ItemClassification.progression)
PROGRESSIVE_TESLA = ItemData(88, RAC1ITEM.PROGRESSIVE_TESLA, RAC1POOL.WEAPONS, ItemClassification.progression)
PROGRESSIVE_DOOM = ItemData(89, RAC1ITEM.PROGRESSIVE_DOOM, RAC1POOL.WEAPONS, ItemClassification.useful)
PROGRESSIVE_MORPH = ItemData(90, RAC1ITEM.PROGRESSIVE_MORPH, RAC1POOL.WEAPONS, ItemClassification.progression)
PROGRESSIVE_DECOY = ItemData(91, RAC1ITEM.PROGRESSIVE_DECOY, RAC1POOL.WEAPONS, ItemClassification.useful)
PROGRESSIVE_BOOT = ItemData(92, RAC1ITEM.PROGRESSIVE_BOOT, RAC1POOL.BOOTS, ItemClassification.progression)
PROGRESSIVE_HOVERBOARD = ItemData(93, RAC1ITEM.PROGRESSIVE_HOVERBOARD, RAC1POOL.EXTRA_ITEMS, ItemClassification.progression)
PROGRESSIVE_TRADE = ItemData(94, RAC1ITEM.PROGRESSIVE_TRADE, RAC1POOL.EXTRA_ITEMS, ItemClassification.progression)
PROGRESSIVE_NANOTECH = ItemData(95, RAC1ITEM.PROGRESSIVE_NANOTECH, RAC1POOL.EXTRA_ITEMS, ItemClassification.useful)

NOVALIS_INFOBOT = ItemData(101, RAC1ITEM.NOVALIS, RAC1POOL.INFOBOTS, ItemClassification.progression)
ARIDIA_INFOBOT = ItemData(102, RAC1ITEM.ARIDIA, RAC1POOL.INFOBOTS, ItemClassification.progression)
KERWAN_INFOBOT = ItemData(103, RAC1ITEM.KERWAN, RAC1POOL.INFOBOTS, ItemClassification.progression)
EUDORA_INFOBOT = ItemData(104, RAC1ITEM.EUDORA, RAC1POOL.INFOBOTS, ItemClassification.progression)
RILGAR_INFOBOT = ItemData(105, RAC1ITEM.RILGAR, RAC1POOL.INFOBOTS, ItemClassification.progression)
BLARG_INFOBOT = ItemData(106, RAC1ITEM.BLARG, RAC1POOL.INFOBOTS, ItemClassification.progression)
UMBRIS_INFOBOT = ItemData(107, RAC1ITEM.UMBRIS, RAC1POOL.INFOBOTS, ItemClassification.progression)
BATALIA_INFOBOT = ItemData(108, RAC1ITEM.BATALIA, RAC1POOL.INFOBOTS, ItemClassification.progression)
GASPAR_INFOBOT = ItemData(109, RAC1ITEM.GASPAR, RAC1POOL.INFOBOTS, ItemClassification.progression)
ORXON_INFOBOT = ItemData(110, RAC1ITEM.ORXON, RAC1POOL.INFOBOTS, ItemClassification.progression)
POKITARU_INFOBOT = ItemData(111, RAC1ITEM.POKITARU, RAC1POOL.INFOBOTS, ItemClassification.progression)
HOVEN_INFOBOT = ItemData(112, RAC1ITEM.HOVEN, RAC1POOL.INFOBOTS, ItemClassification.progression)
GEMLIK_INFOBOT = ItemData(113, RAC1ITEM.GEMLIK_BASE, RAC1POOL.INFOBOTS, ItemClassification.progression)
OLTANIS_INFOBOT = ItemData(114, RAC1ITEM.OLTANIS, RAC1POOL.INFOBOTS, ItemClassification.progression)
QUARTU_INFOBOT = ItemData(115, RAC1ITEM.QUARTU, RAC1POOL.INFOBOTS, ItemClassification.progression)
KALEBO_INFOBOT = ItemData(116, RAC1ITEM.KALEBO_III, RAC1POOL.INFOBOTS, ItemClassification.progression)
FLEET_INFOBOT = ItemData(117, RAC1ITEM.DREKS_FLEET, RAC1POOL.INFOBOTS, ItemClassification.progression)
VELDIN_INFOBOT = ItemData(118, RAC1ITEM.VELDIN, RAC1POOL.INFOBOTS, ItemClassification.progression)

TAKE_AIM = ItemData(200, "Take Aim: Skill Point", "Skillpoint", ItemClassification.filler)
SWING_IT = ItemData(201, "Swing it!: Skill Point", "Skillpoint", ItemClassification.filler)
TRANSPORTED = ItemData(202, "Transported: Skill Point", "Skillpoint", ItemClassification.filler)
STRIKE_A_POSE = ItemData(203, "Strike a pose: Skill Point", "Skillpoint", ItemClassification.filler)
BLIMPY = ItemData(204, "Blimpy: Skill Point", "Skillpoint", ItemClassification.filler)
QWARKTASTIC = ItemData(205, "Qwarktastic: Skill Point", "Skillpoint", ItemClassification.filler)
ANY_TEN = ItemData(206, "Any Ten: Skill Point", "Skillpoint", ItemClassification.filler)
TRICKY = ItemData(207, "Tricky: Skill Point", "Skillpoint", ItemClassification.filler)
CLUCK_CLUCK = ItemData(208, "Cluck, Cluck: Skill Point", "Skillpoint", ItemClassification.filler)
SPEEDY = ItemData(209, "Speedy: Skill Point", "Skillpoint", ItemClassification.filler)
GIRL_TROUBLE = ItemData(210, "Girl Trouble: Skill Point", "Skillpoint", ItemClassification.filler)
JUMPER = ItemData(211, "Jumper: Skill Point", "Skillpoint", ItemClassification.filler)
ACCURACY_COUNTS = ItemData(212, "Accuracy Counts: Skill Point", "Skillpoint", ItemClassification.filler)
EAT_LEAD = ItemData(213, "Eat Lead: Skill Point", "Skillpoint", ItemClassification.filler)
DESTROYED = ItemData(214, "Destroyed: Skill Point", "Skillpoint", ItemClassification.filler)
GUNNER = ItemData(215, "Gunner: Skill Point", "Skillpoint", ItemClassification.filler)
SNIPER = ItemData(216, "Sniper: Skill Point", "Skillpoint", ItemClassification.filler)
HEY_OVER_HERE = ItemData(217, "Hey, Over Here!: Skill Point", "Skillpoint", ItemClassification.filler)
ALIEN_INVASION = ItemData(218, "Alien Invasion: Skill Point", "Skillpoint", ItemClassification.filler)
BURIED_TREASURE = ItemData(219, "Buried Treasure: Skill Point", "Skillpoint", ItemClassification.filler)
PEST_CONTROL = ItemData(220, "Pest Control: Skill Point", "Skillpoint", ItemClassification.filler)
WHIRLYBIRDS = ItemData(221, "Whirlybirds: Skill Point", "Skillpoint", ItemClassification.filler)
SITTING_DUCKS = ItemData(222, "Sitting Ducks: Skill Point", "Skillpoint", ItemClassification.filler)
SHATTERED_GLASS = ItemData(223, "Shattered Glass: Skill Point", "Skillpoint", ItemClassification.filler)
BLAST_EM = ItemData(224, "Blast Em!: Skill Point", "Skillpoint", ItemClassification.filler)
HEAVY_TRAFFIC = ItemData(225, "Heavy Traffic: Skill Point", "Skillpoint", ItemClassification.filler)
MAGICIAN = ItemData(226, "Magician: Skill Point", "Skillpoint", ItemClassification.filler)
SNEAKY = ItemData(227, "Sneaky: Skill Point", "Skillpoint", ItemClassification.filler)
CAREFUL_CRUISE = ItemData(228, "Careful Cruise: Skill Point", "Skillpoint", ItemClassification.filler)
GOING_COMMANDO = ItemData(229, "Going Commando: Skill Point", "Skillpoint", ItemClassification.filler)


@dataclass
class CollectableData(ItemData):
    max_capacity: int = 0x7F


# Collectables
GOLD_BOLT = ItemData(261, RAC1ITEM.GOLD_BOLT,RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing)
GOLD_BOLT_1 = ItemData(262, RAC1ITEM.GOLD_BOLT_1, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 1)
GOLD_BOLT_2 = ItemData(263, RAC1ITEM.GOLD_BOLT_2, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 2)
GOLD_BOLT_3 = ItemData(264, RAC1ITEM.GOLD_BOLT_3, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 3)
GOLD_BOLT_4 = ItemData(265, RAC1ITEM.GOLD_BOLT_4, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 4)
GOLD_BOLT_5 = ItemData(266, RAC1ITEM.GOLD_BOLT_5, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 5)
GOLD_BOLT_6 = ItemData(267, RAC1ITEM.GOLD_BOLT_6, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 6)
GOLD_BOLT_7 = ItemData(268, RAC1ITEM.GOLD_BOLT_7, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 7)
GOLD_BOLT_8 = ItemData(269, RAC1ITEM.GOLD_BOLT_8, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 8)
GOLD_BOLT_9 = ItemData(270, RAC1ITEM.GOLD_BOLT_9, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 9)
GOLD_BOLT_10 = ItemData(271, RAC1ITEM.GOLD_BOLT_10, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 10)
GOLD_BOLT_11 = ItemData(272, RAC1ITEM.GOLD_BOLT_11, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 11)
GOLD_BOLT_12 = ItemData(273, RAC1ITEM.GOLD_BOLT_12, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 12)
GOLD_BOLT_13 = ItemData(274, RAC1ITEM.GOLD_BOLT_13, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 13)
GOLD_BOLT_14 = ItemData(275, RAC1ITEM.GOLD_BOLT_14, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 14)
GOLD_BOLT_15 = ItemData(276, RAC1ITEM.GOLD_BOLT_15, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 15)
GOLD_BOLT_16 = ItemData(277, RAC1ITEM.GOLD_BOLT_16, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 16)
GOLD_BOLT_17 = ItemData(278, RAC1ITEM.GOLD_BOLT_17, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 17)
GOLD_BOLT_18 = ItemData(279, RAC1ITEM.GOLD_BOLT_18, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 18)
GOLD_BOLT_19 = ItemData(280, RAC1ITEM.GOLD_BOLT_19, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 19)
GOLD_BOLT_20 = ItemData(281, RAC1ITEM.GOLD_BOLT_20, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 20)
GOLD_BOLT_21 = ItemData(282, RAC1ITEM.GOLD_BOLT_21, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 21)
GOLD_BOLT_22 = ItemData(283, RAC1ITEM.GOLD_BOLT_22, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 22)
GOLD_BOLT_23 = ItemData(284, RAC1ITEM.GOLD_BOLT_23, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 23)
GOLD_BOLT_24 = ItemData(285, RAC1ITEM.GOLD_BOLT_24, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 24)
GOLD_BOLT_25 = ItemData(286, RAC1ITEM.GOLD_BOLT_25, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 25)
GOLD_BOLT_26 = ItemData(287, RAC1ITEM.GOLD_BOLT_26, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 26)
GOLD_BOLT_27 = ItemData(288, RAC1ITEM.GOLD_BOLT_27, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 27)
GOLD_BOLT_28 = ItemData(289, RAC1ITEM.GOLD_BOLT_28, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 28)
GOLD_BOLT_29 = ItemData(290, RAC1ITEM.GOLD_BOLT_29, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 29)
GOLD_BOLT_30 = ItemData(291, RAC1ITEM.GOLD_BOLT_30, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 30)
GOLD_BOLT_31 = ItemData(292, RAC1ITEM.GOLD_BOLT_31, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 31)
GOLD_BOLT_32 = ItemData(293, RAC1ITEM.GOLD_BOLT_32, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 32)
GOLD_BOLT_33 = ItemData(294, RAC1ITEM.GOLD_BOLT_33, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 33)
GOLD_BOLT_34 = ItemData(295, RAC1ITEM.GOLD_BOLT_34, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 34)
GOLD_BOLT_35 = ItemData(296, RAC1ITEM.GOLD_BOLT_35, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 35)
GOLD_BOLT_36 = ItemData(297, RAC1ITEM.GOLD_BOLT_36, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 36)
GOLD_BOLT_37 = ItemData(298, RAC1ITEM.GOLD_BOLT_37, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 37)
GOLD_BOLT_38 = ItemData(299, RAC1ITEM.GOLD_BOLT_38, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 38)
GOLD_BOLT_39 = ItemData(300, RAC1ITEM.GOLD_BOLT_39, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 39)
GOLD_BOLT_40 = ItemData(301, RAC1ITEM.GOLD_BOLT_40, RAC1POOL.GOLD_BOLTS, ItemClassification.progression_deprioritized_skip_balancing, 40)

BOLT_PACK = ItemData(302, RAC1ITEM.BOLT_PACK_GENERIC, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing)
BOLT_PACK_0 = ItemData(400, RAC1ITEM.BOLT_PACK_0, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 0)
BOLT_PACK_1 = ItemData(401, RAC1ITEM.BOLT_PACK_1, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 1)
BOLT_PACK_2 = ItemData(402, RAC1ITEM.BOLT_PACK_10, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 10)
BOLT_PACK_3 = ItemData(403, RAC1ITEM.BOLT_PACK_100, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 100)
BOLT_PACK_4 = ItemData(404, RAC1ITEM.BOLT_PACK_250, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 250)
BOLT_PACK_5 = ItemData(405, RAC1ITEM.BOLT_PACK_500, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 500)
BOLT_PACK_6 = ItemData(406, RAC1ITEM.BOLT_PACK_750, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 750)
BOLT_PACK_7 = ItemData(407, RAC1ITEM.BOLT_PACK_1000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 1000)
BOLT_PACK_8 = ItemData(408, RAC1ITEM.BOLT_PACK_2000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 2000)
BOLT_PACK_9 = ItemData(409, RAC1ITEM.BOLT_PACK_3000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 3000)
BOLT_PACK_10 = ItemData(410, RAC1ITEM.BOLT_PACK_4000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 4000)
BOLT_PACK_11 = ItemData(411, RAC1ITEM.BOLT_PACK_5000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 5000)
BOLT_PACK_12 = ItemData(412, RAC1ITEM.BOLT_PACK_6000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 6000)
BOLT_PACK_13 = ItemData(413, RAC1ITEM.BOLT_PACK_7000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 7000)
BOLT_PACK_14 = ItemData(414, RAC1ITEM.BOLT_PACK_8000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 8000)
BOLT_PACK_15 = ItemData(415, RAC1ITEM.BOLT_PACK_9000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing, 9000)
BOLT_PACK_16 = ItemData(416, RAC1ITEM.BOLT_PACK_10000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing,
                        10000)
BOLT_PACK_17 = ItemData(417, RAC1ITEM.BOLT_PACK_12500, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing,
                        12500)
BOLT_PACK_18 = ItemData(418, RAC1ITEM.BOLT_PACK_15000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing,
                        15000)
BOLT_PACK_19 = ItemData(419, RAC1ITEM.BOLT_PACK_17500, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing,
                        17500)
BOLT_PACK_20 = ItemData(420, RAC1ITEM.BOLT_PACK_20000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing,
                        20000)
BOLT_PACK_21 = ItemData(421, RAC1ITEM.BOLT_PACK_25000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing,
                        25000)
BOLT_PACK_22 = ItemData(422, RAC1ITEM.BOLT_PACK_30000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing,
                        30000)
BOLT_PACK_23 = ItemData(423, RAC1ITEM.BOLT_PACK_40000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing,
                        40000)
BOLT_PACK_24 = ItemData(424, RAC1ITEM.BOLT_PACK_50000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing,
                        50000)
BOLT_PACK_25 = ItemData(425, RAC1ITEM.BOLT_PACK_75000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing,
                        75000)
BOLT_PACK_26 = ItemData(426, RAC1ITEM.BOLT_PACK_100000, RAC1POOL.FILLER, ItemClassification.progression_deprioritized_skip_balancing,
                        100000)

WEAPONS: Sequence[ItemData] = [
    TAUNTER,
    VISIBOMB,
    WALLOPER,
    RYNO,
    DRONE_DEVICE,
]

NON_PROGRESSIVE_WEAPONS: Sequence[ItemData] = [
    SUCK_CANNON,
    BOMB_GLOVE,
    DEVASTATOR,
    BLASTER,
    PYROCITOR,
    MINE_GLOVE,
    TESLA_CLAW,
    GLOVE_OF_DOOM,
    MORPH_O_RAY,
    DECOY_GLOVE,
]

PROGRESSIVE_WEAPONS: Sequence[ItemData] = [
    PROGRESSIVE_SUCK,
    PROGRESSIVE_BOMB,
    PROGRESSIVE_DEVASTATOR,
    PROGRESSIVE_BLASTER,
    PROGRESSIVE_PYROCITOR,
    PROGRESSIVE_MINE,
    PROGRESSIVE_TESLA,
    PROGRESSIVE_DOOM,
    PROGRESSIVE_MORPH,
    PROGRESSIVE_DECOY,
]

GOLD_WEAPONS: Sequence[ItemData] = [
    GOLD_SUCK_CANNON,
    GOLD_BOMB_GLOVE,
    GOLD_DEVASTATOR,
    GOLD_BLASTER,
    GOLD_PYROCITOR,
    GOLD_MINE_GLOVE,
    GOLD_TESLA_CLAW,
    GOLD_GLOVE_OF_DOOM,
    GOLD_MORPH_O_RAY,
    GOLD_DECOY_GLOVE,
]

PROGRESSIVE_GOLD_WEAPONS: Sequence[ItemData] = [
    GOLD_SUCK_CANNON,
    GOLD_BOMB_GLOVE,
    GOLD_DEVASTATOR,
    GOLD_BLASTER,
    GOLD_PYROCITOR,
    GOLD_MINE_GLOVE,
    GOLD_TESLA_CLAW,
    GOLD_GLOVE_OF_DOOM,
    GOLD_MORPH_O_RAY,
    GOLD_DECOY_GLOVE,
]

GADGETS: Sequence[ItemData] = [
    HYDRODISPLACER,
    TRESPASSER,
    METAL_DETECTOR,
    HOLOGUISE,
    PDA,
    SWINGSHOT,
]

PACKS: Sequence[ItemData] = [
    HELI_PACK,
    THRUSTER_PACK,
    HYDRO_PACK,
]

PROGRESSIVE_PACKS: Sequence[ItemData] = [
    *[PROGRESSIVE_PACK] * 3,
]

HELMETS: Sequence[ItemData] = [
    SONIC_SUMMONER,
    O2_MASK,
    PILOTS_HELMET,
]

PROGRESSIVE_HELMETS: Sequence[ItemData] = [
    *[PROGRESSIVE_HELMET] * 3,
]

BOOTS: Sequence[ItemData] = [
    MAGNEBOOTS,
    GRINDBOOTS,
]

PROGRESSIVE_BOOTS: Sequence[ItemData] = [
    *[PROGRESSIVE_BOOT] * 2,
]

EXTRA_ITEMS: Sequence[ItemData] = [
    MAP_O_MATIC,
    BOLT_GRABBER,
    CODEBOT,
]

NON_PROGRESSIVE_HOVERBOARDS: Sequence[ItemData] = [
    HOVERBOARD,
    ZOOMERATOR,
]

PROGRESSIVE_HOVERBOARDS: Sequence[ItemData] = [
    *[PROGRESSIVE_HOVERBOARD] * 2,
]

NON_PROGRESSIVE_TRADES: Sequence[ItemData] = [
    PERSUADER,
    RARITANIUM,
]

PROGRESSIVE_TRADES: Sequence[ItemData] = [
    *[PROGRESSIVE_TRADE] * 2,
]

NON_PROGRESSIVE_NANOTECHS: Sequence[ItemData] = [
    PREMIUM_NANOTECH,
    ULTRA_NANOTECH,
]

PROGRESSIVE_NANOTECHS: Sequence[ItemData] = [
    *[PROGRESSIVE_NANOTECH] * 2,
]

GOLD_BOLTS: Sequence[ItemData] = [
    GOLD_BOLT,
    GOLD_BOLT_1,
    GOLD_BOLT_2,
    GOLD_BOLT_3,
    GOLD_BOLT_4,
    GOLD_BOLT_5,
    GOLD_BOLT_6,
    GOLD_BOLT_7,
    GOLD_BOLT_8,
    GOLD_BOLT_9,
    GOLD_BOLT_10,
    GOLD_BOLT_11,
    GOLD_BOLT_12,
    GOLD_BOLT_13,
    GOLD_BOLT_14,
    GOLD_BOLT_15,
    GOLD_BOLT_16,
    GOLD_BOLT_17,
    GOLD_BOLT_18,
    GOLD_BOLT_19,
    GOLD_BOLT_20,
    GOLD_BOLT_21,
    GOLD_BOLT_22,
    GOLD_BOLT_23,
    GOLD_BOLT_24,
    GOLD_BOLT_25,
    GOLD_BOLT_26,
    GOLD_BOLT_27,
    GOLD_BOLT_28,
    GOLD_BOLT_29,
    GOLD_BOLT_30,
    GOLD_BOLT_31,
    GOLD_BOLT_32,
    GOLD_BOLT_33,
    GOLD_BOLT_34,
    GOLD_BOLT_35,
    GOLD_BOLT_36,
    GOLD_BOLT_37,
    GOLD_BOLT_38,
    GOLD_BOLT_39,
    GOLD_BOLT_40,
]

BOLT_PACKS: Sequence[ItemData] = [
    BOLT_PACK,
    BOLT_PACK_0,
    BOLT_PACK_1,
    BOLT_PACK_2,
    BOLT_PACK_3,
    BOLT_PACK_4,
    BOLT_PACK_5,
    BOLT_PACK_6,
    BOLT_PACK_7,
    BOLT_PACK_8,
    BOLT_PACK_9,
    BOLT_PACK_10,
    BOLT_PACK_11,
    BOLT_PACK_12,
    BOLT_PACK_13,
    BOLT_PACK_14,
    BOLT_PACK_15,
    BOLT_PACK_16,
    BOLT_PACK_17,
    BOLT_PACK_18,
    BOLT_PACK_19,
    BOLT_PACK_20,
    BOLT_PACK_21,
    BOLT_PACK_22,
    BOLT_PACK_23,
    BOLT_PACK_24,
    BOLT_PACK_25,
    BOLT_PACK_26,
]

PLANETS: Sequence[ItemData] = [
    NOVALIS_INFOBOT,
    ARIDIA_INFOBOT,
    KERWAN_INFOBOT,
    EUDORA_INFOBOT,
    RILGAR_INFOBOT,
    BLARG_INFOBOT,
    UMBRIS_INFOBOT,
    BATALIA_INFOBOT,
    GASPAR_INFOBOT,
    ORXON_INFOBOT,
    POKITARU_INFOBOT,
    HOVEN_INFOBOT,
    GEMLIK_INFOBOT,
    OLTANIS_INFOBOT,
    QUARTU_INFOBOT,
    KALEBO_INFOBOT,
    FLEET_INFOBOT,
    VELDIN_INFOBOT,
]

STARTING_PLANETS: Sequence[ItemData] = [
    NOVALIS_INFOBOT,
    KERWAN_INFOBOT,
    BLARG_INFOBOT,
    BATALIA_INFOBOT,
    ORXON_INFOBOT,
]

SKILLPOINTS: Sequence[ItemData] = [
    TAKE_AIM,
    SWING_IT,
    TRANSPORTED,
    STRIKE_A_POSE,
    BLIMPY,
    QWARKTASTIC,
    ANY_TEN,
    TRICKY,
    CLUCK_CLUCK,
    SPEEDY,
    GIRL_TROUBLE,
    JUMPER,
    ACCURACY_COUNTS,
    EAT_LEAD,
    DESTROYED,
    GUNNER,
    SNIPER,
    HEY_OVER_HERE,
    ALIEN_INVASION,
    BURIED_TREASURE,
    PEST_CONTROL,
    WHIRLYBIRDS,
    SITTING_DUCKS,
    SHATTERED_GLASS,
    BLAST_EM,
    HEAVY_TRAFFIC,
    MAGICIAN,
    SNEAKY,
    CAREFUL_CRUISE,
    GOING_COMMANDO,
]

ALL: Sequence[ItemData] = [*WEAPONS, *NON_PROGRESSIVE_WEAPONS, *PROGRESSIVE_WEAPONS, *GOLD_WEAPONS,
                           *GADGETS, *PACKS, *PROGRESSIVE_PACKS, *HELMETS, *PROGRESSIVE_HELMETS, *BOOTS,
                           *PROGRESSIVE_BOOTS, *EXTRA_ITEMS, *NON_PROGRESSIVE_HOVERBOARDS, *PROGRESSIVE_HOVERBOARDS,
                           *NON_PROGRESSIVE_TRADES, *PROGRESSIVE_TRADES, *NON_PROGRESSIVE_NANOTECHS,
                           *PROGRESSIVE_NANOTECHS, *GOLD_BOLTS, *PLANETS, *SKILLPOINTS, *BOLT_PACKS]

ITEM_POOL: Sequence[ItemData] = [*PLANETS, *WEAPONS, *GADGETS, *EXTRA_ITEMS, *SKILLPOINTS]

STARTING_WEAPONS: Sequence[ItemData] = [*WEAPONS, *NON_PROGRESSIVE_WEAPONS]
ALL_WEAPONS: Sequence[ItemData] = [*WEAPONS, *NON_PROGRESSIVE_WEAPONS, *PROGRESSIVE_WEAPONS, *GOLD_WEAPONS]
ALL_PACKS: Sequence[ItemData] = [*PACKS, *PROGRESSIVE_PACKS]
ALL_HELMETS: Sequence[ItemData] = [*HELMETS, *PROGRESSIVE_HELMETS]
ALL_BOOTS: Sequence[ItemData] = [*BOOTS, *PROGRESSIVE_BOOTS]
ALL_EXTRA_ITEMS: Sequence[ItemData] = [*EXTRA_ITEMS, *NON_PROGRESSIVE_HOVERBOARDS, *PROGRESSIVE_HOVERBOARDS,
                                       *NON_PROGRESSIVE_TRADES, *PROGRESSIVE_TRADES, *NON_PROGRESSIVE_NANOTECHS,
                                       *PROGRESSIVE_NANOTECHS]
ALL_HOVERBOARD: Sequence[ItemData] = [*NON_PROGRESSIVE_HOVERBOARDS, *PROGRESSIVE_HOVERBOARDS]
ALL_TRADE: Sequence[ItemData] = [*NON_PROGRESSIVE_TRADES, *PROGRESSIVE_TRADES]
ALL_NANOTECH: Sequence[ItemData] = [*NON_PROGRESSIVE_NANOTECHS, *PROGRESSIVE_NANOTECHS]
ALL_STARTING: Sequence[ItemData] = [*STARTING_WEAPONS, *GADGETS]

SUCK_GROUP: Sequence[ItemData] = [SUCK_CANNON, GOLD_SUCK_CANNON, PROGRESSIVE_SUCK]
BOMB_GROUP: Sequence[ItemData] = [BOMB_GLOVE, GOLD_BOMB_GLOVE, PROGRESSIVE_BOMB]
DEVASTATOR_GROUP: Sequence[ItemData] = [DEVASTATOR, GOLD_DEVASTATOR, PROGRESSIVE_DEVASTATOR]
BLASTER_GROUP: Sequence[ItemData] = [BLASTER, GOLD_BLASTER, PROGRESSIVE_BLASTER]
PYROCITOR_GROUP: Sequence[ItemData] = [PYROCITOR, GOLD_PYROCITOR, PROGRESSIVE_PYROCITOR]
MINE_GROUP: Sequence[ItemData] = [MINE_GLOVE, GOLD_MINE_GLOVE, PROGRESSIVE_MINE]
TESLA_GROUP: Sequence[ItemData] = [TESLA_CLAW, GOLD_TESLA_CLAW, PROGRESSIVE_TESLA]
DOOM_GROUP: Sequence[ItemData] = [GLOVE_OF_DOOM, GOLD_GLOVE_OF_DOOM, PROGRESSIVE_DOOM]
MORPH_GROUP: Sequence[ItemData] = [MORPH_O_RAY, GOLD_MORPH_O_RAY, PROGRESSIVE_MORPH]
DECOY_GROUP: Sequence[ItemData] = [DECOY_GLOVE, GOLD_DECOY_GLOVE, PROGRESSIVE_DECOY]

PROG: dict[str, Mapping[str, int]] = {
    HELI_PACK.name: {HELI_PACK.name: 1},
    THRUSTER_PACK.name: {THRUSTER_PACK.name: 1},
    HYDRO_PACK.name: {HYDRO_PACK.name: 1},
    SONIC_SUMMONER.name: {SONIC_SUMMONER.name: 1, PROGRESSIVE_HELMET.name: 2},
    O2_MASK.name: {O2_MASK.name: 1, PROGRESSIVE_HELMET.name: 1},
    PILOTS_HELMET.name: {PILOTS_HELMET.name: 1, PROGRESSIVE_HELMET.name: 3},
    SUCK_CANNON.name: {SUCK_CANNON.name: 1},
    GOLD_SUCK_CANNON.name: {SUCK_CANNON.name: 1, GOLD_SUCK_CANNON.name: 1},
    BOMB_GLOVE.name: {BOMB_GLOVE.name: 1},
    GOLD_BOMB_GLOVE.name: {BOMB_GLOVE.name: 1, GOLD_BOMB_GLOVE.name: 1},
    DEVASTATOR.name: {DEVASTATOR.name: 1},
    GOLD_DEVASTATOR.name: {DEVASTATOR.name: 1, GOLD_DEVASTATOR.name: 1},
    BLASTER.name: {BLASTER.name: 1},
    GOLD_BLASTER.name: {BLASTER.name: 1, GOLD_BLASTER.name: 1},
    PYROCITOR.name: {PYROCITOR.name: 1},
    GOLD_PYROCITOR.name: {PYROCITOR.name: 1, GOLD_PYROCITOR.name: 1},
    MINE_GLOVE.name: {MINE_GLOVE.name: 1},
    GOLD_MINE_GLOVE.name: {MINE_GLOVE.name: 1, GOLD_MINE_GLOVE.name: 1},
    TESLA_CLAW.name: {TESLA_CLAW.name: 1},
    GOLD_TESLA_CLAW.name: {TESLA_CLAW.name: 1, GOLD_TESLA_CLAW.name: 1},
    GLOVE_OF_DOOM.name: {GLOVE_OF_DOOM.name: 1},
    GOLD_GLOVE_OF_DOOM.name: {GLOVE_OF_DOOM.name: 1, GOLD_GLOVE_OF_DOOM.name: 1},
    MORPH_O_RAY.name: {MORPH_O_RAY.name: 1},
    GOLD_MORPH_O_RAY.name: {MORPH_O_RAY.name: 1, GOLD_MORPH_O_RAY.name: 1},
    DECOY_GLOVE.name: {DECOY_GLOVE.name: 1},
    GOLD_DECOY_GLOVE.name: {DECOY_GLOVE.name: 1, GOLD_DECOY_GLOVE.name: 1},
    MAGNEBOOTS.name: {MAGNEBOOTS.name: 1, PROGRESSIVE_BOOT.name: 2},
    GRINDBOOTS.name: {GRINDBOOTS.name: 1, PROGRESSIVE_BOOT.name: 1},
    HOVERBOARD.name: {HOVERBOARD.name: 1, PROGRESSIVE_HOVERBOARD.name: 1},
    ZOOMERATOR.name: {ZOOMERATOR.name: 1, PROGRESSIVE_HOVERBOARD.name: 2},
    PERSUADER.name: {PERSUADER.name: 1, PROGRESSIVE_TRADE.name: 1},
    RARITANIUM.name: {RARITANIUM.name: 1, PROGRESSIVE_TRADE.name: 2},
    PREMIUM_NANOTECH.name: {PREMIUM_NANOTECH.name: 1, PROGRESSIVE_NANOTECH.name: 1},
    ULTRA_NANOTECH.name: {ULTRA_NANOTECH.name: 1, PROGRESSIVE_NANOTECH.name: 2},
}


def get_bolt_pack(options) -> str:
    lookup: dict[int, str] = {
        BOLT_PACK_0.quantity: BOLT_PACK_0.name,
        BOLT_PACK_1.quantity: BOLT_PACK_1.name,
        BOLT_PACK_2.quantity: BOLT_PACK_2.name,
        BOLT_PACK_3.quantity: BOLT_PACK_3.name,
        BOLT_PACK_4.quantity: BOLT_PACK_4.name,
        BOLT_PACK_5.quantity: BOLT_PACK_5.name,
        BOLT_PACK_6.quantity: BOLT_PACK_6.name,
        BOLT_PACK_7.quantity: BOLT_PACK_7.name,
        BOLT_PACK_8.quantity: BOLT_PACK_8.name,
        BOLT_PACK_9.quantity: BOLT_PACK_9.name,
        BOLT_PACK_10.quantity: BOLT_PACK_10.name,
        BOLT_PACK_11.quantity: BOLT_PACK_11.name,
        BOLT_PACK_12.quantity: BOLT_PACK_12.name,
        BOLT_PACK_13.quantity: BOLT_PACK_13.name,
        BOLT_PACK_14.quantity: BOLT_PACK_14.name,
        BOLT_PACK_15.quantity: BOLT_PACK_15.name,
        BOLT_PACK_16.quantity: BOLT_PACK_16.name,
        BOLT_PACK_17.quantity: BOLT_PACK_17.name,
        BOLT_PACK_18.quantity: BOLT_PACK_18.name,
        BOLT_PACK_19.quantity: BOLT_PACK_19.name,
        BOLT_PACK_20.quantity: BOLT_PACK_20.name,
        BOLT_PACK_21.quantity: BOLT_PACK_21.name,
        BOLT_PACK_22.quantity: BOLT_PACK_22.name,
        BOLT_PACK_23.quantity: BOLT_PACK_23.name,
        BOLT_PACK_24.quantity: BOLT_PACK_24.name,
        BOLT_PACK_25.quantity: BOLT_PACK_25.name,
        BOLT_PACK_26.quantity: BOLT_PACK_26.name,
    }
    return lookup[options.pack_size_bolts.value]


def get_gold_bolts(options) -> str:
    lookup: dict[int, str] = {}
    for gold_bolt in GOLD_BOLTS:
        if gold_bolt.name == RAC1ITEM.GOLD_BOLT:
            continue
        lookup.update({gold_bolt.quantity: gold_bolt.name})
    return lookup[options.pack_size_gold_bolts.value]


def progression_rules(world):
    match world.options.progressive_weapons.value:
        case Options.GoldWeaponProgression.option_normal:
            PROG[SUCK_CANNON.name] = {SUCK_CANNON.name: 1, GOLD_SUCK_CANNON.name: 1}
            PROG[GOLD_SUCK_CANNON.name] = {GOLD_SUCK_CANNON.name: 1}
            PROG[BOMB_GLOVE.name] = {BOMB_GLOVE.name: 1, GOLD_BOMB_GLOVE.name: 1}
            PROG[GOLD_BOMB_GLOVE.name] = {GOLD_BOMB_GLOVE.name: 1}
            PROG[DEVASTATOR.name] = {DEVASTATOR.name: 1, GOLD_DEVASTATOR.name: 1}
            PROG[GOLD_DEVASTATOR.name] = {GOLD_DEVASTATOR.name: 1}
            PROG[BLASTER.name] = {BLASTER.name: 1, GOLD_BLASTER.name: 1}
            PROG[GOLD_BLASTER.name] = {GOLD_BLASTER.name: 1}
            PROG[PYROCITOR.name] = {PYROCITOR.name: 1, GOLD_PYROCITOR.name: 1}
            PROG[GOLD_PYROCITOR.name] = {GOLD_PYROCITOR.name: 1}
            PROG[MINE_GLOVE.name] = {MINE_GLOVE.name: 1, GOLD_MINE_GLOVE.name: 1}
            PROG[GOLD_MINE_GLOVE.name] = {GOLD_MINE_GLOVE.name: 1}
            PROG[TESLA_CLAW.name] = {TESLA_CLAW.name: 1, GOLD_TESLA_CLAW.name: 1}
            PROG[GOLD_TESLA_CLAW.name] = {GOLD_TESLA_CLAW.name: 1}
            PROG[GLOVE_OF_DOOM.name] = {GLOVE_OF_DOOM.name: 1, GOLD_GLOVE_OF_DOOM.name: 1}
            PROG[GOLD_GLOVE_OF_DOOM.name] = {GOLD_GLOVE_OF_DOOM.name: 1}
            PROG[MORPH_O_RAY.name] = {MORPH_O_RAY.name: 1, GOLD_MORPH_O_RAY.name: 1}
            PROG[GOLD_MORPH_O_RAY.name] = {GOLD_MORPH_O_RAY.name: 1}
            PROG[DECOY_GLOVE.name] = {DECOY_GLOVE.name: 1, GOLD_DECOY_GLOVE.name: 1}
            PROG[GOLD_DECOY_GLOVE.name] = {GOLD_DECOY_GLOVE.name: 1}
        case Options.GoldWeaponProgression.option_progressive:
            PROG[SUCK_CANNON.name] = {PROGRESSIVE_SUCK.name: 1}
            PROG[GOLD_SUCK_CANNON.name] = {PROGRESSIVE_SUCK.name: 2}
            PROG[BOMB_GLOVE.name] = {PROGRESSIVE_BOMB.name: 1}
            PROG[GOLD_BOMB_GLOVE.name] = {PROGRESSIVE_BOMB.name: 2}
            PROG[DEVASTATOR.name] = {PROGRESSIVE_DEVASTATOR.name: 1}
            PROG[GOLD_DEVASTATOR.name] = {PROGRESSIVE_DEVASTATOR.name: 2}
            PROG[BLASTER.name] = {PROGRESSIVE_BLASTER.name: 1}
            PROG[GOLD_BLASTER.name] = {PROGRESSIVE_BLASTER.name: 2}
            PROG[PYROCITOR.name] = {PROGRESSIVE_PYROCITOR.name: 1}
            PROG[GOLD_PYROCITOR.name] = {PROGRESSIVE_PYROCITOR.name: 2}
            PROG[MINE_GLOVE.name] = {PROGRESSIVE_MINE.name: 1}
            PROG[GOLD_MINE_GLOVE.name] = {PROGRESSIVE_MINE.name: 2}
            PROG[TESLA_CLAW.name] = {PROGRESSIVE_TESLA.name: 1}
            PROG[GOLD_TESLA_CLAW.name] = {PROGRESSIVE_TESLA.name: 2}
            PROG[GLOVE_OF_DOOM.name] = {PROGRESSIVE_DOOM.name: 1}
            PROG[GOLD_GLOVE_OF_DOOM.name] = {PROGRESSIVE_DOOM.name: 2}
            PROG[MORPH_O_RAY.name] = {PROGRESSIVE_MORPH.name: 1}
            PROG[GOLD_MORPH_O_RAY.name] = {PROGRESSIVE_MORPH.name: 2}
            PROG[DECOY_GLOVE.name] = {PROGRESSIVE_DECOY.name: 1}
            PROG[GOLD_DECOY_GLOVE.name] = {PROGRESSIVE_DECOY.name: 2}
        case Options.GoldWeaponProgression.option_progressive_reversed:
            world.orders[RAC1ORDER.SUCK_CANNON].reverse()
            PROG[SUCK_CANNON.name] = {PROGRESSIVE_SUCK.name: 1}
            PROG[GOLD_SUCK_CANNON.name] = {PROGRESSIVE_SUCK.name: 1}
            world.orders[RAC1ORDER.BOMB_GLOVE].reverse()
            PROG[BOMB_GLOVE.name] = {PROGRESSIVE_BOMB.name: 1}
            PROG[GOLD_BOMB_GLOVE.name] = {PROGRESSIVE_BOMB.name: 1}
            world.orders[RAC1ORDER.DEVASTATOR].reverse()
            PROG[DEVASTATOR.name] = {PROGRESSIVE_DEVASTATOR.name: 1}
            PROG[GOLD_DEVASTATOR.name] = {PROGRESSIVE_DEVASTATOR.name: 1}
            world.orders[RAC1ORDER.BLASTER].reverse()
            PROG[BLASTER.name] = {PROGRESSIVE_BLASTER.name: 1}
            PROG[GOLD_BLASTER.name] = {PROGRESSIVE_BLASTER.name: 1}
            world.orders[RAC1ORDER.PYROCITOR].reverse()
            PROG[PYROCITOR.name] = {PROGRESSIVE_PYROCITOR.name: 1}
            PROG[GOLD_PYROCITOR.name] = {PROGRESSIVE_PYROCITOR.name: 1}
            world.orders[RAC1ORDER.MINE_GLOVE].reverse()
            PROG[MINE_GLOVE.name] = {PROGRESSIVE_MINE.name: 1}
            PROG[GOLD_MINE_GLOVE.name] = {PROGRESSIVE_MINE.name: 1}
            world.orders[RAC1ORDER.TESLA_CLAW].reverse()
            PROG[TESLA_CLAW.name] = {PROGRESSIVE_TESLA.name: 1}
            PROG[GOLD_TESLA_CLAW.name] = {PROGRESSIVE_TESLA.name: 1}
            world.orders[RAC1ORDER.GLOVE_OF_DOOM].reverse()
            PROG[GLOVE_OF_DOOM.name] = {PROGRESSIVE_DOOM.name: 1}
            PROG[GOLD_GLOVE_OF_DOOM.name] = {PROGRESSIVE_DOOM.name: 1}
            world.orders[RAC1ORDER.MORPH_O_RAY].reverse()
            PROG[MORPH_O_RAY.name] = {PROGRESSIVE_MORPH.name: 1}
            PROG[GOLD_MORPH_O_RAY.name] = {PROGRESSIVE_MORPH.name: 1}
            world.orders[RAC1ORDER.DECOY_GLOVE].reverse()
            PROG[DECOY_GLOVE.name] = {PROGRESSIVE_DECOY.name: 1}
            PROG[GOLD_DECOY_GLOVE.name] = {PROGRESSIVE_DECOY.name: 1}
        case Options.GoldWeaponProgression.option_progressive_random:
            world.random.shuffle(world.orders[RAC1ORDER.SUCK_CANNON])
            PROG[SUCK_CANNON.name] = {PROGRESSIVE_SUCK.name: 1}
            PROG[GOLD_SUCK_CANNON.name] = {PROGRESSIVE_SUCK.name: 1 + world.orders[
                RAC1ORDER.SUCK_CANNON].index(GOLD_SUCK_CANNON.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.BOMB_GLOVE])
            PROG[BOMB_GLOVE.name] = {PROGRESSIVE_BOMB.name: 1}
            PROG[GOLD_BOMB_GLOVE.name] = {PROGRESSIVE_BOMB.name: 1 + world.orders[
                RAC1ORDER.BOMB_GLOVE].index(GOLD_BOMB_GLOVE.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.DEVASTATOR])
            PROG[DEVASTATOR.name] = {PROGRESSIVE_DEVASTATOR.name: 1}
            PROG[GOLD_DEVASTATOR.name] = {PROGRESSIVE_DEVASTATOR.name: 1 + world.orders[
                RAC1ORDER.DEVASTATOR].index(GOLD_DEVASTATOR.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.BLASTER])
            PROG[BLASTER.name] = {PROGRESSIVE_BLASTER.name: 1}
            PROG[GOLD_BLASTER.name] = {PROGRESSIVE_BLASTER.name: 1 + world.orders[
                RAC1ORDER.BLASTER].index(GOLD_BLASTER.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.PYROCITOR])
            PROG[PYROCITOR.name] = {PROGRESSIVE_PYROCITOR.name: 1}
            PROG[GOLD_PYROCITOR.name] = {PROGRESSIVE_PYROCITOR.name: 1 + world.orders[
                RAC1ORDER.PYROCITOR].index(GOLD_PYROCITOR.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.MINE_GLOVE])
            PROG[MINE_GLOVE.name] = {PROGRESSIVE_MINE.name: 1}
            PROG[GOLD_MINE_GLOVE.name] = {PROGRESSIVE_MINE.name: 1 + world.orders[
                RAC1ORDER.MINE_GLOVE].index(GOLD_MINE_GLOVE.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.TESLA_CLAW])
            PROG[TESLA_CLAW.name] = {PROGRESSIVE_TESLA.name: 1}
            PROG[GOLD_TESLA_CLAW.name] = {PROGRESSIVE_TESLA.name: 1 + world.orders[
                RAC1ORDER.TESLA_CLAW].index(TESLA_CLAW.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.GLOVE_OF_DOOM])
            PROG[GLOVE_OF_DOOM.name] = {PROGRESSIVE_DOOM.name: 1}
            PROG[GOLD_GLOVE_OF_DOOM.name] = {PROGRESSIVE_DOOM.name: 1 + world.orders[
                RAC1ORDER.GLOVE_OF_DOOM].index(GOLD_GLOVE_OF_DOOM.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.MORPH_O_RAY])
            PROG[MORPH_O_RAY.name] = {PROGRESSIVE_MORPH.name: 1}
            PROG[GOLD_MORPH_O_RAY.name] = {PROGRESSIVE_MORPH.name: 1 + world.orders[
                RAC1ORDER.MORPH_O_RAY].index(GOLD_MORPH_O_RAY.item_id)}
            world.random.shuffle(world.orders[RAC1ORDER.DECOY_GLOVE])
            PROG[DECOY_GLOVE.name] = {PROGRESSIVE_DECOY.name: 1}
            PROG[GOLD_DECOY_GLOVE.name] = {PROGRESSIVE_DECOY.name: 1 + world.orders[
                RAC1ORDER.DECOY_GLOVE].index(GOLD_DECOY_GLOVE.item_id)}
        case _:
            pass

    match world.options.progressive_packs.value:
        case Options.ProgressiveOptions.option_progressive:
            PROG[HELI_PACK.name] = {PROGRESSIVE_PACK.name: 1}
            PROG[THRUSTER_PACK.name] = {PROGRESSIVE_PACK.name: 2}
            PROG[HYDRO_PACK.name] = {PROGRESSIVE_PACK.name: 3}
        case Options.ProgressiveOptions.option_progressive_reversed:
            world.orders[RAC1ORDER.PACKS].reverse()
            PROG[HELI_PACK.name] = {PROGRESSIVE_PACK.name: 3}
            PROG[THRUSTER_PACK.name] = {PROGRESSIVE_PACK.name: 2}
            PROG[HYDRO_PACK.name] = {PROGRESSIVE_PACK.name: 1}
        case Options.ProgressiveOptions.option_progressive_random:
            world.random.shuffle(world.orders[RAC1ORDER.PACKS])
            PROG[HELI_PACK.name] = {
                PROGRESSIVE_PACK.name: 1 + world.orders[RAC1ORDER.PACKS].index(HELI_PACK.item_id)}
            PROG[THRUSTER_PACK.name] = {
                PROGRESSIVE_PACK.name: 1 + world.orders[RAC1ORDER.PACKS].index(THRUSTER_PACK.item_id)}
            PROG[HYDRO_PACK.name] = {
                PROGRESSIVE_PACK.name: 1 + world.orders[RAC1ORDER.PACKS].index(HYDRO_PACK.item_id)}
        case _:
            pass

    match world.options.progressive_helmets.value:
        case Options.ProgressiveOptions.option_progressive:
            PROG[O2_MASK.name] = {PROGRESSIVE_HELMET.name: 1}
            if world.options.shuffle_helmets.value <= Options.ItemOptions.option_random_same:
                PROG[SONIC_SUMMONER.name] = {PROGRESSIVE_HELMET.name: 3}
                PROG[PILOTS_HELMET.name] = {PROGRESSIVE_HELMET.name: 2}
                world.orders[RAC1ORDER.HELMETS] = [O2_MASK.item_id, PILOTS_HELMET.item_id,
                                                             SONIC_SUMMONER.item_id]
            else:
                PROG[SONIC_SUMMONER.name] = {PROGRESSIVE_HELMET.name: 2}
                PROG[PILOTS_HELMET.name] = {PROGRESSIVE_HELMET.name: 3}
        case Options.ProgressiveOptions.option_progressive_reversed:
            world.orders[RAC1ORDER.HELMETS].reverse()
            PROG[O2_MASK.name] = {PROGRESSIVE_HELMET.name: 3}
            PROG[SONIC_SUMMONER.name] = {PROGRESSIVE_HELMET.name: 2}
            PROG[PILOTS_HELMET.name] = {PROGRESSIVE_HELMET.name: 1}
        case Options.ProgressiveOptions.option_progressive_random:
            world.random.shuffle(world.orders[RAC1ORDER.HELMETS])
            PROG[O2_MASK.name] = {
                PROGRESSIVE_HELMET.name: 1 + world.orders[RAC1ORDER.HELMETS].index(O2_MASK.item_id)}
            PROG[SONIC_SUMMONER.name] = {
                PROGRESSIVE_HELMET.name: 1 + world.orders[RAC1ORDER.HELMETS].index(SONIC_SUMMONER.item_id)}
            PROG[PILOTS_HELMET.name] = {
                PROGRESSIVE_HELMET.name: 1 + world.orders[RAC1ORDER.HELMETS].index(PILOTS_HELMET.item_id)}
            if (world.options.shuffle_helmets.value <= Options.ItemOptions.option_random_same
                    and PROG[PILOTS_HELMET.name].values() == 3):
                temp = PROG[PILOTS_HELMET.name]
                PROG[PILOTS_HELMET.name] = PROG[SONIC_SUMMONER.name]
                PROG[SONIC_SUMMONER.name] = temp
                if world.orders[RAC1ORDER.HELMETS].index(O2_MASK.item_id) == 0:
                    world.orders[RAC1ORDER.HELMETS] = [O2_MASK.item_id, PILOTS_HELMET.item_id,
                                                                 SONIC_SUMMONER.item_id]
                else:
                    world.orders[RAC1ORDER.HELMETS] = [PILOTS_HELMET.item_id, O2_MASK.item_id,
                                                                 SONIC_SUMMONER.item_id]

        case _:
            pass

    match world.options.progressive_boots.value:
        case Options.ProgressiveOptions.option_progressive:
            PROG[GRINDBOOTS.name] = {PROGRESSIVE_BOOT.name: 1}
            PROG[MAGNEBOOTS.name] = {PROGRESSIVE_BOOT.name: 2}
        case Options.ProgressiveOptions.option_progressive_reversed:
            world.orders[RAC1ORDER.BOOTS].reverse()
            PROG[GRINDBOOTS.name] = {PROGRESSIVE_BOOT.name: 2}
            PROG[MAGNEBOOTS.name] = {PROGRESSIVE_BOOT.name: 1}
        case Options.ProgressiveOptions.option_progressive_random:
            world.random.shuffle(world.orders[RAC1ORDER.BOOTS])
            PROG[GRINDBOOTS.name] = {
                PROGRESSIVE_BOOT.name: 1 + world.orders[RAC1ORDER.BOOTS].index(GRINDBOOTS.item_id)}
            PROG[MAGNEBOOTS.name] = {
                PROGRESSIVE_BOOT.name: 1 + world.orders[RAC1ORDER.BOOTS].index(MAGNEBOOTS.item_id)}
        case _:
            pass

    if world.options.shuffle_extra_items.value == Options.ItemOptions.option_vanilla:
        PROG[HOVERBOARD.name] = {HOVERBOARD.name: 1, PROGRESSIVE_HOVERBOARD.name: 1}
        PROG[ZOOMERATOR.name] = {ZOOMERATOR.name: 1, PROGRESSIVE_HOVERBOARD.name: 2}
    else:
        match world.options.progressive_hoverboard.value:
            case Options.ProgressiveOptions.option_progressive:
                PROG[HOVERBOARD.name] = {PROGRESSIVE_HOVERBOARD.name: 1}
                PROG[ZOOMERATOR.name] = {PROGRESSIVE_HOVERBOARD.name: 2}
            case Options.ProgressiveOptions.option_progressive_reversed:
                world.orders[RAC1ORDER.HOVERBOARD].reverse()
                PROG[HOVERBOARD.name] = {PROGRESSIVE_HOVERBOARD.name: 2}
                PROG[ZOOMERATOR.name] = {PROGRESSIVE_HOVERBOARD.name: 1}
            case Options.ProgressiveOptions.option_progressive_random:
                world.random.shuffle(world.orders[RAC1ORDER.HOVERBOARD])
                PROG[HOVERBOARD.name] = {
                    PROGRESSIVE_HOVERBOARD.name: 1 + world.orders[RAC1ORDER.HOVERBOARD].index(
                        HOVERBOARD.item_id)}
                PROG[ZOOMERATOR.name] = {
                    PROGRESSIVE_HOVERBOARD.name: 1 + world.orders[RAC1ORDER.HOVERBOARD].index(
                        ZOOMERATOR.item_id)}
            case _:
                pass
    if world.options.shuffle_extra_items.value == Options.ItemOptions.option_vanilla:
        PROG[RARITANIUM.name] = {RARITANIUM.name: 1, PROGRESSIVE_TRADE.name: 1}
        PROG[PERSUADER.name] = {PERSUADER.name: 1, PROGRESSIVE_TRADE.name: 2}
    else:
        match world.options.progressive_raritanium.value:
            case Options.ProgressiveOptions.option_progressive:
                PROG[RARITANIUM.name] = {PROGRESSIVE_TRADE.name: 1}
                PROG[PERSUADER.name] = {PROGRESSIVE_TRADE.name: 2}
            case Options.ProgressiveOptions.option_progressive_reversed:
                world.orders[RAC1ORDER.TRADE].reverse()
                PROG[RARITANIUM.name] = {PROGRESSIVE_TRADE.name: 2}
                PROG[PERSUADER.name] = {PROGRESSIVE_TRADE.name: 1}
            case Options.ProgressiveOptions.option_progressive_random:
                world.random.shuffle(world.orders[RAC1ORDER.TRADE])
                PROG[RARITANIUM.name] = {
                    PROGRESSIVE_TRADE.name: 1 + world.orders[RAC1ORDER.TRADE].index(RARITANIUM.item_id)}
                PROG[PERSUADER.name] = {
                    PROGRESSIVE_TRADE.name: 1 + world.orders[RAC1ORDER.TRADE].index(PERSUADER.item_id)}
            case _:
                pass

    match world.options.progressive_nanotech.value:
        case Options.ProgressiveOptions.option_progressive:
            PROG[PREMIUM_NANOTECH.name] = {PROGRESSIVE_NANOTECH.name: 1}
            PROG[ULTRA_NANOTECH.name] = {PROGRESSIVE_NANOTECH.name: 2}
        case Options.ProgressiveOptions.option_progressive_reversed:
            world.orders[RAC1ORDER.NANOTECH].reverse()
            PROG[PREMIUM_NANOTECH.name] = {PROGRESSIVE_NANOTECH.name: 2}
            PROG[ULTRA_NANOTECH.name] = {PROGRESSIVE_NANOTECH.name: 1}
        case Options.ProgressiveOptions.option_progressive_random:
            world.random.shuffle(world.orders[RAC1ORDER.NANOTECH])
            PROG[PREMIUM_NANOTECH.name] = {PROGRESSIVE_NANOTECH.name: 1 + world.orders[
                RAC1ORDER.NANOTECH].index(PREMIUM_NANOTECH.item_id)}
            PROG[ULTRA_NANOTECH.name] = {PROGRESSIVE_NANOTECH.name: 1 + world.orders[
                RAC1ORDER.NANOTECH].index(ULTRA_NANOTECH.item_id)}
        case _:
            pass
    return


def get_pool(options) -> Sequence[ItemData]:
    pool = []
    for item in ITEM_POOL:
        pool += [item]
    if options.progressive_weapons.value > Options.GoldWeaponProgression.option_normal:
        for item in PROGRESSIVE_WEAPONS:
            pool += [item, item]
    else:
        for item in NON_PROGRESSIVE_WEAPONS:
            pool += [item]
        for item in GOLD_WEAPONS:
            pool += [item]
    if options.progressive_packs.value > Options.ProgressiveOptions.option_vanilla:
        for item in PROGRESSIVE_PACKS:
            pool += [item]
    else:
        for item in PACKS:
            pool += [item]
    if options.progressive_helmets.value > Options.ProgressiveOptions.option_vanilla:
        for item in PROGRESSIVE_HELMETS:
            pool += [item]
    else:
        for item in HELMETS:
            pool += [item]
    if options.progressive_boots.value > Options.ProgressiveOptions.option_vanilla:
        for item in PROGRESSIVE_BOOTS:
            pool += [item]
    else:
        for item in BOOTS:
            pool += [item]
    if options.progressive_hoverboard.value > Options.ProgressiveOptions.option_vanilla:
        for item in PROGRESSIVE_HOVERBOARDS:
            pool += [item]
    else:
        for item in NON_PROGRESSIVE_HOVERBOARDS:
            pool += [item]
    if options.progressive_raritanium.value > Options.ProgressiveOptions.option_vanilla:
        for item in PROGRESSIVE_TRADES:
            pool += [item]
    else:
        for item in NON_PROGRESSIVE_TRADES:
            pool += [item]
    if options.progressive_nanotech.value > Options.ProgressiveOptions.option_vanilla:
        for item in PROGRESSIVE_NANOTECHS:
            pool += [item]
    else:
        for item in NON_PROGRESSIVE_NANOTECHS:
            pool += [item]
    lookup: dict[int, tuple[ItemData, int]] = {
        1: (GOLD_BOLT_1, 40),
        2: (GOLD_BOLT_2, 30),
        3: (GOLD_BOLT_3, 20),
        4: (GOLD_BOLT_4, 15),
        5: (GOLD_BOLT_5, 12),
        6: (GOLD_BOLT_6, 10),
        7: (GOLD_BOLT_7, 9),
        8: (GOLD_BOLT_8, 8),
        9: (GOLD_BOLT_9, 7),
        10: (GOLD_BOLT_10, 6),
        11: (GOLD_BOLT_11, 5),
        12: (GOLD_BOLT_12, 5),
        13: (GOLD_BOLT_13, 5),
        14: (GOLD_BOLT_14, 4),
        15: (GOLD_BOLT_15, 4),
        16: (GOLD_BOLT_16, 4),
        17: (GOLD_BOLT_17, 4),
        18: (GOLD_BOLT_18, 4),
        19: (GOLD_BOLT_19, 4),
        20: (GOLD_BOLT_20, 3),
        21: (GOLD_BOLT_21, 3),
        22: (GOLD_BOLT_22, 3),
        23: (GOLD_BOLT_23, 3),
        24: (GOLD_BOLT_24, 3),
        25: (GOLD_BOLT_25, 3),
        26: (GOLD_BOLT_26, 3),
        27: (GOLD_BOLT_27, 3),
        28: (GOLD_BOLT_28, 3),
        29: (GOLD_BOLT_29, 3),
        30: (GOLD_BOLT_30, 2),
        31: (GOLD_BOLT_31, 2),
        32: (GOLD_BOLT_32, 2),
        33: (GOLD_BOLT_33, 2),
        34: (GOLD_BOLT_34, 2),
        35: (GOLD_BOLT_35, 2),
        36: (GOLD_BOLT_36, 2),
        37: (GOLD_BOLT_37, 2),
        38: (GOLD_BOLT_38, 2),
        39: (GOLD_BOLT_39, 2),
        40: (GOLD_BOLT_40, 1),
    }
    for _ in range(lookup[options.pack_size_gold_bolts.value][1]):
        pool += [lookup[options.pack_size_gold_bolts.value][0]]
    return pool


def get_starting_planets(options) -> Sequence[ItemData]:
    planets: Sequence[ItemData] = []
    for item in STARTING_PLANETS:
        planets += [item]
    if options.shuffle_infobots.value >= Options.ShuffleInfobots.option_unrestricted:
        planets += [ARIDIA_INFOBOT]
        if options.shuffle_helmets.value >= Options.ShuffleHelmets.option_unrestricted:
            planets += [GASPAR_INFOBOT]
        if options.shuffle_gold_bolts.value:
            planets += [HOVEN_INFOBOT]
    return planets


def from_id(item_id: int) -> ItemData:
    matching = [item for item in ALL if item.item_id == item_id]
    if len(matching) == 0:
        raise ValueError(f"No item data for item id '{item_id}'")
    assert len(matching) < 2, f"{len(matching)} item data found with id '{item_id}'. Items are: {matching}"
    return matching[0]


def from_name(item_name: str) -> ItemData:
    matching = [item for item in ALL if item.name == item_name]
    if len(matching) == 0:
        raise ValueError(f"No item data for '{item_name}'")
    # if item_name != GOLD_BOLT.name:
    #     assert len(matching) < 2, f"Multiple item data with name '{item_name}'. Please report."
    return matching[0]


def get_item_groups() -> dict[str, set[str]]:
    groups: dict[str, set[str]] = {
        RAC1POOL.WEAPONS: {w.name for w in ALL_WEAPONS},
        RAC1POOL.GADGETS: {g.name for g in GADGETS},
        RAC1POOL.PACKS: {p.name for p in ALL_PACKS},
        RAC1POOL.HELMETS: {h.name for h in ALL_HELMETS},
        RAC1POOL.BOOTS: {b.name for b in ALL_BOOTS},
        RAC1POOL.EXTRA_ITEMS: {e.name for e in ALL_EXTRA_ITEMS},
        RAC1POOL.GOLD_BOLTS: {c.name for c in GOLD_BOLTS},
        RAC1POOL.INFOBOTS: {i.name for i in PLANETS},
        RAC1POOL.SKILLPOINT: {s.name for s in SKILLPOINTS},
    }
    return groups


def check_progressive_item(options, item) -> str:
    new_item = item
    match from_name(item).pool:
        case SUCK_CANNON.pool | GOLD_SUCK_CANNON.pool:
            if options.progressive_weapons.value > Options.GoldWeaponProgression.option_normal:
                match item:
                    case SUCK_CANNON.name:
                        new_item = PROGRESSIVE_SUCK.name
                    case GOLD_SUCK_CANNON.name:
                        new_item = PROGRESSIVE_SUCK.name
                    case BOMB_GLOVE.name:
                        new_item = PROGRESSIVE_BOMB.name
                    case GOLD_BOMB_GLOVE.name:
                        new_item = PROGRESSIVE_BOMB.name
                    case DEVASTATOR.name:
                        new_item = PROGRESSIVE_DEVASTATOR.name
                    case GOLD_DEVASTATOR.name:
                        new_item = PROGRESSIVE_DEVASTATOR.name
                    case BLASTER.name:
                        new_item = PROGRESSIVE_BLASTER.name
                    case GOLD_BLASTER.name:
                        new_item = PROGRESSIVE_BLASTER.name
                    case PYROCITOR.name:
                        new_item = PROGRESSIVE_PYROCITOR.name
                    case GOLD_PYROCITOR.name:
                        new_item = PROGRESSIVE_PYROCITOR.name
                    case MINE_GLOVE.name:
                        new_item = PROGRESSIVE_MINE.name
                    case GOLD_MINE_GLOVE.name:
                        new_item = PROGRESSIVE_MINE.name
                    case TESLA_CLAW.name:
                        new_item = PROGRESSIVE_TESLA.name
                    case GOLD_TESLA_CLAW.name:
                        new_item = PROGRESSIVE_TESLA.name
                    case GLOVE_OF_DOOM.name:
                        new_item = PROGRESSIVE_DOOM.name
                    case GOLD_GLOVE_OF_DOOM.name:
                        new_item = PROGRESSIVE_DOOM.name
                    case MORPH_O_RAY.name:
                        new_item = PROGRESSIVE_MORPH.name
                    case GOLD_MORPH_O_RAY.name:
                        new_item = PROGRESSIVE_MORPH.name
                    case DECOY_GLOVE.name:
                        new_item = PROGRESSIVE_DECOY.name
                    case GOLD_DECOY_GLOVE.name:
                        new_item = PROGRESSIVE_DECOY.name
        case HELI_PACK.pool:
            if options.progressive_packs.value:
                new_item = PROGRESSIVE_PACK.name
        case O2_MASK.pool:
            if options.progressive_helmets.value:
                new_item = PROGRESSIVE_HELMET.name
        case GRINDBOOTS.pool:
            if options.progressive_boots.value:
                new_item = PROGRESSIVE_BOOT.name
        case HOVERBOARD.pool:
            match item:
                case HOVERBOARD.name | ZOOMERATOR.name:
                    if options.progressive_hoverboard.value:
                        new_item = PROGRESSIVE_HOVERBOARD.name
                case RARITANIUM.name | PERSUADER.name:
                    if options.progressive_raritanium.value:
                        new_item = PROGRESSIVE_TRADE.name
                case PREMIUM_NANOTECH.name | ULTRA_NANOTECH.name:
                    if options.progressive_nanotech.value:
                        new_item = PROGRESSIVE_NANOTECH.name
        case _:
            pass
    return new_item
