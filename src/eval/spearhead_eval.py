from src.core.unit import Unit
from src.eval.eval import DefenseEvaluator, MeleeEvaluator, ShootingEvaluator

class SpearheadEvaluator:
    def evaluate_spearhead(self, spearhead: list[Unit]) -> None:
        defense_evaluator = DefenseEvaluator()
        defense_value = 0
        for unit in spearhead:
            defense_value += defense_evaluator.eval_unit(unit)
            if unit.spearhead_properties.reinforcements:
                defense_value += defense_evaluator.eval_unit(unit)
        print("Defense value: ", defense_value)

        melee_evaluator = MeleeEvaluator()
        melee_value = 0
        for unit in spearhead:
            melee_value += melee_evaluator.eval_unit(unit)
        print("Melee value: ", int(melee_value))

        shooting_evaluator = ShootingEvaluator()
        shooting_value = 0
        for unit in spearhead:
            shooting_value += shooting_evaluator.eval_unit(unit)
        print("Shooting value: ", int(shooting_value))
