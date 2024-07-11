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
    CRIT_MORTAL = 3

class WeaponProfile(BaseModel):
    attacks: int | Dice
    to_hit: int
    to_wound: int
    rend: int
    damage: int | Dice
    range: Optional[int] = None
    trait: Optional[WeaponTrait] = None

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