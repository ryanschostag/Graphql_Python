import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from data import read_data


@strawberry.type
class FootballPlayer:
	name: str
	country: str
	position: str
	type: str


@strawberry.type
class CricketPlayer:
	name: str
	country: str
	battingorder: int
	type: str


@strawberry.type
class Invalid:
	name: str
	country: str
	type: str
	invalid_data: str


Player = strawberry.union("Player", (FootballPlayer, CricketPlayer, Invalid))


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


schema = strawberry.Schema(query=Query, types=[FootballPlayer, CricketPlayer, Invalid])
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

print(schema)
