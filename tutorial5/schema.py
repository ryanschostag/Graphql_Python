import strawberry


@strawberry.type
class Weather:
    city: str
    temperature: str