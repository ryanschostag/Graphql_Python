import strawberry
from .schema import Employee
from .data import read_file


@strawberry.type
class Query:
    @strawberry.field
    def employee(self) -> list[Employee]:
        return [Employee(**e) for e in read_file()]