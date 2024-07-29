from src.core.unit import Unit, DefenseProfile, WeaponProfile, WeaponTrait, SpearheadProperties
from src.core.dice import D3

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

SoulscryerS = Unit(
    name="Isharann Soulscryer",
    models=1,
    movement=6,
    health=5,
    defense_profile=DefenseProfile(save=5),
    weapon_profiles=[
        WeaponProfile(range=10, attacks=8, to_hit=5, to_wound=5, damage=1, traits=[WeaponTrait.COMPANION]),
        WeaponProfile(attacks=3, to_hit=3, to_wound=4, damage=D3)
    ],
    spearhead_properties=SpearheadProperties()
)

MorrsarrGuardS = Unit(
    name="Akhelian Morrsarr Guard",
    models=3,
    movement=14,
    health=4,
    defense_profile=DefenseProfile(save=4),
    weapon_profiles=[
        WeaponProfile(attacks=2, to_hit=3, to_wound=4, rend=1, damage=1),
        WeaponProfile(attacks=3, to_hit=4, to_wound=3, rend=1, damage=D3, traits=[WeaponTrait.COMPANION])
    ],
    spearhead_properties=SpearheadProperties()
)

AkhelianAllopexS = Unit(
    name="Akhelian Allopex",
    models=1,
    movement=12,
    health=8,
    defense_profile=DefenseProfile(save=4),
    weapon_profiles=[
        WeaponProfile(range=18, attacks=2, to_hit=3, to_wound=2, rend=1, damage=3),
        WeaponProfile(attacks=4, to_hit=3, to_wound=4, rend=1, damage=1),
        WeaponProfile(attacks=3, to_hit=4, to_wound=2, rend=2, damage=2, traits=[WeaponTrait.COMPANION])
    ],
    spearhead_properties=SpearheadProperties()
)

NamarthiThrallsS = Unit(
    name="Namarti Thralls",
    models=5,
    movement=6,
    health=1,
    defense_profile=DefenseProfile(save=5),
    weapon_profiles=[
        WeaponProfile(attacks=2, to_hit=3, to_wound=4, rend=1, damage=1),
    ],
    spearhead_properties=SpearheadProperties(reinforcements=True)
)

SoulraidHunt = [SoulscryerS, MorrsarrGuardS, AkhelianAllopexS, NamarthiThrallsS, NamarthiThrallsS]