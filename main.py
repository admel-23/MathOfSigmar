from src.core.unit_eval import calculate_attack_value, calculate_defense_value
from src.unit_profiles.idoneth_deepkin import IdonethDeepkinUnits
from src.unit_profiles.nurgle import NurgleUnits
from src.core.unit import DefenseProfile


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    units = NurgleUnits
    for unit in units:
        print("Unit: ", unit.name, "(", unit.points, ")")
        attack_value = calculate_attack_value(unit)
        print("  Attack (pts): ", attack_value[0], " - ", attack_value[2])
        defense_value = calculate_defense_value(unit)
        print("  Defense (pts): ", defense_value[0], " - ", defense_value[2])