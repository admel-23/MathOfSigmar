from src.core.unit import Unit, DefenseProfile, WeaponProfile, WeaponTrait, SpearheadProperties
from src.core.dice import D3_p3, D3, D6

Rotigus = Unit(
    name="Rotigus",
    models=1,
    movement=6,
    health=22,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=5, to_hit=3, to_wound=2, rend=1, damage=3),
        WeaponProfile(attacks=2, to_hit=3, to_wound=2, rend=2, damage=2),
        WeaponProfile(attacks=10, to_hit=5, to_wound=5, rend=0, damage=1, traits=[WeaponTrait.CRIT_AUTO_WOUND, WeaponTrait.COMPANION])
    ],
    points=500
)

GreatUncleanOne = Unit(
    name="Great Unclean One",
    models=1,
    movement=6,
    health=20,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(range=7, attacks=D3_p3, to_hit=3, to_wound=2, rend=2, damage=2, traits=[WeaponTrait.SHOOT_IN_COMBAT]),
        WeaponProfile(attacks=4, to_hit=3, to_wound=2, rend=2, damage=4),
        WeaponProfile(attacks=10, to_hit=5, to_wound=5, rend=0, damage=1, traits=[WeaponTrait.CRIT_AUTO_WOUND, WeaponTrait.COMPANION])
    ],
    points=480
)

Poxbringer = Unit(
    name="Poxbringer",
    models=1,
    movement=4,
    health=5,
    defense_profile=DefenseProfile(save=5, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=3, to_hit=4, to_wound=3, rend=1, damage=2, traits=[WeaponTrait.CRIT_MORTAL])
    ],
    points=130
)

HorticulousSlimux = Unit(
    name="Horticulous Slimux",
    models=1,
    movement=4,
    health=8,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=3, to_hit=3, to_wound=3, rend=1, damage=2),
        WeaponProfile(attacks=4, to_hit=4, to_wound=3, rend=1, damage=D3, traits=[WeaponTrait.COMPANION])
    ],
    points=150
)

SpoilpoxScrivener = Unit(
    name="Spoilpox Scrivener",
    models=1,
    movement=4,
    health=5,
    defense_profile=DefenseProfile(save=5, ward=5),
    weapon_profiles=[
        WeaponProfile(range=7, attacks=D6, to_hit=2, to_wound=4, rend=0, damage=1, traits=[WeaponTrait.COMPANION]),
        WeaponProfile(attacks=3, to_hit=4, to_wound=3, rend=1, damage=2)
    ],
    points=100
)

SloppityBilepiper = Unit(
    name="Sloppity Bilepiper",
    models=1,
    movement=4,
    health=5,
    defense_profile=DefenseProfile(save=5, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=3, to_hit=4, to_wound=3, rend=1, damage=2)
    ],
    points=110
)

Nurglings = Unit(
    name="Nurglings",
    models=3,
    movement=4,
    health=4,
    defense_profile=DefenseProfile(save=6, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=5, to_hit=5, to_wound=5, rend=0, damage=1, traits=[WeaponTrait.CRIT_AUTO_WOUND])
    ],
    points=110
)

BeastOfNurgle = Unit(
    name="Beast Of Nurgle",
    models=1,
    movement=7,
    health=8,
    defense_profile=DefenseProfile(save=5, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=5, to_hit=4, to_wound=3, rend=1, damage=D3, traits=[WeaponTrait.COMPANION])
    ],
    points=150
)

PlagueDrones = Unit(
    name="Plague Drones",
    models=3,
    movement=8,
    health=5,
    defense_profile=DefenseProfile(save=5, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=2, to_hit=4, to_wound=3, rend=0, damage=1, traits=[WeaponTrait.CRIT_MORTAL]),
        WeaponProfile(attacks=6, to_hit=4, to_wound=3, rend=0, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    points=180
)

Plaguebearers = Unit(
    name="Plaguebearers",
    models=10,
    movement=4,
    health=2,
    defense_profile=DefenseProfile(save=6, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=1, to_hit=4, to_wound=3, rend=0, damage=1, traits=[WeaponTrait.CRIT_MORTAL])
    ],
    points=140
)

Glottkin = Unit(
    name="The Glottkin",
    models=1,
    movement=6,
    health=24,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=4, to_hit=3, to_wound=2, rend=2, damage=D3_p3),
        WeaponProfile(attacks=3, to_hit=3, to_wound=2, rend=2, damage=3),
        WeaponProfile(attacks=4, to_hit=3, to_wound=3, rend=1, damage=2)
    ],
    points=550
)

