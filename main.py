from src.unit_profiles.idoneth_deepkin import SoulraidHunt
from src.unit_profiles.nurgle import BleakHost
from src.eval.spearhead_eval import SpearheadEvaluator


if __name__ == '__main__':
    spearhead_evaluator = SpearheadEvaluator()
    spearheads = [
        ["Soulraid Hunt (Idoneth Deepkin)", SoulraidHunt],
        ["Bleak Host (Nurgle)", BleakHost]
    ]
    for spearhead in spearheads:
        spearhead_name = spearhead[0]
        spearhead_list = spearhead[1]
        print("Spearhead: ", spearhead_name)
        spearhead_evaluator.evaluate_spearhead(spearhead=spearhead_list)