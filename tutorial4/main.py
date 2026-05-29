import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from data import read_file


@strawberry.type
class Employee:
	name: str
	city: str
	designation: str
	experience_in_year: str


@strawberry.type
class Query:
	@strawberry.field
	def employee(self) -> list[Employee]:
		return [Employee(**e) for e in read_file()]


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

print(schema)