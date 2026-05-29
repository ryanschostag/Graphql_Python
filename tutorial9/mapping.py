import strawberry
from .schema import FootballPlayer, CricketPlayer, Invalid, Player
from .data import read_data


@strawberry.type
class Query:
    @strawberry.field
    def player(self, playertype: str) -> list[Player]:
        data = read_data()
        if playertype == "fplayer":
            return [FootballPlayer(**p) for p in data[0]["footballplayer"]]
        elif playertype == "cplayer":
            return [CricketPlayer(**p) for p in data[0]["cricketplayer"]]
        else:
            return [Invalid(**p) for p in data[0]["invalid"]]


