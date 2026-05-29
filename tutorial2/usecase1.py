import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

course_name = "computer science"
course_time_year = 1


@strawberry.type
class Query:
    @strawberry.field
    def name(self) -> str:
        return course_name

    @strawberry.field
    def duration(self) -> int:
        return course_time_year


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

print(schema)