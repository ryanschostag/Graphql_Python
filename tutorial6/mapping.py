import strawberry


@strawberry.type
class Query:
    @strawberry.field(description="hello string")
    def hello(self) -> str:
        return "hello world!!!"

    @strawberry.field(description="bye string")
    def bye(self) -> str:
        return "good bye!!"
