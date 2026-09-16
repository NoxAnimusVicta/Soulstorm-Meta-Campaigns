"""Pure Soulstorm setup calculations. Inputs are AFTER costs and commitments.
No human result is sampled. Returned setup must be played or supplied an outcome.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class BattleSide:
    supply:float
    manpower:float
    fleet_strength:int
    faction:str


def band(value):
    if not 0<=value<=100:raise ValueError('Resource outside 0..100')
    return min(4,max(0,int((max(1,value)-1)//20)))


def setup(player,enemy,*,player_attacking=True,defended=False,siege=False,
          bunker_levels=0,ambush=False,intel_difficulty=False,isolated=False,
          raider=None,map_capacity=None):
    """Compute teams/difficulty. Slots duplicate each side unless consented
    participating campaign allies are explicitly assigned by the referee.
    bunker_levels: active base bunker=1; upgraded=2; otherwise=0.
    """
    if min(player.fleet_strength,enemy.fleet_strength,bunker_levels)<0:
        raise ValueError('Negative strength or construction level')
    difficulty=5-band(player.supply)+band(enemy.supply)-2
    if defended and not siege:difficulty+=1 if player_attacking else -1
    difficulty+=bunker_levels if player_attacking else -bunker_levels
    if ambush:difficulty+=1 if player_attacking else -1
    if intel_difficulty and player_attacking:difficulty-=1
    if isolated and not player_attacking:difficulty+=2
    difficulty=min(5,max(1,difficulty))
    friendly=max(1,1+player.fleet_strength//5+band(player.manpower)-2)
    hostile=max(1,1+enemy.fleet_strength//5+band(enemy.manpower)-2)
    reduction=max(0,max(friendly,hostile)-4)
    if min(friendly,hostile)-reduction<1:
        raise ValueError('Source scaling cannot preserve this difference and minimum one; referee ruling required')
    friendly-=reduction;hostile-=reduction
    teams=[{'faction':player.faction,'formations':friendly},
           {'faction':enemy.faction,'formations':hostile}]
    if raider:teams.append({'faction':raider,'formations':1,'can_capture':False})
    participants=sum(t['formations'] for t in teams)
    minimum=max(2*max(t['formations'] for t in teams),participants)
    if minimum>8:raise ValueError('Participant count exceeds supported eight-slot maps; referee ruling required')
    capacity=minimum if map_capacity is None else map_capacity
    if not isinstance(capacity,int) or not minimum<=capacity<=8:raise ValueError('Map cannot accommodate the required teams')
    return dict(difficulty=difficulty,teams=teams,required_capacity=minimum,
                map_capacity=capacity,closed_slots=capacity-participants,
                outcome='awaiting reported result')
