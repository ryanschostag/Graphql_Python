import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Query:
    @strawberry.field(description="hello string")
    def hello(self) -> str:
        return "hello world!!!"

    @strawberry.field(description="bye string")
    def bye(self) -> str:
        return "good bye!!"


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

print(schema)