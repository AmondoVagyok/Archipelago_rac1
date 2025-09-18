import logging

from BaseClasses import CollectionState
from .data import Items

rac_logger = logging.getLogger("Ratchet & Clank")
rac_logger.setLevel(logging.DEBUG)


def can_improved_jump(state: CollectionState, player: int) -> bool:
    return (state.has_any_count(Items.PROG[Items.HELI_PACK.name], player)
            or state.has_any_count(Items.PROG[Items.THRUSTER_PACK.name], player))


def can_heli_high_jump(state: CollectionState, player: int) -> bool:  # relevant for eudora gold bolt
    return state.has_any_count(Items.PROG[Items.HELI_PACK.name], player)


def can_glide(state: CollectionState, player: int) -> bool:  # gliding is not possible without the heli pack
    return state.has_any_count(Items.PROG[Items.HELI_PACK.name], player)


def can_ground_pound(state: CollectionState, player: int) -> bool:
    return state.has_any_count(Items.PROG[Items.THRUSTER_PACK.name], player)


def has_hydro_pack(state: CollectionState, player: int) -> bool:
    return state.has_any_count(Items.PROG[Items.HYDRO_PACK.name], player)


def has_sonic(state: CollectionState, player: int) -> bool:
    return state.has_any_count(Items.PROG[Items.SONIC_SUMMONER.name], player)


def has_o2_mask(state: CollectionState, player: int) -> bool:
    return state.has_any_count(Items.PROG[Items.O2_MASK.name], player)


def has_pilots_helmet(state: CollectionState, player: int) -> bool:
    return state.has_any_count(Items.PROG[Items.PILOTS_HELMET.name], player)


def has_devastator(state: CollectionState, player: int) -> bool:
    return state.has_any_count(Items.PROG[Items.DEVASTATOR.name], player)


def has_swingshot(state: CollectionState, player: int) -> bool:
    return state.has(Items.SWINGSHOT.name, player)


def has_visibomb(state: CollectionState, player: int) -> bool:
    return state.has(Items.VISIBOMB.name, player)


def has_taunter(state: CollectionState, player: int) -> bool:
    return state.has(Items.TAUNTER.name, player)


def has_blaster(state: CollectionState, player: int) -> bool:
    return state.has(Items.BLASTER.name, player)


def has_morph(state: CollectionState, player: int) -> bool:
    return state.has_any_count(Items.PROG[Items.MORPH_O_RAY.name], player)


def has_hydrodisplacer(state: CollectionState, player: int) -> bool:
    return state.has(Items.HYDRODISPLACER.name, player)


def has_trespasser(state: CollectionState, player: int) -> bool:
    return state.has(Items.TRESPASSER.name, player)


def has_7500_bolts(state: CollectionState, player: int) -> bool:
    return has_metal_detector(state, player) or has_bolts(state, player, 7500)


def has_10k_bolts(state: CollectionState, player: int) -> bool:
    return has_metal_detector(state, player) or has_bolts(state, player, 10000)


def has_15k_bolts(state: CollectionState, player: int) -> bool:
    return has_metal_detector(state, player) or has_bolts(state, player, 15000)


def has_20k_bolts(state: CollectionState, player: int) -> bool:
    return has_metal_detector(state, player) or has_bolts(state, player, 20000)


def has_30k_bolts(state: CollectionState, player: int) -> bool:
    return has_metal_detector(state, player) or has_bolts(state, player, 30000)


def has_40k_bolts(state: CollectionState, player: int) -> bool:
    return has_metal_detector(state, player) or has_bolts(state, player, 40000)


def has_60k_bolts(state: CollectionState, player: int) -> bool:
    return has_metal_detector(state, player) or has_bolts(state, player, 60000)


def has_150k_bolts(state: CollectionState, player: int) -> bool:
    return has_metal_detector(state, player) or has_bolts(state, player, 150000)


def can_buy(state: CollectionState, player: int, bolts: int) -> bool:
    match state.multiworld.worlds[player].options.vendor_logic.value:
        case 0:
            logic = True
        case 1:
            logic = has_metal_detector(state, player) or has_bolts(state, player, bolts)
        case _:
            logic = has_metal_detector(state, player)
    return logic


