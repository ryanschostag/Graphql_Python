import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from .mapping import Query
from .schema import FootballPlayer, CricketPlayer, Invalid

schema = strawberry.Schema(query=Query, types=[FootballPlayer, CricketPlayer, Invalid])
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

print(schema)
