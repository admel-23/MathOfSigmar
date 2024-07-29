from src.core.unit import Unit, DefenseProfile, WeaponProfile, WeaponTrait, SpearheadProperties

ChaosLordS = Unit(
    name="Chaos Lord",
    models=1,
    movement=5,
    health=6,
    defense_profile=DefenseProfile(save=3),
    weapon_profiles=[
        WeaponProfile(attacks=5, to_hit=3, to_wound=3, damage=2, traits=[WeaponTrait.CRIT_MORTAL])
    ],
    spearhead_properties=SpearheadProperties()
)

ChaosChariotS = Unit(
    name="Chaos Chariot",
    models=1,
    movement=10,
    health=7,
    defense_profile=DefenseProfile(save=4),
    weapon_profiles=[
        WeaponProfile(attacks=6, to_hit=3, to_wound=3, damage=1),
        WeaponProfile(attacks=2, to_hit=4, to_wound=4, damage=1),
        WeaponProfile(attacks=4, to_hit=5, to_wound=3, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    spearhead_properties=SpearheadProperties()
)

ChaosWarriorsS = Unit(
    name="Chaos Warriors",
    models=5,
    movement=5,
    health=2,
    defense_profile=DefenseProfile(save=3),
    weapon_profiles=[
        WeaponProfile(attacks=2, to_hit=3, to_wound=3, rend=1, damage=1)
    ],
    spearhead_properties=SpearheadProperties()
)

ChaosKnightsS = Unit(
    name="Chaos Knights",
    models=5,
    movement=10,
    health=4,
    defense_profile=DefenseProfile(save=3),
    weapon_profiles=[
        WeaponProfile(attacks=3, to_hit=3, to_wound=3, rend=1, damage=1),
        WeaponProfile(attacks=2, to_hit=5, to_wound=3, damage=1, traits=[WeaponTrait.COMPANION])
    ],
    spearhead_properties=SpearheadProperties()
)

BloodwindLegion = [ChaosLordS, ChaosChariotS, ChaosWarriorsS, ChaosWarriorsS, ChaosKnightsS]
