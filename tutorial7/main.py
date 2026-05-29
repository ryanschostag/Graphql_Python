import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


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


@strawberry.type
class Query:
    @strawberry.field(description="coming from football player interface")
    def fplayer(self) -> FootballPlayer:
        return FootballPlayer(name="player1", country="Spain", position="Central Back")

    @strawberry.field(description="coming from cricket player interface")
    def cplayer(self) -> CricketPlayer:
        return CricketPlayer(name="player2", country="India", battingorder=1)


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

print(schema)
