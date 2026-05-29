import strawberry
from .schema import FootballPlayer, CricketPlayer
from .data import read_data


@strawberry.type
class Query:
    @strawberry.field(description="list object type implements interface")
    def fplayer(self) -> list[FootballPlayer]:
        data = read_data()
        return [FootballPlayer(**p) for p in data[0]["footballplayer"]]

    @strawberry.field(description="list object type implements interface")
    def cplayer(self) -> list[CricketPlayer]:
        data = read_data()
        return [CricketPlayer(**p) for p in data[0]["cricketplayer"]]