MorbidexTwiceborn = Unit(
    name="Morbidex Twiceborn",
    models=1,
    movement=8,
    health=14,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(range=7, attacks=3, to_hit=3, to_wound=3, rend=1, damage=1, traits=[WeaponTrait.COMPANION, WeaponTrait.SHOOT_IN_COMBAT]),
        WeaponProfile(attacks=5, to_hit=3, to_wound=3, rend=1, damage=2),
        WeaponProfile(attacks=5, to_hit=4, to_wound=2, rend=2, damage=3, traits=[WeaponTrait.COMPANION])
    ],
    points=320
)

BloabRotspawned = Unit(
    name="Bloab Rotspawned",
    models=1,
    movement=8,
    health=14,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(range=7, attacks=7, to_hit=2, to_wound=4, rend=1, damage=D3, traits=[WeaponTrait.COMPANION, WeaponTrait.SHOOT_IN_COMBAT]),
        WeaponProfile(attacks=3, to_hit=3, to_wound=3, rend=1, damage=2),
        WeaponProfile(attacks=5, to_hit=4, to_wound=2, rend=2, damage=3, traits=[WeaponTrait.COMPANION])
    ],
    points=320
)

GutrotSpume = Unit(
    name="Gutrot Spume",
    models=1,
    movement=4,
    health=7,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=5, to_hit=3, to_wound=2, rend=1, damage=2, traits=[WeaponTrait.CRIT_MORTAL, WeaponTrait.ANTI_HERO])
    ],
    points=180
)

LordOfAfflictions = Unit(
    name="Lord Of Afflictions",
    models=1,
    movement=8,
    health=8,
    defense_profile=DefenseProfile(save=3, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=4, to_hit=3, to_wound=3, rend=1, damage=2, traits=[WeaponTrait.CHARGE_D_p1]),
        WeaponProfile(attacks=6, to_hit=4, to_wound=3, rend=0, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    points=220
)

OrghottsDeamonspew = Unit(
    name="Orghotts Deamonspew",
    models=1,
    movement=8,
    health=14,
    defense_profile=DefenseProfile(save=3, ward=5),
    weapon_profiles=[
        WeaponProfile(range=7, attacks=1, to_hit=3, to_wound=3, rend=0, damage=D6, traits=[WeaponTrait.COMPANION, WeaponTrait.SHOOT_IN_COMBAT]),
        WeaponProfile(attacks=7, to_hit=3, to_wound=3, rend=1, damage=2),
        WeaponProfile(attacks=5, to_hit=4, to_wound=2, rend=2, damage=3, traits=[WeaponTrait.COMPANION])
    ],
    points=340
)

LordOfBlights = Unit(
    name="Lord Of Blights",
    models=1,
    movement=4,
    health=7,
    defense_profile=DefenseProfile(save=3, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=4, to_hit=3, to_wound=3, rend=1, damage=3, traits=[WeaponTrait.ANTI_CHARGE])
    ],
    points=170
)

HarbingerOfDecay = Unit(
    name="Harbinger Of Decay",
    models=1,
    movement=8,
    health=7,
    defense_profile=DefenseProfile(save=3, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=3, to_hit=3, to_wound=3, rend=1, damage=3, traits=[WeaponTrait.CRIT_MORTAL]),
        WeaponProfile(attacks=2, to_hit=5, to_wound=3, rend=0, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    points=200
)

RotbringerSorcerer = Unit(
    name="Rotbringer Sorcerer",
    models=1,
    movement=4,
    health=6,
    defense_profile=DefenseProfile(save=5, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=3, to_hit=4, to_wound=3, rend=1, damage=D3)
    ],
    points=120
)

LordOfPlagues = Unit(
    name="Lord Of Plagues",
    models=1,
    movement=4,
    health=7,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=5, to_hit=3, to_wound=3, rend=1, damage=2, traits=[WeaponTrait.CRIT_MORTAL])
    ],
    points=170
)

PussgoyleBlightlords = Unit(
    name="Pussgoyle Blightlords",
    models=2,
    movement=8,
    health=8,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=4, to_hit=3, to_wound=3, rend=1, damage=1, traits=[WeaponTrait.CHARGE_D_p1]),
        WeaponProfile(attacks=6, to_hit=4, to_wound=3, rend=0, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    points=250
)

