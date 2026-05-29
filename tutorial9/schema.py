import strawberry


@strawberry.type
class FootballPlayer:
    name: str
    country: str
    type: str
    position: str


@strawberry.type
class CricketPlayer:
    name: str
    country: str
    type: str
    battingorder: int


@strawberry.type
class Invalid:
    name: str
    country: str
    type: str
    invalid_data: str
