from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Query:

    @strawberry.field
    def concat(self, a: str, b: str) -> str:
        return a + " " + b

    @strawberry.field
    def add(self, a: int, b: int) -> int:
        return a + b


schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()

app.include_router(graphql_app, prefix="/graphql")