def has_metal_detector(state: CollectionState, player: int) -> bool:
    return (state.has(Items.METAL_DETECTOR.name, player)
            and (
                early_metal_spots(state, player)
                or blarg_metal_spots(state, player)
                or rilgar_metal_spots(state, player)
                or umbris_metal_spots(state, player)
                or gaspar_metal_spots(state, player)
                or orxon_metal_spots(state, player)
                or gemlik_metal_spots(state, player)
                or oltanis_metal_spots(state, player)
                or kalebo_metal_spots(state, player)
                or fleet_metal_spots(state, player)
                or veldin_metal_spots(state, player)
            ))


def early_metal_spots(state: CollectionState, player: int) -> bool:
    return state.has_any([
        Items.NOVALIS_INFOBOT.name,
        Items.KERWAN_INFOBOT.name,
        Items.ARIDIA_INFOBOT.name,
        Items.EUDORA_INFOBOT.name,
        Items.BATALIA_INFOBOT.name,
        Items.POKITARU_INFOBOT.name,
        Items.HOVEN_INFOBOT.name,
        Items.QUARTU_INFOBOT.name,
    ], player)


def has_bolts(state: CollectionState, player: int, count: int) -> bool:
    # 500,
    # 1000 * 3,
    # 2000 * 5,
    # 2500 * 3,
    # 4000 * 2,
    # 7500 * 5,
    # 10000 * 5,
    # 15000,
    # 20000 * 3
    # 30000 * 2,
    # 40000,
    # 60000 * 2,
    # 150000
    lookup: dict[int, int] = {
        500: 500,
        1000: 1500,
        2000: 5500,
        2500: 16000,
        4000: 25000,
        7500: 36500,
        10000: 75000,
        15000: 130000,
        20000: 150000,
        30000: 220000,
        40000: 290000,
        60000: 350000,
        150000: 560000,
    }

    total = 0
    for item in [
        Items.BOLT_PACK_1,
        Items.BOLT_PACK_2,
        Items.BOLT_PACK_3,
        Items.BOLT_PACK_4,
        Items.BOLT_PACK_5,
        Items.BOLT_PACK_6,
        Items.BOLT_PACK_7,
        Items.BOLT_PACK_8,
        Items.BOLT_PACK_9,
        Items.BOLT_PACK_10,
        Items.BOLT_PACK_11,
        Items.BOLT_PACK_12,
        Items.BOLT_PACK_13,
        Items.BOLT_PACK_14,
        Items.BOLT_PACK_15,
        Items.BOLT_PACK_16,
        Items.BOLT_PACK_17,
        Items.BOLT_PACK_18,
        Items.BOLT_PACK_19,
        Items.BOLT_PACK_20,
        Items.BOLT_PACK_21,
        Items.BOLT_PACK_22,
        Items.BOLT_PACK_23,
        Items.BOLT_PACK_24,
        Items.BOLT_PACK_25,
        Items.BOLT_PACK_26
    ]:
        if state.prog_items[player].get(item.name) is not None:
            total += state.prog_items[player].get(item.name) * item.quantity * state.multiworld.worlds[
                player].options.pack_size_bolts.value
        for planet, bolts in {
            Items.NOVALIS_INFOBOT.name: 4800,
            Items.KERWAN_INFOBOT.name: 2250,
            Items.EUDORA_INFOBOT.name: 4500,
            Items.BLARG_INFOBOT.name: 2250,
            Items.RILGAR_INFOBOT.name: 325,
            Items.BATALIA_INFOBOT.name: 3000,
            Items.GASPAR_INFOBOT.name: 7850,
            Items.ORXON_INFOBOT.name: 4750,
            Items.POKITARU_INFOBOT.name: 2430,
            Items.HOVEN_INFOBOT.name: 2600,
            Items.OLTANIS_INFOBOT.name: 4150,
        }.items():
            total += state.has(planet, player) * bolts * state.multiworld.worlds[
                player].options.pack_size_bolts.value
    return total >= lookup[count]


def has_magneboots(state: CollectionState, player: int) -> bool:
    return state.has_any_count(Items.PROG[Items.MAGNEBOOTS.name], player)


def has_grindboots(state: CollectionState, player: int) -> bool:
    return state.has_any_count(Items.PROG[Items.GRINDBOOTS.name], player)


def has_hoverboard(state: CollectionState, player: int) -> bool:
    return state.has_any_count(Items.PROG[Items.HOVERBOARD.name], player)


