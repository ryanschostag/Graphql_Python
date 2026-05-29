import strawberry
from .schema import Course
from .data import read_data


@strawberry.type
class Query:
    @strawberry.field
    def course(self) -> list[Course]:
        return [Course(**c) for c in read_data()]
