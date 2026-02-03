import typing

from BaseClasses import CollectionState, Location, Region
from .data import Planets
from .data.Items import get_gold_bolts
from .data.Locations import LocationData, POOL_GOLDEN_WEAPON
from .data.Planets import PlanetData
from ..generic.Rules import forbid_item

if typing.TYPE_CHECKING:
    from . import RacWorld


class RacLocation(Location):
    game: str = "Ratchet & Clank"


def create_regions(world: 'RacWorld'):
    # create all regions and populate with locations
    menu = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(menu)

    for planet_data in Planets.LOGIC_PLANETS:
        if planet_data.locations:
            def generate_planet_access_rule(planet: PlanetData) -> typing.Callable[[CollectionState], bool]:
                def planet_access_rule(state: CollectionState):
                    return state.has(planet.name, world.player)

                return planet_access_rule

            def general_access(planet: PlanetData, index: int) -> typing.Callable[[CollectionState], bool]:
                def access(state: CollectionState) -> bool:
                    if state.prog_items[1].get("Hoverboard"):
                        pass
                    return planet.locations[index].access_rule(state, world.player)

                return access

            region = Region(planet_data.name, world.player, world.multiworld)
            world.multiworld.regions.append(region)
            if region.name != "General":
                menu.connect(region, f'Menu -> {region.name}', generate_planet_access_rule(planet_data))
            if planet_data.name == "Rilgar":
                region.connect(world.get_region("General"), "Rilgar Hoverboard Race", general_access(planet_data, 1))
            if planet_data.name == "Kalebo III":
                region.connect(world.get_region("General"), "Kalebo Hoverboard Race", general_access(planet_data, 0))

            for location_data in planet_data.locations:
                def generate_access_rule(loc: LocationData) -> typing.Callable[[CollectionState], bool]:
                    def access_rule(state: CollectionState):
                        if loc.access_rule:
                            return loc.access_rule(state, world.player)
                        return True

                    return access_rule

                region.add_locations({location_data.name: location_data.location_id}, RacLocation)
                location = world.multiworld.get_location(location_data.name, world.player)
                location.access_rule = generate_access_rule(location_data)
                if POOL_GOLDEN_WEAPON in location_data.pools:
                    forbid_item(location, get_gold_bolts(world.options), world.player)

    # from Utils import visualize_regions
    # visualize_regions(world.multiworld.get_region("Menu", world.player), "my_world.puml")
