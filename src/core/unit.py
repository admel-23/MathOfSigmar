from pydantic import BaseModel
from typing import Optional
from enum import Enum
from src.core.dice import Dice

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
    ANTI_CHARGE = 11,
    CHARGE_D_p1 = 9,
    SHOOT_IN_COMBAT = 10,

class WeaponProfile(BaseModel):
    attacks: int | Dice
    to_hit: int
    to_wound: int
    rend: int
    damage: int | Dice
    range: Optional[int] = None
    traits: [WeaponTrait] = []

    def has_trait(self, t: WeaponTrait):
        if t in self.traits:
            return True
        return False

class DefenseProfile(BaseModel):
    save: int
    ward: Optional[int] = None

class Unit(BaseModel):
    name: str
    models: int
    movement: int
    health: int
    defense_profile: DefenseProfile
    weapon_profiles: list[WeaponProfile]
    points: Optional[int] = None