import collections
import random

import trueskill
import uuid
from numpy import random
import scipy

from typing import List, Iterable

# player_ids = [uuid.uuid4() for _ in range(10)]
player_ids = [i for i in range(10)]

skills = collections.defaultdict(lambda: trueskill.Rating())

ts = trueskill.TrueSkill(backend="scipy")

def create_match(player_ids: List[uuid.uuid4]):
    players = random.choice(player_ids, size=4, replace=False)
    teams = [list(players[:2]), list(players[2:])]
    teams = [make_squads(t) for t in teams]
    return teams


def make_squads(team: List[uuid.uuid4]):
    if random.random() < 0.5:
        # Squad
        return tuple(team),
    else:
        # Not squad
        return tuple([(i,) for i in team])

matches = [
    create_match(player_ids) for _ in range(100)
]
matches = [
    [((1, 2,),), ((3,), (4,))],
]

def get_team_skills(team: Iterable):
    team_skills = []
    # return [skills[player] for player in team]
    for squad in team:
        squad_skills = []
        for player in squad:
            squad_skills.append(skills[player])
        team_skills.append(tuple(squad_skills))
    return tuple(team_skills)


for match in matches:
    t1_ids, t2_ids = match
    t1, t2 = get_team_skills(t1_ids), get_team_skills(t2_ids)
    # team = [
    #     (ranking, squadsize, weight)
    # ]
    rated = ts.rate([t1, t2])
    players = [i for team in match for squad in team for i in squad]
    ratings = [i for team_rating in rated for i in team_rating]
    skills.update(zip(players, ratings))

print(skills)

