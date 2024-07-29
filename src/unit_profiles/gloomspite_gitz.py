from src.core.unit import Unit, DefenseProfile, WeaponProfile, WeaponTrait, SpearheadProperties
from src.core.dice import D3_p3, D3, D6, D6_p3, D6_p6, D6_p8, TwoD6

Kragnos = Unit(
    name="Kragons The End of Empires",
    models=1,
    movement=10,
    health=18,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=6, to_hit=3, to_wound=2, rend=3, damage=4),
        WeaponProfile(attacks=3, to_hit=4, to_wound=2, rend=2, damage=D3, traits=[WeaponTrait.CRIT_2HIT]),
        WeaponProfile(attacks=6, to_hit=3, to_wound=2, rend=1, damage=2)
    ],
    points=680
)

Skragrott = Unit(
    name="Skragrott The Loonking",
    models=1,
    movement=5,
    health=6,
    defense_profile=DefenseProfile(save=6, ward=4),
    weapon_profiles=[
        WeaponProfile(attacks=4, to_hit=3, to_wound=4, rend=1, damage=D3)
    ],
    points=220
)

Loonboss = Unit(
    name="Loonboss",
    models=1,
    movement=5,
    health=5,
    defense_profile=DefenseProfile(save=4, ward=6),
    weapon_profiles=[
        WeaponProfile(attacks=5, to_hit=4, to_wound=4, rend=1, damage=D3)
    ],
    points=130
)

Gobbapalooza = Unit(
    name="Gobbapalooza",
    models=5,
    movement=5,
    health=3,
    defense_profile=DefenseProfile(save=6, ward=6),
    weapon_profiles=[
        WeaponProfile(attacks=1, to_hit=4, to_wound=4, rend=1, damage=D3)
    ],
    points=150
)

RabbleRowza = Unit(
    name="Rabble-Rowza",
    models=1,
    movement=5,
    health=5,
    defense_profile=DefenseProfile(save=5),
    weapon_profiles=[
        WeaponProfile(range=12, attacks=3, to_hit=4, to_wound=4, rend=0, damage=D3,
                      traits=[WeaponTrait.CRIT_AUTO_WOUND]),
        WeaponProfile(attacks=5, to_hit=4, to_wound=4, rend=1, damage=D3)
    ],
    points=120

)

