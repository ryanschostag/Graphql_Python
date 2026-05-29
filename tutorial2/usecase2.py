import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

data = [
    {
        "name": "Roni",
        "city": "Cologne",
        "country": "India"

},
{
        "name": "John",
        "city": "London",
        "country": "UK"

},
{
         "name": "Maria",
         "city": "Sydney",
         "country": "Australia"
}
]

@strawberry.type
class Student:
    name: str
    city: str
    country: str


@strawberry.type
class Query:
    @strawberry.field
    def student(self) -> list[Student]:
        return [Student(**d) for d in data]


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

print(schema)