PutridBlightkings = Unit(
    name="Putrid Blightkings",
    models=5,
    movement=4,
    health=3,
    defense_profile=DefenseProfile(save=3, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=4, to_hit=3, to_wound=3, rend=1, damage=1)
    ],
    points=200
)

RotmireCreed = Unit(
    name="RotmireCreed",
    models=10,
    movement=5,
    health=1,
    defense_profile=DefenseProfile(save=6, ward=5),
    weapon_profiles=[
        WeaponProfile(range=12, attacks=2, to_hit=4, to_wound=3, rend=0, damage=1, traits=[WeaponTrait.CRIT_AUTO_WOUND]),
        WeaponProfile(attacks=2, to_hit=4, to_wound=4, rend=0, damage=1)
    ],
    points=130
)

ChaosChosen = Unit(
    name="Chaos Chosen",
    models=5,
    movement=5,
    health=3,
    defense_profile=DefenseProfile(save=3),
    weapon_profiles=[
        WeaponProfile(attacks=3, to_hit=3, to_wound=3, rend=1, damage=2, traits=[WeaponTrait.CRIT_MORTAL]),
    ],
    points=250
)

NurgleUnits = [Rotigus, GreatUncleanOne, Poxbringer, HorticulousSlimux, SpoilpoxScrivener,
               SloppityBilepiper, Nurglings, BeastOfNurgle, PlagueDrones, Plaguebearers,
               Glottkin, MorbidexTwiceborn, BloabRotspawned, GutrotSpume, LordOfAfflictions,
               OrghottsDeamonspew, LordOfBlights, HarbingerOfDecay, RotbringerSorcerer,
               LordOfPlagues, PussgoyleBlightlords, PutridBlightkings, RotmireCreed, ChaosChosen]

SpoilpoxScrivenerS = Unit(
    name="Spoilpox Scrivener",
    models=1,
    movement=4,
    health=5,
    defense_profile=DefenseProfile(save=5, ward=5),
    weapon_profiles=[
        WeaponProfile(range=7, attacks=D6, to_hit=2, to_wound=4, damage=1),
        WeaponProfile(attacks=3, to_hit=4, to_wound=3, rend=1, damage=2)
    ],
    spearhead_properties=SpearheadProperties()
)

PussgoyleBlightlordsS = Unit(
    name="Pussgoyle Blightlords",
    models=1,
    movement=8,
    health=8,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=3, to_hit=3, to_wound=3, rend=2, damage=1),
        WeaponProfile(attacks=6, to_hit=4, to_wound=3, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    spearhead_properties=SpearheadProperties()
)

PussgoyleBlightlordsS3 = Unit(
    name="Pussgoyle Blightlords",
    models=1,
    movement=8,
    health=8,
    defense_profile=DefenseProfile(save=4, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=3, to_hit=3, to_wound=3, rend=2, damage=1),
        WeaponProfile(attacks=6, to_hit=4, to_wound=3, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    spearhead_properties=SpearheadProperties(arrives_3rd_round=True)
)

PutridBlightkingsS = Unit(
    name="Putrid Blightkings",
    models=5,
    movement=4,
    health=3,
    defense_profile=DefenseProfile(save=3, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=4, to_hit=3, to_wound=3, rend=1, damage=1)
    ],
    spearhead_properties=SpearheadProperties()
)

PlaguebearersS = Unit(
    name="Plaguebearers",
    models=5,
    movement=4,
    health=2,
    defense_profile=DefenseProfile(save=6, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=1, to_hit=4, to_wound=3, damage=1, traits=[WeaponTrait.CRIT_MORTAL])
    ],
    spearhead_properties=SpearheadProperties()
)

PlaguebearersS3 = Unit(
    name="Plaguebearers",
    models=5,
    movement=4,
    health=2,
    defense_profile=DefenseProfile(save=6, ward=5),
    weapon_profiles=[
        WeaponProfile(attacks=1, to_hit=4, to_wound=3, damage=1, traits=[WeaponTrait.CRIT_MORTAL])
    ],
    spearhead_properties=SpearheadProperties(arrives_3rd_round=True)
)

BleakHost = [SpoilpoxScrivenerS, PussgoyleBlightlordsS, PussgoyleBlightlordsS3, PutridBlightkingsS,
             PlaguebearersS, PlaguebearersS3]