import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from data import read_data


@strawberry.type
class FootballPlayer:
	name: str
	country: str
	position: str


@strawberry.type
class CricketPlayer:
	name: str
	country: str
	battingorder: int


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


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

print(schema)