def has_hologuise(state: CollectionState, player: int) -> bool:
    return state.has(Items.HOLOGUISE.name, player)


def has_pda(state: CollectionState, player: int) -> bool:
    return state.has(Items.PDA.name, player)


def has_zoomerator(state: CollectionState, player: int) -> bool:
    return state.has_any_count(Items.PROG[Items.ZOOMERATOR.name], player)


def has_raritanium(state: CollectionState, player: int) -> bool:
    return state.has_any_count(Items.PROG[Items.RARITANIUM.name], player)


def has_codebot(state: CollectionState, player: int) -> bool:
    return state.has(Items.CODEBOT.name, player)


def has_explosive_weapon(state: CollectionState, player: int) -> bool:
    return (state.has_any_count(Items.PROG[Items.BOMB_GLOVE.name], player)
            or state.has_any_count(Items.PROG[Items.MINE_GLOVE.name], player)
            or state.has_any_count(Items.PROG[Items.DEVASTATOR.name], player)
            or state.has_any([Items.VISIBOMB.name, Items.RYNO.name], player))


def has_long_range_weapon(state: CollectionState, player: int) -> bool:
    return (state.has_any_count(Items.PROG[Items.DEVASTATOR.name], player)
            or state.has(Items.VISIBOMB.name, player))


def has_medium_range_weapon(state: CollectionState, player: int) -> bool:
    return (state.has_any_count(Items.PROG[Items.BLASTER.name], player)
            or state.has_any_count(Items.PROG[Items.DEVASTATOR.name], player)
            or state.has_any([Items.VISIBOMB.name, Items.RYNO.name], player))


def has_short_range_weapon(state: CollectionState, player: int) -> bool:
    return (state.has_any_count(Items.PROG[Items.PYROCITOR.name], player)
            or state.has_any_count(Items.PROG[Items.BLASTER.name], player)
            or state.has_any_count(Items.PROG[Items.SUCK_CANNON.name], player)
            or state.has_any_count(Items.PROG[Items.DEVASTATOR.name], player)
            or state.has_any_count(Items.PROG[Items.TESLA_CLAW.name], player)
            or state.has_any([Items.VISIBOMB.name, Items.RYNO.name], player))


def has_40_gold_bolts(state: CollectionState, player: int) -> bool:
    lookup: dict[int, tuple[str, int]] = {
        1: (Items.GOLD_BOLT_1.name, 40),
        2: (Items.GOLD_BOLT_2.name, 20),
        3: (Items.GOLD_BOLT_3.name, 14),
        4: (Items.GOLD_BOLT_4.name, 10),
        5: (Items.GOLD_BOLT_5.name, 8),
        6: (Items.GOLD_BOLT_6.name, 7),
        7: (Items.GOLD_BOLT_7.name, 6),
        8: (Items.GOLD_BOLT_8.name, 5),
        9: (Items.GOLD_BOLT_9.name, 5),
        10: (Items.GOLD_BOLT_10.name, 4),
        11: (Items.GOLD_BOLT_11.name, 4),
        12: (Items.GOLD_BOLT_12.name, 4),
        13: (Items.GOLD_BOLT_13.name, 4),
        14: (Items.GOLD_BOLT_14.name, 3),
        15: (Items.GOLD_BOLT_15.name, 3),
        16: (Items.GOLD_BOLT_16.name, 3),
        17: (Items.GOLD_BOLT_17.name, 3),
        18: (Items.GOLD_BOLT_18.name, 3),
        19: (Items.GOLD_BOLT_19.name, 3),
        20: (Items.GOLD_BOLT_20.name, 2),
        21: (Items.GOLD_BOLT_21.name, 2),
        22: (Items.GOLD_BOLT_22.name, 2),
        23: (Items.GOLD_BOLT_23.name, 2),
        24: (Items.GOLD_BOLT_24.name, 2),
        25: (Items.GOLD_BOLT_25.name, 2),
        26: (Items.GOLD_BOLT_26.name, 2),
        27: (Items.GOLD_BOLT_27.name, 2),
        28: (Items.GOLD_BOLT_28.name, 2),
        29: (Items.GOLD_BOLT_29.name, 2),
        30: (Items.GOLD_BOLT_30.name, 2),
        31: (Items.GOLD_BOLT_31.name, 2),
        32: (Items.GOLD_BOLT_32.name, 2),
        33: (Items.GOLD_BOLT_33.name, 2),
        34: (Items.GOLD_BOLT_34.name, 2),
        35: (Items.GOLD_BOLT_35.name, 2),
        36: (Items.GOLD_BOLT_36.name, 2),
        37: (Items.GOLD_BOLT_37.name, 2),
        38: (Items.GOLD_BOLT_38.name, 2),
        39: (Items.GOLD_BOLT_39.name, 2),
        40: (Items.GOLD_BOLT_40.name, 1),
    }
    item, count = lookup[state.multiworld.worlds[player].options.pack_size_gold_bolts.value]
    if state.count(item, player) < count:
        rac_logger.debug(f"Missing gold bolt packs from world, expected {count} but only had "
                         f"{state.count(item, player)}. Can reach {state.prog_items}")
    return state.has(item, player, count)


