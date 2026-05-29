import strawberry


@strawberry.interface
class Player:
    name: str
    country: str


@strawberry.type
class FootballPlayer(Player):
    position: str


@strawberry.type
class CricketPlayer(Player):
    battingorder: int