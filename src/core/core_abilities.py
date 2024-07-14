from src.core.unit import WeaponTrait, Unit, PassiveAbility, WarscrollAbility, WeaponProfile

def add_one_to_hit_weapon(weapon_profile: WeaponProfile) -> None:
    weapon_profile.to_hit = weapon_profile.to_hit - 1

def neg_one_to_hit_weapon(weapon_profile: WeaponProfile) -> None:
    weapon_profile.to_hit = weapon_profile.to_hit + 1

def add_one_to_wound_weapon(weapon_profile: WeaponProfile) -> None:
    weapon_profile.to_wound = weapon_profile.to_wound - 1

def neg_one_to_wound_weapon(weapon_profile: WeaponProfile) -> None:
    weapon_profile.to_wound = weapon_profile.to_wound + 1

def check_range_criteria(weapon_profile: WeaponProfile, melee_only: bool, ranged_only: bool) -> bool:
    if weapon_profile.range == 0 and ranged_only:
        return False
    if weapon_profile.range > 0 and melee_only:
        return False
    return True

def add_one_to_hit(unit: Unit, melee_only = False, ranged_only = False) -> None:
    for weapon in unit.weapon_profiles:
        if weapon.has_trait(WeaponTrait.COMPANION):
            continue
        if not check_range_criteria(weapon, melee_only, ranged_only):
            continue
        add_one_to_hit_weapon(weapon)

def add_one_to_wound(unit: Unit, melee_only = False, ranged_only = False) -> None:
    for weapon in unit.weapon_profiles:
        if weapon.has_trait(WeaponTrait.COMPANION):
            continue
        if not check_range_criteria(weapon, melee_only, ranged_only):
            continue
        add_one_to_wound_weapon(weapon)



AllOutAttack = PassiveAbility(
    name="All-out attack"
)