# TODO: Trick/Glitch logic

# Novalis
def novalis_cave_gb_rule(state: CollectionState, player: int) -> bool:
    return has_explosive_weapon(state, player)  # Tricks


def novalis_underwater_caves_rule(state: CollectionState, player: int) -> bool:
    return has_hydro_pack(state, player)  # Tricks


def novalis_gold_weapon_10k(state: CollectionState, player: int) -> bool:
    return has_40_gold_bolts(state, player) and has_10k_bolts(state, player)


def novalis_gold_weapon_20k(state: CollectionState, player: int) -> bool:
    return has_40_gold_bolts(state, player) and has_20k_bolts(state, player)


def novalis_gold_weapon_30k(state: CollectionState, player: int) -> bool:
    return has_40_gold_bolts(state, player) and has_30k_bolts(state, player)


def novalis_gold_weapon_60k(state: CollectionState, player: int) -> bool:
    return has_40_gold_bolts(state, player) and has_60k_bolts(state, player)


# Aridia
def aridia_trespasser_rule(state: CollectionState, player: int) -> bool:
    return has_swingshot(state, player)  # Tricks


def aridia_laser_rule(state: CollectionState, player: int) -> bool:
    return has_magneboots(state, player)  # Tricks


def aridia_cave_rule(state: CollectionState, player: int) -> bool:
    return has_explosive_weapon(state, player)  # Tricks


# Kerwan
def kerwan_train_rule(state: CollectionState, player: int) -> bool:
    return can_improved_jump(state, player)  # Tricks


def kerwan_course_gb_rule(state: CollectionState, player: int) -> bool:
    return can_glide(state, player)  # Tricks


# Eudora
def eudora_suck_cannon_rule(state: CollectionState, player: int) -> bool:
    return can_glide(state, player)  # Tricks


def eudora_henchman_rule(state: CollectionState, player: int) -> bool:
    return (has_swingshot(state, player)
            and has_trespasser(state, player)
            and can_improved_jump(state, player))


def eudora_skillpoint_rule(state: CollectionState, player: int) -> bool:
    return has_short_range_weapon(state, player)


# Rilgar
def rilgar_hoverboard_rule(state: CollectionState, player: int) -> bool:
    return (has_hoverboard(state, player)
            and can_improved_jump(state, player))


def rilgar_bouncer_rule(state: CollectionState, player: int) -> bool:
    return (has_swingshot(state, player)
            and can_improved_jump(state, player)
            and has_hydrodisplacer(state, player))


def rilgar_underwater_bolt_rule(state: CollectionState, player: int) -> bool:
    return (rilgar_bouncer_rule(state, player)
            and has_o2_mask(state, player))


def rilgar_ryno_rule(state: CollectionState, player: int) -> bool:
    return can_improved_jump(state, player) and has_150k_bolts(state, player)


def rilgar_metal_spots(state: CollectionState, player: int) -> bool:
    return (state.has(Items.RILGAR_INFOBOT.name, player)
            and can_improved_jump(state, player))


# Blarg
def blarg_outside_gold_bolt_rule(state: CollectionState, player: int) -> bool:
    return (has_o2_mask(state, player)
            and has_trespasser(state, player))


def blarg_metal_spots(state: CollectionState, player: int) -> bool:
    return (state.has(Items.BLARG_INFOBOT.name, player)
            and (
                state.has(Items.SWINGSHOT.name, player)
                or blarg_outside_gold_bolt_rule(state, player)
            ))


