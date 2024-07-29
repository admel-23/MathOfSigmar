from abc import ABC, abstractmethod
from src.core.unit import Unit, WeaponProfile, DefenseProfile, WeaponTrait
from src.core.dice import D6
from src.core.utils import get_value

SIMULATION_STEPS = 1000


class UnitEvaluator(ABC):
    @abstractmethod
    def eval_unit(self, unit: Unit) -> float:
        pass


class AttackEvaluator(UnitEvaluator):
    @abstractmethod
    def weapon_matches(self, weapon_profile: WeaponProfile) -> bool:
        pass

    def eval_unit(self, unit: Unit) -> float:
        total_value: float = 0
        for weapon_profile in unit.weapon_profiles:
            if self.weapon_matches(weapon_profile):
                v6 = AttackEvaluator._simulate_weapon_damage(unit.models, weapon_profile, DefenseProfile(save=5)) * 5
                v5 = AttackEvaluator._simulate_weapon_damage(unit.models, weapon_profile, DefenseProfile(save=5)) * 7
                v4 = AttackEvaluator._simulate_weapon_damage(unit.models, weapon_profile, DefenseProfile(save=4)) * 10
                v3 = AttackEvaluator._simulate_weapon_damage(unit.models, weapon_profile, DefenseProfile(save=3)) * 15
                v2 = AttackEvaluator._simulate_weapon_damage(unit.models, weapon_profile, DefenseProfile(save=3)) * 24
                v_total = (v2 + v3 + v4 + v5 + v6) / 5
                total_value += v_total
        return total_value

    @staticmethod
    def _simulate_weapon_damage(models: int, weapon_profile: WeaponProfile, defense_profile: DefenseProfile) -> float:
        damage_results: list[int] = []
        for step in range(0, SIMULATION_STEPS):
            damage = 0
            for i in range(models):
                damage += AttackEvaluator._resolve_weapon_damage(weapon_profile, defense_profile)
            damage_results.append(damage)
        return sum(damage_results) / len(damage_results)

    @staticmethod
    def _resolve_weapon_damage(weapon_profile: WeaponProfile, defense_profile: DefenseProfile) -> int:
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




class MeleeEvaluator(AttackEvaluator):
    def weapon_matches(self, weapon_profile: WeaponProfile) -> bool:
        return weapon_profile.range == 0


class ShootingEvaluator(AttackEvaluator):
    def weapon_matches(self, weapon_profile: WeaponProfile) -> bool:
        return weapon_profile.range > 0


class DefenseEvaluator(UnitEvaluator):
    def eval_unit(self, unit: Unit) -> float:
        save_multipliers = {
            6: 5,
            5: 7,
            4: 10,
            3: 15,
            2: 24
        }
        save_multiplier = save_multipliers[unit.defense_profile.save]
        damage_capacity = unit.models * unit.health
        if unit.defense_profile.ward is not None:
            damage_capacity = DefenseEvaluator._simulate_ward_damage_to_kill(
                unit.models * unit.health, unit.defense_profile.ward)
        return int(damage_capacity * save_multiplier)

    @staticmethod
    def _simulate_ward_damage_to_kill(health: int, ward: int) -> float:
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
        return sum(damage_results) / len(damage_results)
