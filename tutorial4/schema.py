import strawberry


@strawberry.type
class Employee:
    name: str
    city: str
    designation: str
    experience_in_year: str