# Umbris
def umbris_snagglebeast_rule(state: CollectionState, player: int) -> bool:
    return (has_swingshot(state, player)
            and can_glide(state, player)
            and has_hydrodisplacer(state, player))


def umbris_pressure_bolt_rule(state: CollectionState, player: int) -> bool:
    return (has_swingshot(state, player)
            and can_glide(state, player))


def umbris_jump_bolt_rule(state: CollectionState, player: int) -> bool:
    return (has_swingshot(state, player)
            and can_glide(state, player)
            and has_hydrodisplacer(state, player))


def umbris_metal_spots(state: CollectionState, player: int) -> bool:
    return (state.has(Items.UMBRIS_INFOBOT.name, player)
            and umbris_pressure_bolt_rule(state, player))


# Gaspar
def gaspar_skillpoint_rule(state: CollectionState, player: int) -> bool:
    return (has_visibomb(state, player)
            or (
                has_swingshot(state, player)
                and has_medium_range_weapon(state, player)
            ))


def gaspar_metal_spots(state: CollectionState, player: int) -> bool:
    return (state.has(Items.GASPAR_INFOBOT.name, player)
            and (
                has_swingshot(state, player)
                or can_improved_jump(state, player)
            ))


# Orxon
def orxon_nanotech_rule(state: CollectionState, player: int) -> bool:
    return (has_o2_mask(state, player)
            and can_glide(state, player))


def orxon_ultra_nanotech_rule(state: CollectionState, player: int) -> bool:
    return orxon_nanotech_rule(state, player) and has_30k_bolts(state, player)


def orxon_visibomb_rule(state: CollectionState, player: int) -> bool:
    return has_o2_mask(state, player) and has_15k_bolts(state, player)


def orxon_visibomb_bolt_rule(state: CollectionState, player: int) -> bool:
    return (orxon_ratchet_infobot_rule(state, player)
            and has_visibomb(state, player))


def orxon_ratchet_infobot_rule(state: CollectionState, player: int) -> bool:
    return (has_o2_mask(state, player)
            and can_glide(state, player)
            and has_swingshot(state, player)
            and has_magneboots(state, player))


def orxon_sniper_rule(state: CollectionState, player: int) -> bool:
    return (has_o2_mask(state, player)
            and can_glide(state, player)
            and (
                has_devastator(state, player)
                or has_blaster(state, player)
                or has_visibomb(state, player)
            ))


def orxon_hey_over_here_rule(state: CollectionState, player: int) -> bool:
    return (has_o2_mask(state, player)
            and can_glide(state, player)
            and has_magneboots(state, player)
            and has_taunter(state, player))


def orxon_metal_spots(state: CollectionState, player: int) -> bool:
    return (state.has(Items.ORXON_INFOBOT.name, player)
            and has_o2_mask(state, player))


# Pokitaru
def pokitaru_ship_rule(state: CollectionState, player: int) -> bool:
    return (has_pilots_helmet(state, player)
            and can_ground_pound(state, player))


def pokitaru_persuader_rule(state: CollectionState, player: int) -> bool:
    return (has_raritanium(state, player)
            and has_trespasser(state, player)
            and has_hydrodisplacer(state, player))


def pokitaru_gold_bolt_rule(state: CollectionState, player: int) -> bool:
    return (has_swingshot(state, player)
            and can_ground_pound(state, player))


# Hoven
def hoven_infobot_rule(state: CollectionState, player: int) -> bool:
    return (has_short_range_weapon(state, player)
            and can_improved_jump(state, player))


def hoven_raritanium_rule(state: CollectionState, player: int) -> bool:
    return (has_swingshot(state, player)
            and can_improved_jump(state, player))


# Gemlik
def gemlik_quark_rule(state: CollectionState, player: int) -> bool:
    return (has_magneboots(state, player)
            and can_improved_jump(state, player)
            and has_long_range_weapon(state, player)
            and has_trespasser(state, player)
            and has_swingshot(state, player))


def gemlik_bolt_rule(state: CollectionState, player: int) -> bool:
    return (has_visibomb(state, player)
            and can_improved_jump(state, player)
            and has_trespasser(state, player))


# def gemlik_gold_weapon_rule(state: CollectionState, player: int) -> bool:
#     return (gemlik_quark_rule(state, player)
#             and has_40_gold_bolts(state, player)
#             and has_bolts(state, player))


