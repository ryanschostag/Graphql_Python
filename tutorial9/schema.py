import strawberry


@strawberry.interface
class Player:
    name: str
    country: str
    type: str


@strawberry.type
class FootballPlayer(Player):
    position: str


@strawberry.type
class CricketPlayer(Player):
    battingorder: int


@strawberry.type
class Invalid(Player):
    invalid_data: str
