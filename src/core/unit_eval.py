from src.core.dice import D6, Dice
from src.core.unit import DefenseProfile, WeaponProfile, Unit, WeaponTrait
from src.core.utils import percentile, get_value


SIMULATION_STEPS = 1000

def resolve_weapon_damage(weapon_profile: WeaponProfile, defense_profile: DefenseProfile) -> int:
    damage: int = 0
    attacks = get_value(weapon_profile.attacks)
    for i in range(0, attacks):
        hit_roll_result = D6.roll_check(weapon_profile.to_hit)
        if hit_roll_result.is_failed():
            continue
        auto_wound = False
        wound_rolls = 1
        if hit_roll_result.is_critical_success() and (len(weapon_profile.traits) > 0):
            if weapon_profile.has_trait(WeaponTrait.CRIT_MORTAL):
                damage += get_value(weapon_profile.damage)
                continue
            if weapon_profile.has_trait(WeaponTrait.CRIT_AUTO_WOUND):
                auto_wound = True
            if weapon_profile.has_trait(WeaponTrait.CRIT_2HIT):
                wound_rolls = 2
        for wound_roll in range(wound_rolls):
            wound_roll_result = D6.roll_check(weapon_profile.to_wound)
            if wound_roll_result.is_failed() and (not auto_wound):
                continue
            save_roll_result = D6.roll_check(
                defense_profile.save, roll_modifier=-weapon_profile.rend, critical_success_allowed=False)
            if save_roll_result.is_succeeded():
                continue
            damage += get_value(weapon_profile.damage)
    return damage

def resolve_unit_damage(unit: Unit, defense_profile: DefenseProfile) -> int:
    total_damage: int = 0
    for model in range(unit.models):
        for weapon_profile in unit.weapon_profiles:
            total_damage += resolve_weapon_damage(weapon_profile, defense_profile)
    return total_damage

def simulate_unit_damage(unit: Unit, defense_profile: DefenseProfile) -> [float, float, float]:
    damage_results: list[int] = []
    for step in range(0, SIMULATION_STEPS):
        damage_results.append(resolve_unit_damage(unit, defense_profile))
    damage_results.sort()
    return [percentile(damage_results, 10),
            percentile(damage_results, 50),
            percentile(damage_results, 90)]

def simulate_ward_damage_to_kill(health: int, ward: int) -> [float, float, float]:
    damage_results: list[int] = []
    for step in range(0, SIMULATION_STEPS):
        health_remaining = health
        damage_taken = 0
        while health_remaining > 0:
            damage_taken += 1
            if D6.roll_check(ward).is_failed():
                health_remaining -= 1
        damage_results.append(damage_taken)
    damage_results.sort()
    return [percentile(damage_results, 10),
            percentile(damage_results, 50),
            percentile(damage_results, 90)]


def calculate_attack_value(unit: Unit) -> (float, float, float):
    v5 = simulate_unit_damage(unit, DefenseProfile(save=5))
    v5 = [x * 7 for x in v5]
    v4 = simulate_unit_damage(unit, DefenseProfile(save=4))
    v4 = [x * 10 for x in v4]
    v3 = simulate_unit_damage(unit, DefenseProfile(save=3))
    v3 = [x * 14 for x in v3]
    v_total = []
    for i in range(len(v5)):
        v_total.append(int((v3[i]+v4[i]+v5[i])/3))
    return v_total

def calculate_defense_value(unit: Unit) -> (float, float, float):
    save_multiplier = 15
    if unit.defense_profile.save >= 5:
        save_multiplier = 7
    if unit.defense_profile.save == 4:
        save_multiplier = 10
    damage_capacity = [unit.models * unit.health, unit.models * unit.health, unit.models * unit.health]
    if unit.defense_profile.ward is not None:
        damage_capacity = simulate_ward_damage_to_kill(unit.models * unit.health, unit.defense_profile.ward)
    return [int(x * save_multiplier) for x in damage_capacity]