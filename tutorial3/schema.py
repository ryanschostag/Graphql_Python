import strawberry


@strawberry.type
class Course:
    name: str
    level: str
    duration_in_year: int