def gemlik_metal_spots(state: CollectionState, player: int) -> bool:
    return (state.has(Items.GEMLIK_INFOBOT.name, player)
            and gemlik_quark_rule(state, player))


# Oltanis
def oltanis_main_bolt_rule(state: CollectionState, player: int) -> bool:
    return (has_grindboots(state, player)
            and has_swingshot(state, player))


def oltanis_final_bolt_rule(state: CollectionState, player: int) -> bool:
    return (has_grindboots(state, player)
            and has_swingshot(state, player)
            and has_magneboots(state, player))


def oltanis_metal_spots(state: CollectionState, player: int) -> bool:
    return (state.has(Items.OLTANIS_INFOBOT.name, player)
            and (
                has_swingshot(state, player)
                or has_magneboots(state, player)
            ))


# Quartu
def quartu_infiltrate_rule(state: CollectionState, player: int) -> bool:
    return (has_hologuise(state, player)
            and has_swingshot(state, player)
            and can_ground_pound(state, player))


def quartu_codebot_rule(state: CollectionState, player: int) -> bool:
    return (has_codebot(state, player)
            and has_swingshot(state, player))


def quartu_bolt_grabber_rule(state: CollectionState, player: int) -> bool:
    return (has_hydro_pack(state, player)
            and has_o2_mask(state, player))


# Kalebo III
def kalebo_switch_rule(state: CollectionState, player: int) -> bool:
    return (state.has_any_count(Items.PROG[Items.BOMB_GLOVE.name], player)
            or state.has_any_count(Items.PROG[Items.BLASTER.name], player)
            or state.has_any_count(Items.PROG[Items.DEVASTATOR.name], player)
            or state.has_any_count(Items.PROG[Items.TESLA_CLAW.name], player)
            or state.has_any([Items.VISIBOMB.name, Items.RYNO.name], player))


def kalebo_hologuise_rule(state: CollectionState, player: int) -> bool:
    return (has_hoverboard(state, player)
            and has_swingshot(state, player)
            and has_grindboots(state, player)
            and kalebo_switch_rule(state, player))


def kalebo_metal_spots(state: CollectionState, player: int) -> bool:
    return (state.has(Items.KALEBO_INFOBOT.name, player)
            and kalebo_switch_rule(state, player)
            and (has_swingshot(state, player)
                 or can_improved_jump(state, player)))


# Drek's Fleet
def fleet_infobot_rule(state: CollectionState, player: int) -> bool:
    return (has_magneboots(state, player)
            and has_pilots_helmet(state, player)
            and has_hologuise(state, player)
            and has_swingshot(state, player))


def fleet_water_rule(state: CollectionState, player: int) -> bool:
    return (has_o2_mask(state, player)
            and has_hydro_pack(state, player))


def fleet_second_bolt_rule(state: CollectionState, player: int) -> bool:
    return (has_magneboots(state, player)
            and has_pilots_helmet(state, player)
            and has_hologuise(state, player)
            and has_swingshot(state, player))


def fleet_metal_spots(state: CollectionState, player: int) -> bool:
    return (state.has(Items.FLEET_INFOBOT.name, player)
            and (
                has_hologuise(state, player)
                or fleet_water_rule(state, player)
            ))


# Veldin
def veldin_global_rule(state: CollectionState, player: int) -> bool:
    return (has_trespasser(state, player)
            and has_magneboots(state, player)
            and has_hydrodisplacer(state, player)
            and can_ground_pound(state, player))


def veldin_grind_bolt_rule(state: CollectionState, player: int) -> bool:
    return (veldin_global_rule(state, player)
            and has_grindboots(state, player)
            and has_swingshot(state, player))


def veldin_halfway_bolt_rule(state: CollectionState, player: int) -> bool:
    return veldin_global_rule(state, player)


def veldin_taunter_bolt_rule(state: CollectionState, player: int) -> bool:
    return (veldin_global_rule(state, player)
            and has_taunter(state, player))


def veldin_metal_spots(state: CollectionState, player: int) -> bool:
    return (veldin_global_rule(state, player)
            and has_swingshot(state, player))


def veldin_defeat_drek_rule(state: CollectionState, player: int) -> bool:
    return (veldin_global_rule(state, player)
            and has_swingshot(state, player))
