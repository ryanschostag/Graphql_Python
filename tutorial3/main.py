import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from data import read_data


@strawberry.type
class Course:
	name: str
	level: str
	duration_in_year: int


@strawberry.type
class Query:
	@strawberry.field
	def course(self) -> list[Course]:
		return [Course(**c) for c in read_data()]


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

print(schema)