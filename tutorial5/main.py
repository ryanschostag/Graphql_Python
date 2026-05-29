import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from data import read_data


@strawberry.type
class Weather:
	city: str
	temperature: str


@strawberry.type
class Query:
	@strawberry.field
	def city_temp(self, city: str) -> Weather:
		# reuse mapping-style logic if available
		data = read_data()
		for row in data:
			if row["city"] == city:
				return Weather(**row)
		return Weather(city=city, temperature="not found in the sequence")


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

print(schema)
