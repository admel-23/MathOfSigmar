from pydantic import BaseModel
from typing import Optional
from enum import Enum
from src.core.dice import Dice
from abc import ABC, abstractmethod

class NumberCharacteristic(BaseModel):
    characteristic: str

    def get_value(self) -> int:
        return int(self.characteristic)

class WeaponTrait(Enum):
    CRIT_2HIT = 1,
    CRIT_AUTO_WOUND = 2,
    CRIT_MORTAL = 3,
    COMPANION = 4,
    ANTI_CAVALRY = 5,
    ANTI_INFANTRY = 6,
    ANTI_MONSTER = 7,
    ANTI_HERO = 8,
    ANTI_CHARGE = 9,
    CHARGE_D_p1 = 10,
    SHOOT_IN_COMBAT = 11


class WeaponProfile(BaseModel):
    attacks: int | Dice
    to_hit: int
    to_wound: int
    rend: int
    damage: int | Dice
    range: Optional[int] = 0
    traits: list[WeaponTrait] = []

    def has_trait(self, t: WeaponTrait):
        if t in self.traits:
            return True
        return False


class DefenseProfile(BaseModel):
    save: int
    ward: Optional[int] = None

class SpearheadProperties(BaseModel):
    reinforcements = False,
    arrives_3rd_round = False

class Unit(BaseModel):
    name: str
    models: int
    movement: int | Dice
    health: int
    defense_profile: DefenseProfile
    weapon_profiles: list[WeaponProfile]
    points: Optional[int] = None
    spearhead_properties: Optional[SpearheadProperties] = None

class PassiveAbility(BaseModel, ABC):
    name: str

    @abstractmethod
    def apply_to_unit(self, unit: Unit) -> Unit:
        pass

class WarscrollAbility(PassiveAbility, ABC):
    originating_unit_name: str

# class Modifier