FungoidCaveShaman = Unit(
    name="Fungoid Cave Shaman",
    models=1,
    movement=5,
    health=5,
    defense_profile=DefenseProfile(save=6),
    weapon_profiles=[
        WeaponProfile(attacks=3, to_hit=4, to_wound=4, rend=1, damage=2),
        WeaponProfile(attacks=2, to_hit=4, to_wound=3, rend=1, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    points=100
)

SquigbossGnashaSquig = Unit(
    name="Squigboss with Gnasha Squig",
    models=1,
    movement=5,
    health=4,
    defense_profile=DefenseProfile(save=6),
    weapon_profiles=[
        WeaponProfile(attacks=5, to_hit=4, to_wound=4, rend=0, damage=2),
        WeaponProfile(attacks=2, to_hit=4, to_wound=3, rend=1, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    points=110
)

LoonbossOnManglerSquig = Unit(
    name="Loonboss On Mangler Squig",
    models=1,
    movement=D6_p8,
    health=14,
    defense_profile=DefenseProfile(save=5),
    weapon_profiles=[
        WeaponProfile(attacks=5, to_hit=4, to_wound=4, rend=1, damage=2),
        WeaponProfile(attacks=4, to_hit=4, to_wound=2, rend=1, damage=D6, traits=[WeaponTrait.COMPANION]),
        WeaponProfile(attacks=4, to_hit=4, to_wound=4, rend=0, damage=D3, traits=[WeaponTrait.COMPANION])
    ],
    points=260
)

ManglerSquigs = Unit(
    name="Mangler Squigs",
    models=1,
    movement=D6_p8,
    health=14,
    defense_profile=DefenseProfile(save=5),
    weapon_profiles=[
        WeaponProfile(attacks=4, to_hit=4, to_wound=5, rend=0, damage=1),
        WeaponProfile(attacks=4, to_hit=4, to_wound=2, rend=1, damage=D6, traits=[WeaponTrait.COMPANION]),
        WeaponProfile(attacks=4, to_hit=4, to_wound=4, rend=0, damage=D3, traits=[WeaponTrait.COMPANION])
    ],
    points=220
)

SneakySnufflers = Unit(
    name="Sneaky Snufflers",
    models=6,
    movement=5,
    health=2,
    defense_profile=DefenseProfile(save=6, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=3, to_hit=4, to_wound=4, rend=0, damage=1),
        WeaponProfile(attacks=2, to_hit=4, to_wound=4, rend=0, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    points=140
)

SnarlfangRiders = Unit(
    name="Snarlfang Riders",
    models=5,
    movement=12,
    health=2,
    defense_profile=DefenseProfile(save=5),
    weapon_profiles=[
        WeaponProfile(range=15, attacks=2, to_hit=4, to_wound=5, rend=0, damage=1),
        WeaponProfile(attacks=2, to_hit=4, to_wound=5, rend=0, damage=1),
        WeaponProfile(attacks=2, to_hit=4, to_wound=3, rend=0, damage=2, traits=[WeaponTrait.COMPANION])
    ],
    points=130
)

LoonsmashaFanatics = Unit(
    name="Loonsmasha Fanatics",
    models=5,
    movement=TwoD6,
    health=1,
    defense_profile=DefenseProfile(save=6),
    weapon_profiles=[
        WeaponProfile(attacks=D6, to_hit=4, to_wound=3, rend=2, damage=D3),
    ],
    points=140
)

SporesplattaFanatics = Unit(
    name="Sporesplatta Fanatics",
    models=5,
    movement=TwoD6,
    health=1,
    defense_profile=DefenseProfile(save=6),
    weapon_profiles=[
        WeaponProfile(attacks=D3, to_hit=3, to_wound=4, rend=1, damage=D3),
    ],
    points=120
)

MoonclanShootas = Unit(
    name="Moonclan Shootas",
    models=20,
    movement=5,
    health=1,
    defense_profile=DefenseProfile(save=6),
    weapon_profiles=[
        WeaponProfile(range=18, attacks=2, to_hit=4, to_wound=5, rend=0, damage=1),
        WeaponProfile(attacks=1, to_hit=4, to_wound=5, rend=0, damage=1)
    ],
    points=160
)

MoonclanStabbas = Unit(
    name="Moonclan Stabbas",
    models=20,
    movement=5,
    health=1,
    defense_profile=DefenseProfile(save=5),
    weapon_profiles=[
        WeaponProfile(attacks=2, to_hit=4, to_wound=5, rend=0, damage=1)
    ],
    points=140
)

SquigHerd = Unit(
    name="Squig Herd",
    models=12,
    movement=D6_p3,
    health=1,
    defense_profile=DefenseProfile(save=6),
    weapon_profiles=[
        WeaponProfile(attacks=3, to_hit=4, to_wound=3, rend=1, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    points=140
)

LoonbossOnGiantCaveSquig = Unit(
    name="Loonboss on Giant Cave Squig",
    models=1,
    movement=D6_p6,
    health=6,
    defense_profile=DefenseProfile(save=5),
    weapon_profiles=[
        WeaponProfile(attacks=5, to_hit=4, to_wound=4, rend=1, damage=2),
        WeaponProfile(attacks=4, to_hit=4, to_wound=3, rend=2, damage=D3, traits=[WeaponTrait.COMPANION])
    ],
    points=130
)

SquigHoppers = Unit(
    name="Squig Hoppers",
    models=10,
    movement=D6_p8,
    health=2,
    defense_profile=DefenseProfile(save=6),
    weapon_profiles=[
        WeaponProfile(attacks=2, to_hit=4, to_wound=5, rend=0, damage=1),
        WeaponProfile(attacks=3, to_hit=4, to_wound=3, rend=1, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    points=170
)

BoingrotBounderz = Unit(
    name="Boingrot Bounderz",
    models=5,
    movement=D6_p6,
    health=2,
    defense_profile=DefenseProfile(save=5),
    weapon_profiles=[
        WeaponProfile(attacks=3, to_hit=4, to_wound=4, rend=1, damage=1),
        WeaponProfile(attacks=3, to_hit=4, to_wound=3, rend=1, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    points=120
)

Trugg = Unit(
    name="Trugg The Troggoth King",
    models=1,
    movement=6,
    health=16,
    defense_profile=DefenseProfile(save=4),
    weapon_profiles=[
        WeaponProfile(attacks=4, to_hit=3, to_wound=2, rend=2, damage=4),
        WeaponProfile(attacks=2, to_hit=4, to_wound=2, rend=2, damage=D3_p3)
    ],
    points=360
)

DankholdTroggboss = Unit(
    name="Dankhold Troggboss",
    models=1,
    movement=6,
    health=12,
    defense_profile=DefenseProfile(save=4),
    weapon_profiles=[
        WeaponProfile(attacks=5, to_hit=4, to_wound=2, rend=2, damage=D6)
    ],
    points=220
)

DankholdTroggoth = Unit(
    name="Dankhold Troggoth",
    models=1,
    movement=6,
    health=10,
    defense_profile=DefenseProfile(save=4),
    weapon_profiles=[
        WeaponProfile(attacks=4, to_hit=4, to_wound=2, rend=2, damage=D3_p3)
    ],
    points=180
)

FellwaterTroggoths = Unit(
    name="Fellwater Troggoths",
    models=3,
    movement=6,
    health=5,
    defense_profile=DefenseProfile(save=5),
    weapon_profiles=[
        WeaponProfile(range=6, attacks=D3, to_hit=2, to_wound=3, rend=2, damage=1),
        WeaponProfile(attacks=4, to_hit=4, to_wound=3, rend=1, damage=2)
    ],
    points=180
)

RockgutTroggoths = Unit(
    name="Rockgut Troggoths",
    models=3,
    movement=6,
    health=5,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(range=10, attacks=1, to_hit=5, to_wound=2, rend=2, damage=D3),
        WeaponProfile(attacks=2, to_hit=4, to_wound=2, rend=2, damage=3)
    ],
    points=170
)

GloomspiteGitzUnits = [Kragnos, Skragrott, Loonboss, Gobbapalooza, RabbleRowza, FungoidCaveShaman,
                       SquigbossGnashaSquig, LoonbossOnManglerSquig, ManglerSquigs, SneakySnufflers,
                       SnarlfangRiders, LoonsmashaFanatics, SporesplattaFanatics, MoonclanShootas,
                       MoonclanStabbas, SquigHerd, LoonbossOnGiantCaveSquig, SquigHoppers, BoingrotBounderz,
                       Trugg, DankholdTroggboss, DankholdTroggoth, FellwaterTroggoths, RockgutTroggoths]

LoonbossS = Unit(
    name="Loonboss",
    models=1,
    movement=5,
    health=5,
    defense_profile=DefenseProfile(save=4, ward=6),
    weapon_profiles=[
        WeaponProfile(attacks=5, to_hit=4, to_wound=4, rend=1, damage=D3)
    ],
    spearhead_properties=SpearheadProperties()
)

SquigHoppersS = Unit(
    name="Squig Hoppers",
    models=5,
    movement=D6_p8,
    health=2,
    defense_profile=DefenseProfile(save=6),
    weapon_profiles=[
        WeaponProfile(attacks=2, to_hit=4, to_wound=5, damage=1),
        WeaponProfile(attacks=3, to_hit=4, to_wound=3, rend=1, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    spearhead_properties=SpearheadProperties()
)

RockgutTroggothsS = Unit(
    name="Rockgut Troggoths",
    models=3,
    movement=6,
    health=5,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(range=10, attacks=1, to_hit=5, to_wound=2, rend=2, damage=D3),
        WeaponProfile(attacks=2, to_hit=4, to_wound=2, rend=2, damage=3)
    ],
    spearhead_properties=SpearheadProperties()
)


MoonclanStabbasS = Unit(
    name="Moonclan Stabbas",
    models=10,
    movement=5,
    health=1,
    defense_profile=DefenseProfile(save=5),
    weapon_profiles=[
        WeaponProfile(attacks=2, to_hit=4, to_wound=5, rend=0, damage=1)
    ],
    spearhead_properties=SpearheadProperties(reinforcements=True)
)

BadMoonMadmob = [LoonbossS, MoonclanStabbasS, MoonclanStabbasS, SquigHoppersS, SquigHoppersS, RockgutTroggothsS]