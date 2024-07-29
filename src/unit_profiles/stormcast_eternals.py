from src.core.unit import Unit, DefenseProfile, WeaponProfile, WeaponTrait, SpearheadProperties
from src.core.dice import D3

LordVigilantS = Unit(
    name="Lord-Vigilant on Gryph-Stalker",
    models=1,
    movement=12,
    health=8,
    defense_profile=DefenseProfile(save=3),
    weapon_profiles=[
        WeaponProfile(attacks=5, to_hit=3, to_wound=3, rend=2, damage=2),
        WeaponProfile(attacks=3, to_hit=4, to_wound=3, rend=1, damage=2, traits=[WeaponTrait.COMPANION]),
    ],
    spearhead_properties=SpearheadProperties()
)

LordVeritantS = Unit(
    name="Lord-Veritant",
    models=1,
    movement=5,
    health=6,
    defense_profile=DefenseProfile(save=3),
    weapon_profiles=[
        WeaponProfile(attacks=1, to_hit=3, to_wound=3, rend=1, damage=3),
        WeaponProfile(attacks=3, to_hit=3, to_wound=3, rend=1, damage=D3)
    ],
    spearhead_properties=SpearheadProperties()
)

ProsecutorsS = Unit(
    name="Prosecutors",
    models=3,
    movement=12,
    health=2,
    defense_profile=DefenseProfile(save=3),
    weapon_profiles=[
        WeaponProfile(range=10, attacks=1, to_hit=3, to_wound=3, rend=1, damage=D3),
        WeaponProfile(attacks=3, to_hit=3, to_wound=3, rend=1, damage=1)
    ],
    spearhead_properties=SpearheadProperties(reinforcements=True)
)

LiberatorsS = Unit(
    name="Liberators",
    models=5,
    movement=5,
    health=2,
    defense_profile=DefenseProfile(save=3),
    weapon_profiles=[
        WeaponProfile(attacks=2, to_hit=3, to_wound=3, rend=1, damage=1, traits=[WeaponTrait.CRIT_MORTAL])
    ],
    spearhead_properties=SpearheadProperties(reinforcements=True)
)

VigilantBrotherhood = [LordVigilantS, LordVeritantS, ProsecutorsS, LiberatorsS]