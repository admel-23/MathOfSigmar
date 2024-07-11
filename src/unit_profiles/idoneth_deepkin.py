from src.core.unit import Unit, DefenseProfile, WeaponProfile

NamarthiThralls = Unit(
    name="Namarthi Thralls",
    models=10,
    movement=6,
    health=1,
    defense_profile=DefenseProfile(save=5),
    weapon_profiles=[
        WeaponProfile(attacks=1, to_hit=3, to_wound=4, rend=1, damage=1)
    ]
)

EidolonAspectOfTheStorm = Unit(
    name="Eidolon of Mathlann: Aspect of the Storm",
    models=1,
    movement=10,
    health=12,
    defense_profile=DefenseProfile(save=3, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=6, to_hit=3, to_wound=2, rend=2, damage=2),
        WeaponProfile(attacks=6, to_hit=4, to_wound=4, rend=0, damage=1)
    ]
)

Leviadon = Unit(
    name="Akhilian Leviadon",
    models=1,
    movement=10,
    health=16,
    defense_profile=DefenseProfile(save=3, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=4, to_hit=3, to_wound=2, rend=1, damage=3, range=18),
        WeaponProfile(attacks=7, to_hit=4, to_wound=2, rend=2, damage=3),
        WeaponProfile(attacks=4, to_hit=3, to_wound=4, rend=1, damage=1)
    ]
)

IdonethDeepkinUnits = [NamarthiThralls, EidolonAspectOfTheStorm, Leviadon]